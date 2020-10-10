# import the necessary packages
from flask import Flask, render_template, Response
from camera import Video

app = Flask(__name__)


@app.route('/')
def index():
    """Rendering the Homepage"""
    return render_template('index.html')


def gen(camera):
    """Yields the Real-Time Video frames"""
    while True:
        # get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    """Returns the video as a Response which is then rendered on the webpage"""
    return Response(gen(Video()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0', port='5000', debug=True)
