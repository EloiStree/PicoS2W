import os
from time import time
import wifi
import mdns

class S2WLibConnectToWifi:
    def __init__(self):
        self.connected = False
        self.m_using_wifi = False

    def connect(self, ssid: str, password: str):
        try:
            wifi.radio.connect(ssid, password)
            self.connected = True
        except Exception as e:
            print(f"Failed to connect to Wi-Fi: {e}")
            self.connected = False

    def is_connected(self) -> bool:
        return self.connected and self.m_using_wifi
    
    def try_to_connect_wifi(self):
        """Connect to Wi-Fi using the credentials defined in setting.toml """
        
        WIFI_SSID = os.getenv("WIFI_SSID")
        WIFI_PASSWORD = os.getenv("WIFI_PASSWORD")
        print(f"WIFI_SSID: \"{WIFI_SSID}\"")
        print(f"Connecting to Wi-Fi with SSID: \"{WIFI_SSID}\"...")
        try:
            wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
            print("Connected to Wi-Fi!")
            self.m_using_wifi = True
        except ConnectionError as e:
            
            print("Failed to connect to Wi-Fi:", e)
            raise e
                
        print('Pico Wifi IP address is:', wifi.radio.ipv4_address)
                # Start mDNS
        mdns_server = mdns.Server(wifi.radio)
        mdns_server.hostname = os.getenv("MDNS_HOSTNAME")
        