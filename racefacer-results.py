import socketio
import logging
import websocket

logging.basicConfig(
    filename="socketio.log",
    # format="%(asctime)s %(levelname)s %(name)s %(message)s",
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.DEBUG,
)

# websocket.enableTrace(True)

sio = socketio.Client()

@sio.event
def connect():
    logging.info('connection established')
    sio.emit('join', 'kartarenacheb')

@sio.event
def connect_error(data):
    logging.error("The connection failed!")
    
@sio.event
def disconnect():
    logging.info('disconnected from server')

@sio.event
def kartarenacheb(data):
    logging.info(f"message received: kartarenacheb - {data}")
    # sio.emit('my response', {'response': 'my response'})
    # 
    # 42["join","kartarenacheb"]
    # sio.emit('join', 'kartarenacheb')

@sio.on('*')
def any_event(event, sid, data):
    logging.info(f"event received: {event} - {sid} - {data}")

sio.connect('https://live.racefacer.com:3123/socket.io/')
sio.wait()