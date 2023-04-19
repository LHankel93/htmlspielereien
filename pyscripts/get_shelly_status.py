import pandas as pd
import requests
import time
import datetime
import json
import sqlite3
# import pyodbc
import mariadb
# db_user = "shelly_python"
# db_pw = "yllesh_nthonp"
# db_table = 'wifi_sta_hist'

conn = mariadb.connect(host="localhost", port=3306,
                       user="shelly_python", password="yllesh_nthonp")

cursor = conn.cursor(named_tuple=True)
cursor.execute("SET NAMES utf8")
cursor.execute("USE shelly_status")

link = "http://192.168.178.12/status"
response = requests.get(link)

# json in response parsen in einzelne Werte
device_id = 1
timestamp = datetime.datetime.now()
json_body:str = response.json()["wifi_sta"]

sql = """INSERT INTO wifi_sta_hist (device_id, timestamp, connected, ssid, ip, rssi) VALUES (%s, %s, %s, %s, %s, %s)"""
vals = (device_id, timestamp, json_body["connected"],
        json_body["ssid"], json_body["ip"], json_body["rssi"])
cursor.execute(sql, vals)
conn.commit()
print(cursor.rowcount, "rows inserted.")

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
