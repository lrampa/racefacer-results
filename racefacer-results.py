import socketio
import logging
import websocket
import pyodbc
import os

db_server = os.environ.get('DB_SERVER')
db_database= os.environ.get('DB_DATABASE')
db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')

conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={db_server};DATABASE={db_database};UID={db_username};PWD={db_password};TrustServerCertificate=yes'

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
    # {'data': {'type': 'session', 'status_string': 'in_progress', 'event_name': 'Session #43', 'time_left': '00:07:12', 'time_left_in_seconds': 432, 'duration_type': 'min', 'total_laps': 12, 'current_lap': 5, 'has_pole': False, 'ranking_key': 'by_time', 'has_pits': False, 'has_stint': False, 'is_endurance': False, 'penalties': [], 'runs': [{'id': 339414, 'pos': 1, 'pole': None, 'country_code': 'es', 'name': 'Günther Jonah', 'team': 'Günther Jonah', 'kart': '10', 'kart_id': 72, 'kart_color': 'eea400', 'current_lap': '', 'total_laps': 5, 'last_time': '1:02.711', 'last_time_short': '62.711', 'last_time_raw': 62711, 'prev_time_raw': 63398, 'best_time': '1:02.711', 'best_time_raw': 62711, 's1': '-', 's2': '-', 's3': '-', 's4': '-', 's1_status': 'good', 's2_status': 'good', 's3_status': 'good', 's4_status': 'good', 'gap': '-', 'int': '-', 'number_of_pits': 0, 'total_driver_changes': '', 'current_pit_time': '', 'in_pit': False, 'last_passing': 1722242061101, 'avg_lap': '1:03.289', 'avg_lap_raw': 63289, 'consistency_lap': '0.578', 'consistency_lap_raw': 578, 'current_lap_start_timestamp': 1722242063, 'current_lap_start_microtimestamp': 1722242063392, 'current_lap_milliseconds': 12000, 'run_status': 'in_progress'}, {'id': 339412, 'pos': 2, 'pole': None, 'country_code': 'es', 'name': 'PODHRADSKÝ TOMÁŠ', 'team': 'PODHRADSKÝ TOMÁŠ', 'kart': '16', 'kart_id': 78, 'kart_color': 'eea400', 'current_lap': '', 'total_laps': 5, 'last_time': '1:03.926', 'last_time_short': '63.926', 'last_time_raw': 63926, 'prev_time_raw': 64519, 'best_time': '1:03.926', 'best_time_raw': 63926, 's1': '-', 's2': '-', 's3': '-', 's4': '-', 's1_status': 'good', 's2_status': 'good', 's3_status': 'good', 's4_status': 'good', 'gap': '+1.215', 'int': '+1.215', 'number_of_pits': 0, 'total_driver_changes': '', 'current_pit_time': '', 'in_pit': False, 'last_passing': 1722242050269, 'avg_lap': '1:04.366', 'avg_lap_raw': 64366, 'consistency_lap': '0.440', 'consistency_lap_raw': 440, 'current_lap_start_timestamp': 1722242052, 'current_lap_start_microtimestamp': 1722242052241, 'current_lap_milliseconds': 23000, 'run_status': 'in_progress'}, {'id': 339411, 'pos': 3, 'pole': None, 'country_code': 'es', 'name': 'PODHRADSKY VACLAV', 'team': 'PODHRADSKY VACLAV', 'kart': '11', 'kart_id': 73, 'kart_color': 'eea400', 'current_lap': '', 'total_laps': 5, 'last_time': '1:04.730', 'last_time_short': '64.730', 'last_time_raw': 64730, 'prev_time_raw': 73090, 'best_time': '1:04.730', 'best_time_raw': 64730, 's1': '-', 's2': '-', 's3': '-', 's4': '-', 's1_status': 'good', 's2_status': 'good', 's3_status': 'good', 's4_status': 'good', 'gap': '+2.019', 'int': '+0.804', 'number_of_pits': 0, 'total_driver_changes': '', 'current_pit_time': '', 'in_pit': False, 'last_passing': 1722242069507, 'avg_lap': '1:07.862', 'avg_lap_raw': 67862, 'consistency_lap': '3.132', 'consistency_lap_raw': 3132, 'current_lap_start_timestamp': 1722242071, 'current_lap_start_microtimestamp': 1722242071469, 'current_lap_milliseconds': 4000, 'run_status': 'in_progress'}, {'id': 339413, 'pos': 4, 'pole': None, 'country_code': 'es', 'name': 'Karel Kastner', 'team': 'Karel Kastner', 'kart': '1', 'kart_id': 65, 'kart_color': 'eea400', 'current_lap': '', 'total_laps': 4, 'last_time': '1:24.820', 'last_time_short': '84.820', 'last_time_raw': 84820, 'prev_time_raw': 80903, 'best_time': '1:20.903', 'best_time_raw': 80903, 's1': '-', 's2': '-', 's3': '-', 's4': '-', 's1_status': 'good', 's2_status': 'good', 's3_status': 'good', 's4_status': 'good', 'gap': '+18.192', 'int': '+16.173', 'number_of_pits': 0, 'total_driver_changes': '', 'current_pit_time': '', 'in_pit': False, 'last_passing': 1722242059566, 'avg_lap': '1:22.861', 'avg_lap_raw': 82861, 'consistency_lap': '1.958', 'consistency_lap_raw': 1958, 'current_lap_start_timestamp': 1722242061, 'current_lap_start_microtimestamp': 1722242061322, 'current_lap_milliseconds': 14000, 'run_status': 'in_progress'}, {'id': 339417, 'pos': 5, 'pole': None, 'country_code': 'es', 'name': 'Andre Hendrich', 'team': 'Andre Hendrich', 'kart': '33', 'kart_id': 409, 'kart_color': '5d28ae', 'current_lap': '', 'total_laps': 1, 'last_time': '-', 'last_time_short': '-', 'last_time_raw': None, 'prev_time_raw': None, 'best_time': '-', 'best_time_raw': None, 's1': '-', 's2': '-', 's3': '-', 's4': '-', 's1_status': 'good', 's2_status': 'good', 's3_status': 'good', 's4_status': 'good', 'gap': '-', 'int': '-', 'number_of_pits': 0, 'total_driver_changes': '', 'current_pit_time': '', 'in_pit': False, 'last_passing': 1722242071347, 'avg_lap': '-', 'avg_lap_raw': None, 'consistency_lap': '-', 'consistency_lap_raw': 0, 'current_lap_start_timestamp': 1722242076, 'current_lap_start_microtimestamp': 1722242075546, 'current_lap_milliseconds': -1000, 'run_status': 'in_progress'}], 'timestamp': 1722242075, 'timestamp_socket': 1722242076}, 'race_predictor_data': [], 'slug': 'kartarenacheb', 'type': 'live-timing', 'socket': None}

    # ('session', 'in_progress', 'Session #118', '0:01:17', '77', 'min', '10', '11', 'FALSE', 'by_time', 'FALSE', 'FALSE', 'FALSE', '1722533931', '1722542279', '341033', '1', '', 'es', 'Valeriia Karpuntsova', 'Valeriia Karpuntsova', '13', '55', '29abe1', '', '11', '49,137', '49,137', '49137', '50679', '46,09', '46090', '-', '-', '-', '-', 'good', 'good', 'good', 'good', '-', '-', '0', '', '', 'FALSE', '1,72253E+12', '49,643', '49643', '3,553', '3553', '1722533931', '1,72253E+12', '0', 'in_progress')
    data = []
    # iterate over data['data']['runs'] and create a tuple for each run
    for run in data['data']['runs']:
        data.append((
            data['data']['type'],
            data['data']['status_string'],
            data['data']['event_name'],
            data['data']['time_left'],
            data['data']['time_left_in_seconds'],
            data['data']['duration_type'],
            data['data']['total_laps_race'],
            data['data']['current_lap_race'],
            data['data']['has_pole'],
            data['data']['ranking_key'],
            data['data']['has_pits'],
            data['data']['has_stint'],
            data['data']['is_endurance'],
            data['data']['timestamp'],
            data['data']['timestamp_socket'],
            run['id'],
            run['pos'],
            run['pole'],
            run['country_code'],
            run['name'],
            run['team'],
            run['kart'],
            run['kart_id'],
            run['kart_color'],
            run['current_lap'],
            run['total_laps'],
            run['last_time'],
            run['last_time_short'],
            run['last_time_raw'],
            run['prev_time_raw'],
            run['best_time'],
            run['best_time_raw'],
            run['s1'],
            run['s2'],
            run['s3'],
            run['s4'],
            run['s1_status'],
            run['s2_status'],
            run['s3_status'],
            run['s4_status'],
            run['gap'],
            run['int'],
            run['number_of_pits'],
            run['total_driver_changes'],
            run['current_pit_time'],
            run['in_pit'],
            run['last_passing'],
            run['avg_lap'],
            run['avg_lap_raw'],
            run['consistency_lap'],
            run['consistency_lap_raw'],
            run['current_lap_start_timestamp'],
            run['current_lap_start_microtimestamp'],
            run['current_lap_milliseconds'],
            run['run_status'],
        ))
        (data['data']['type'], )

    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    insert_query = """
        INSERT INTO racefacer.dbo.racefacer_results (inserted, [type], status_string, event_name, time_left, time_left_in_seconds, duration_type, total_laps_race, current_lap_race, has_pole, ranking_key, has_pits, has_stint, is_endurance, [timestamp], timestamp_socket, id, pos, pole, country_code, name, team, kart, kart_id, kart_color, current_lap, total_laps, last_time, last_time_short, last_time_raw, prev_time_raw, best_time, best_time_raw, s1, s2, s3, s4, s1_status, s2_status, s3_status, s4_status, gap, [int], number_of_pits, total_driver_changes, current_pit_time, in_pit, last_passing, avg_lap, avg_lap_raw, consistency_lap, consistency_lap_raw, current_lap_start_timestamp, current_lap_start_microtimestamp, current_lap_milliseconds, run_status)
        VALUES(sysdatetime(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.executemany(insert_query, data)
    conn.commit()
    conn.close()

sio.connect('https://live.racefacer.com:3123/socket.io/')
sio.wait()
