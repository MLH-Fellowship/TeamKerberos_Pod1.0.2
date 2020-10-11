import base64
import cv2
from ASL_Classifier.classify_webcam import solve
class Video(object):
    """This class process the Video received, processes it."""

    def __init__(self):
        # capturing video
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        # releasing camera
        self.video.release()

    def encode_frame(self, frame):
        """Takes video frames and encode it into base64 jpeg image"""

        ret, jpeg = cv2.imencode('.jpg', frame)
        frame = base64.b64encode(jpeg).decode('utf-8')
        return "data:image/jpeg;base64,{}".format(frame)

    def get_frame(self):
        """Convert the video frames to bytes"""

        # extracting frames
        ret, frame = self.video.read()

        # adding rectangular box where user is supposed to make gestures
        cv2.rectangle(frame, (150, 200), (400, 400), (255, 0, 0), 2)

        return self.encode_frame(frame)