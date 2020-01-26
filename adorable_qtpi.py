import paho.mqtt.client as mqtt
import json
import requests
import os

LOCAWOOD_TOKEN = os.environ["LOCAWOOD_TOKEN"]
MQTT_HOST = os.environ["MQTT_HOST"]
MQTT_USERNAME = os.environ["MQTT_USERNAME"]
MQTT_TOPIC = os.environ["MQTT_TOPIC"]

# Optional envs
MQTT_CLIENT_ID = os.getenv("MQTT_CLIENT_ID")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    if rc != 0:
        print("Failed to connect to broker :'(")

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print('Got message %s', msg.payload)
    localwood_payload = json.loads(msg.payload.decode('utf-8'))
    localwood_payload['token'] = LOCAWOOD_TOKEN

    try:
        requests.post('http://localhost:8080/sockets', data = localwood_payload)
    except Exception as err:
        print(err)

client = mqtt.Client(client_id = MQTT_CLIENT_ID)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

client.connect(MQTT_HOST)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
