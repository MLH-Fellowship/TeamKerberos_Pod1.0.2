# import the necessary packages
import random
import time
import socketio
from video_processing import Video

sio = socketio.Client()
server_address = "http://0.0.0.0:5001/"


@sio.event
def connect():
    """This funnction is triggered when CV client is successfully connected to the server"""
    print('[INFO] Successfully connected to server.')


@sio.event
def connect_error():
    """This funnction is triggered when CV client fails to connect to the server"""
    print('[INFO] Failed to connect to server')


@sio.event
def disconnect():
    """This funnction is triggered when CV client is disconnected from the server"""
    print('[INFO] Disconnected from server.')


def start_connection():
    """Establishes websocket connection to the server"""
    print("[INFO] Establishing Connection")
    sio.connect(
        server_address,
        transports=['websocket'],
        namespaces=['/cv'],
    )
    time.sleep(1)


def stream_video():
    """Streams base64 enocoded image to the server using websocket"""

    # dummy data
    words = ['Abhishek', 'Shubhank', 'Shreya']

    while True:
        sio.emit(
            'cv2server',
            {
                'image': Video().get_frame(),
                'text': random.choice(words)
            })


if __name__ == "__main__":
    try:
        start_connection()
    except TypeError:
        print("[INFO] Connection failed")
    stream_video()




