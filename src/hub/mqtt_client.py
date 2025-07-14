
import paho.mqtt.client as mqtt
import json
import sqlite3

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("home/network/traffic")
    client.subscribe("home/devices/+/status")

def on_message(client, userdata, msg):
    print(f"{msg.topic} {str(msg.payload)}")
    conn = sqlite3.connect('data/guardian.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (log) VALUES (?)", (msg.payload.decode(),))
    conn.commit()
    conn.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt", 1883, 60)
