import json
import uasyncio as asyncio
import os

from src.microdot.microdot import Microdot, send_file, Response
from src.microdot.websocket import with_websocket

from src.env import Env
from src.wifi import connect_wifi, set_mdns_hostname
from src.speaker_controls import speaker_controls
from src.html import get_index_html

ws_clients = set()

app = Microdot()

@app.route('/')
async def index(request):
    return Response(get_index_html(), headers={ 'Content-Type': 'text/html' })

@app.route('/ws') # clients can connect to ws://localhost:80/ws
@with_websocket
async def websocket_handler(request, ws):
    ws_clients.add(ws)
    try:
        while True:
            # any error thrown here will terminate the websocket connection
            message = await ws.receive()
            
            data = json.loads(message)
            
            for key, value in data['input'].items():
                speaker_controls.set_value(key, value)

            # forward the change event to all other websocket clients so they're in sync
            for client in ws_clients:
                if client is not ws:
                    await client.send(message)
    except Exception:
        pass

    finally:
        ws_clients.remove(ws)

async def start_webserver():
    port = 80
    await app.start_server(debug=True, host='0.0.0.0', port=port)

if Env.has_wifi_credentials:
    connect_wifi(Env.wifi_ssid, Env.wifi_password)
    set_mdns_hostname("balls")

asyncio.run(start_webserver())