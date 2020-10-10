from flask_socketio import SocketIO
from flask import Flask, render_template, request

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    """Renders home page."""
    return render_template('index.html')


@socketio.on('connect', namespace='/web')
def connect_web():
    """This funnction is triggered when web client connects successfully"""
    print('[INFO] Web client connected: {}'.format(request.sid))


@socketio.on('disconnect', namespace='/web')
def disconnect_web():
    """This funnction is triggered when web client disconnects"""
    print('[INFO] Web client disconnected: {}'.format(request.sid))


@socketio.on('connect', namespace='/cv')
def connect_cv():
    """This funnction is triggered when CV client connects successfully"""
    print('[INFO] CV client connected: {}'.format(request.sid))


@socketio.on('disconnect', namespace='/cv')
def disconnect_cv():
    """This funnction is triggered when CV client disconnects"""
    print('[INFO] CV client disconnected: {}'.format(request.sid))


@socketio.on('cv2server')
def handle_cv_message(message):
    """Streams Video and predicted word to the Web Client"""
    socketio.emit('server2web', message, namespace='/web')


if __name__ == "__main__":
    print('[INFO] Starting server at http://localhost:5001')
    socketio.run(app=app, host='0.0.0.0', port=5001)
