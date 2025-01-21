def get_parent_dir(filepath):
    parts = filepath.split("/")
    return "/".join(parts[:-2]) if len(parts) > 1 else "/"

server_dir = get_parent_dir(__file__)

def read_env_file(filepath):
    env_vars = {}
    try:
        with open(filepath, 'r') as f:
            for line in f:
                if '=' in line and not line.strip().startswith('#'):
                    key, value = line.strip().split('=', 1)
                    env_vars[key] = value
    except OSError:
        print("Error: .env file not found")
    return env_vars

raw_env = read_env_file(server_dir + "/.env")

wifi_ssid = raw_env.get('WIFI_SSID')
wifi_password = raw_env.get('WIFI_PASSWORD')

class Env:
    wifi_ssid = wifi_ssid
    wifi_password = wifi_password
    
    has_wifi_credentials = wifi_ssid and wifi_password
