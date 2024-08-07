import socketio
import logging
import websocket
import pyodbc
import os

db_server = os.environ.get('DB_SERVER')
db_database= os.environ.get('DB_DATABASE')
db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')

conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={db_server};DATABASE={db_database};UID={db_username};PWD={db_password}'

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

@sio.on('*')
def any_event(event, sid, data):
    logging.info(f"event received: {event} - {sid} - {data}")

    data = [
        ('John', 'Doe', 30),
        ('Jane', 'Smith', 25)
    ]

    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    insert_query = "INSERT INTO YourTableName (FirstName, LastName, Age) VALUES (?, ?, ?)"
    cursor.executemany(insert_query, data)
    conn.commit()
    conn.close()

sio.connect('https://live.racefacer.com:3123/socket.io/')
sio.wait()
