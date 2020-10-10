# import the necessary packages
import base64
import random

import cv2
# from flask_socketio import SocketIO
import time
from flask import Flask, render_template, request

import socketio

sio = socketio.Client()
server_addr = "http://127.0.0.1:5001/"


@sio.event
def connect():
    print('[INFO] Successfully connected to server.')


@sio.event
def connect_error():
    print('[INFO] Failed to connect to server.')


@sio.event
def disconnect():
    print('[INFO] Disconnected from server.')


class Video(object):
    """This class process the Video received, processes it."""

    def __init__(self):
        # capturing video
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        # releasing camera
        self.video.release()

    def get_frame(self):
        """Convert the video frames to bytes"""
        # extracting frames
        ret, frame = self.video.read()
        cv2.rectangle(frame, (150, 200), (400, 400), (255, 0, 0), 2)
        ret, jpeg = cv2.imencode('.jpg', frame)
        # cv2.rectangle(jpeg, (15, 15), (150, 150), (255, 0, 0), 7)
        frame = base64.b64encode(jpeg).decode('utf-8')
        return "data:image/jpeg;base64,{}".format(frame)


def setup():
    print("trying to connect to server")
    sio.connect(
        "http://0.0.0.0:5001/",
        transports=['websocket'],
        namespaces=['/cv'],
    )
    time.sleep(1)


def main():
    setup()
    cam = Video()
    words = ['Abhishek', 'Shubhank', 'Shreya']
    while True:
        sio.emit(
            'cv2server',
            {
                'image': cam.get_frame(),
                'text': random.choice(words)
            })


if __name__ == "__main__":
    main()
