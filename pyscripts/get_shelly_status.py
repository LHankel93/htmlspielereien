import traceback
import logging
import pandas as pd
import requests
import datetime
# import json
import mariadb
# db_user = "shelly_python"
# db_pw = "yllesh_nthonp"
# db_table = 'wifi_sta_hist'
try:
    conn = mariadb.connect(host="localhost", port=3306,
                           user="shelly_python", password="yllesh_nthonp")

    cursor = conn.cursor(named_tuple=True)
    cursor.execute("SET NAMES utf8")
    cursor.execute("USE shelly_status")

    link = "http://192.168.178.12/status"
    response = requests.get(link)

    # json in response parsen in einzelne Werte
    # device_id = 1
    timestamp = datetime.datetime.now()
    json_body_wifi: str = response.json()["wifi_sta"]

    json_body = response.json()
    device_id = json_body["mac"]

    # print(json_body["mac"])

    # Beispiel: cur.execute("INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria","DB"))
    try:
        sql = "INSERT INTO wifi_sta_hist (device_id, timestamp, connected, ssid, ip, rssi) VALUES (?, ?, ?, ?, ?, ?)"
        vals = (device_id, timestamp, json_body_wifi["connected"],
                json_body_wifi["ssid"], json_body_wifi["ip"], json_body_wifi["rssi"])
        cursor.execute(sql, vals)
        conn.commit()
        print(cursor.rowcount, "rows inserted.")
    except mariadb.Error as e:
        print(f"Error: {e}")

    # print(response.status_code)
    # print(response.headers)
    # print(response.text)
    # print(response.json()["wifi_sta"])

    # id, device_id, timestamp, connected, ssid, ip, rssi
    # Daten in DB persistieren
    # zum Testen Zugangsdaten nur lokal

    cursor.execute('SELECT * FROM wifi_sta_hist')

    for i in cursor:
        print(i)
    cursor.close()
    conn.close()
    exit(0)
except Exception as e:
    logging.error(traceback.format_exc())
    print(f"Error: {e}")
    cursor.close()
    conn.close()
    exit(1)
    # Logs the error appropriately.
