import paho.mqtt.client as mqtt
import os
import json
from . import database as db
from .data_models import Device, NetworkLog, SystemEvent

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT Broker with result code {rc}")
    client.subscribe("device/+/status")
    client.subscribe("network/logs")
    client.subscribe("system/events")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.topic} {msg.payload.decode()}")
    try:
        payload = json.loads(msg.payload.decode())
        if msg.topic.startswith("device/"):
            device_id = msg.topic.split("/")[1]
            # This is a simplified update. In a real app, you'd upsert or validate.
            conn = db.get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT OR REPLACE INTO devices (id, name, ip_address, status) VALUES (?, ?, ?, ?)",
                (device_id, payload.get("name", device_id), payload.get("ip_address", "unknown"), payload.get("status", "online"))
            )
            conn.commit()
        elif msg.topic == "network/logs":
            conn = db.get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO network_logs (timestamp, source_ip, destination_ip, protocol, port) VALUES (?, ?, ?, ?, ?)",
                (payload.get("timestamp"), payload.get("source_ip"), payload.get("destination_ip"), payload.get("protocol"), payload.get("port"))
            )
            conn.commit()
        elif msg.topic == "system/events":
            conn = db.get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO system_events (timestamp, service, event_type, message) VALUES (?, ?, ?, ?)",
                (payload.get("timestamp"), payload.get("service"), payload.get("event_type"), payload.get("message"))
            )
            conn.commit()

    except json.JSONDecodeError:
        print(f"Error decoding JSON from topic {msg.topic}: {msg.payload.decode()}")
    except Exception as e:
        print(f"Error processing MQTT message: {e}")

def start_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    mqtt_broker_host = os.getenv("MQTT_BROKER_HOST", "localhost")
    mqtt_broker_port = int(os.getenv("MQTT_BROKER_PORT", 1883))

    try:
        client.connect(mqtt_broker_host, mqtt_broker_port, 60)
        client.loop_start() # Start the loop in a non-blocking way
    except Exception as e:
        print(f"Could not connect to MQTT broker: {e}")

