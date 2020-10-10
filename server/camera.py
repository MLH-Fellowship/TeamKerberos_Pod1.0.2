# import the necessary packages
import cv2


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
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
