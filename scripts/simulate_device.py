
import paho.mqtt.client as mqtt
import time
import json

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

client = mqtt.Client()
client.on_connect = on_connect

client.connect("localhost", 1883, 60)

client.loop_start()

while True:
    # Simulate network traffic
    traffic_payload = {
        "timestamp": time.time(),
        "source_ip": "192.168.1.100",
        "destination_ip": "8.8.8.8",
        "bytes_sent": 1500
    }
    client.publish("home/network/traffic", json.dumps(traffic_payload))
    print(f"Published network traffic: {traffic_payload}")

    # Simulate device status
    device_payload = {
        "timestamp": time.time(),
        "device_id": "camera_living_room",
        "status": "online"
    }
    client.publish("home/devices/camera_living_room/status", json.dumps(device_payload))
    print(f"Published device status: {device_payload}")

    time.sleep(10)
