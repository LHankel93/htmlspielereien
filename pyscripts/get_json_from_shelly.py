import traceback
import logging
import pandas as pd
import requests
import datetime
# import json
try:

    link = "http://192.168.178.12/status"
    response = requests.get(link)

    # json in response parsen in einzelne Werte
    device_id = 1
    timestamp = datetime.datetime.now()
    # json_body: str = response.json()["wifi_sta"]
    json_body: str = response.json()

    print(json_body["mac"])
    # TODO: additionally get the actual device ID from the API to save in the DB

    # sql = """INSERT INTO wifi_sta_hist (device_id, timestamp, connected, ssid, ip, rssi) VALUES (%s, %s, %s, %s, %s, %s)"""
    # vals = (device_id, timestamp, json_body["connected"],
    #        json_body["ssid"], json_body["ip"], json_body["rssi"])
    # cursor.execute(sql, vals)
    # conn.commit()
    # print(cursor.rowcount, "rows inserted.")

    # print(response.status_code)
    # print(response.headers)
    # print(response.text)
    # print(response.json()["wifi_sta"])

    # id, device_id, timestamp, connected, ssid, ip, rssi
    # Daten in DB persistieren
    # zum Testen Zugangsdaten nur lokal
    exit(0)
except Exception as e:
    logging.error(traceback.format_exc())
    exit(1)
    # Logs the error appropriately.
