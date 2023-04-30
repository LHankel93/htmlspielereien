import traceback
import logging
import pandas as pd
import requests
from requests import ConnectTimeout
import datetime
# import json
import mariadb
# set the following connection details according to your db install.
# do not save them in this file as clear text as I did.
# "Don't do as I do, do as I say."
# db_user = "shelly_python"
# db_pw = "yllesh_nthonp"
# db_table = 'wifi_sta_hist'

# Set the DB Connection and the Cursor
try:
    conn = mariadb.connect(host="localhost", port=3306,
                           user="shelly_python", password="yllesh_nthonp")

    cursor = conn.cursor(named_tuple=True)
    cursor.execute("SET NAMES utf8")
    cursor.execute("USE shelly_status")
    # fill variables for the insert
    ip = "192.168.178.12" # 192.168.178.12 my 3d printer ip
    link = "http://"+ip+"/status"
    timestamp = datetime.datetime.now()
    # device_id = 1
    # ssid = "standard_ssid"
    # connected = False
    # rssi = -128

    # Try to get a response from the smart device, if yes Insert status data into db
    # if response fails (requests.ConnectionError) display error to user, Insert into DB that device is not reachable.
    # Those values will have to be set manually here, since device can't fill the response.
    try:
        response = requests.get(link, timeout=3)
        # json in response parsen in einzelne Werte
        timestamp = datetime.datetime.now()
        json_body_wifi: str = response.json()["wifi_sta"]

        json_body = response.json()
        device_id = json_body["mac"]

        # DEBUG:
        # print(json_body["mac"])

        # example: cur.execute("INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria","DB"))
        # if we reach the following try/exception block, that means the resposne was retrieved successfully
        # insert data as planned.
        try:
            sql = "INSERT INTO wifi_sta_hist (device_id, timestamp, connected, ssid, ip, rssi) VALUES (?, ?, ?, ?, ?, ?)"
            vals = (device_id, timestamp, json_body_wifi["connected"],
                    json_body_wifi["ssid"], json_body_wifi["ip"], json_body_wifi["rssi"])
            cursor.execute(sql, vals)
            conn.commit()
            print(cursor.rowcount, "rows inserted.")
        except mariadb.Error as e:
            print(f"Error: {e}")
    except requests.ConnectionError as e:
        # Data could not be retrieved, aka Device is likely disconnected from the network.
        # I want to insert data into the DB that corresponds with that status
        # aka device_id (MAC-address) has to be queried from the DB with the last known IP.
        # column "connected" = 0; SSID = last known SSID; IP = already known from the request; RSSI = -128 (lowest possible value for TINYINT 127)
        print("oh no.")
        print(f"Error: {e}")
        sql = "SELECT device_id, ssid FROM wifi_sta_hist WHERE ip = ? AND id = (SELECT id FROM wifi_sta_hist WHERE ip = ? ORDER BY id DESC LIMIT 1 ) ORDER BY id ASC"
        vals = (ip, ip)
        cursor.execute(sql, vals)
        device_id_off = 1
        ssid_off = "standard_ssid"
        # retrieve some values from the cursor so we can fill in the necessary values for our "fake insert"
        for (device_id, ssid) in cursor:
            device_id_off = device_id
            ssid_off = ssid
        try:
            # print(device_id, ssid_off) # debug, works
            sql = "INSERT INTO wifi_sta_hist (device_id, timestamp, connected, ssid, ip, rssi) VALUES (?, ?, ?, ?, ?, ?)"
            # use values as described a few lines above
            vals = (device_id_off, timestamp, False, ssid_off, ip, -128)
            cursor.execute(sql, vals)
        except mariadb.Error as e:
            print("Fehler beim Einfügen von Fake Daten.")
            print(f"Error: {e}")
    except requests.JSONDecodeError as e:
        print(f"Error: {e}")
    # json in response parsen in einzelne Werte
    # timestamp = datetime.datetime.now()
    # json_body_wifi: str = response.json()["wifi_sta"]

    # json_body = response.json()
    # device_id = json_body["mac"]

    # DEBUG:
    # print(json_body["mac"])

    # Beispiel: cur.execute("INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria","DB"))

    # print(response.status_code)
    # print(response.headers)
    # print(response.text)
    # print(response.json()["wifi_sta"])

    # id, device_id, timestamp, connected, ssid, ip, rssi
    # Daten in DB persistieren
    # zum Testen Zugangsdaten nur lokal
    conn.commit()
    cursor.execute('SELECT * FROM wifi_sta_hist')

    for i in cursor:
        print(i)

except Exception as e:
    logging.error(traceback.format_exc())
    print(f"Error: {e}")
    cursor.close()
    conn.close()
    exit(1)
    # Logs the error appropriately.
finally:
    cursor.close()
    conn.close()
    print("--------------Finished.--------------")
    exit(0)
