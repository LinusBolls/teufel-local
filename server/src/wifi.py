import time

def set_mdns_hostname(hostname):
    try:
        import mdns
    except ImportError:
        print("Failed to set mdns hostname: 'esp' module is not available on this platform")
        return
    
    mdns_server = mdns.Server()
    mdns_server.start(hostname, "ESP32-C3 Device")
    mdns_server.add_service('_http', '_tcp', 80)
    print(f"mDNS set: {hostname}.local")

CONNECTION_ATTEMPTS = 10

def connect_wifi(ssid, password):
    try:
        import network
    except ImportError:
        print("Failed to connect to Wi-Fi: 'network' module is not available on this platform")
        return

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        wlan.connect(ssid, password)

        for _ in range(CONNECTION_ATTEMPTS):
            if wlan.isconnected():
                break
            time.sleep(1)

    if wlan.isconnected():
        print('Connected to:', wlan.ifconfig())
    else:
        print('Failed to connect!')
