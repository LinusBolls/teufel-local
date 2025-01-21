# teufel.local server

a micropython program that serves a html page with control sliders for the volume, input mode, etc of the teufel speaker. the client communicates with the server via websocket to maintain a realtime connection. the clients are kept in sync by the webserver via websocket.
when the server receives events from the client, it performs the servo movements to change the physical controls of the teufel speaker.

the server is based on [microdot](https://microdot.readthedocs.io), a minimalistic python web framework.

## getting started

for local development, install micropython using a package manager of your choice:

`$ brew install micropython`

and run the file:

`micropython src/main.py`

the page will be available at http://localhost:80. the port can be changed by defining a `PORT` environment variable.

by setting a local hostname for your device:

`$ sudo scutil --set HostName teufel; sudo scutil --set LocalHostName teufel; sudo scutil --set ComputerName teufel; sudo killall mDNSResponder`

devices in your network will be able to access the page at http://teufel.local.
