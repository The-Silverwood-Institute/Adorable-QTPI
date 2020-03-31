# Adorable-QTPI

Consumes messages from an MQTT topic and sends them to [Localwood's API](https://github.com/The-Silverwood-Institute/Localwood). You would use this microservice in conjunction with an MQTT broker such as [Flespi](https://flespi.com/) to control the lights in your home remotely.

## Requirements

- Python 3
- paho-mqtt `pip3 install -r requirements.txt`

## Usage

You will need multiple environment variables (see code) to configure the connection to an MQTT broker and to authenticate with Localwood.

1. Run server with: `python3 adorable_qtpi.py`
2. Run Localwood on the same host

## Problems?

If you have problems or questions feel free to [open an issue](https://github.com/The-Silverwood-Institute/Localwood/issues/new). Pull requests always welcome :smile_cat:
