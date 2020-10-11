# import the necessary packages
import base64
import os
import time

import cv2
import socketio

# Disable tensorflow compilation warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

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


class DetectSign(object):
    """This class process the Video received, processes it."""

    def __init__(self):
        # capturing video
        self.video = cv2.VideoCapture(0)
        time.sleep(1)

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

    def predict(self, image_data, sess, softmax_tensor, label_lines):

        predictions = sess.run(softmax_tensor,
                               {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        max_score = 0.0
        res = ''
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            if score > max_score:
                max_score = score
                res = human_string
        return res, max_score

    # Loads label file, strips off carriage return
    def solve(self):
        label_lines = [line.rstrip() for line
                       in tf.gfile.GFile("server/logs/trained_labels.txt")]

        # Unpersists graph from file
        with tf.gfile.FastGFile("server/logs/trained_graph.pb", 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name='')

        with tf.Session() as sess:
            # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
            c = 0

            cap = self.video
            time.sleep(1)
            res, score = '', 0.0
            i = 0
            mem = ''
            consecutive = 0
            sequence = ''

            while True:
                ret, img = cap.read()
                img = cv2.flip(img, 1)

                if ret:
                    x1, y1, x2, y2 = 100, 100, 300, 300
                    img_cropped = img[y1:y2, x1:x2]

                    c += 1
                    image_data = cv2.imencode('.jpg', img_cropped)[1].tostring()

                    if i == 4:
                        res_tmp, score = self.predict(image_data, sess, softmax_tensor, label_lines)
                        res = res_tmp
                        i = 0
                        if mem == res:
                            consecutive += 1
                        else:
                            consecutive = 0
                        if consecutive == 2 and res not in ['nothing']:
                            if res == 'space':
                                sequence += ' '
                            elif res == 'del':
                                sequence = sequence[:-1]
                            else:
                                sequence += res
                            consecutive = 0
                    i += 1
                    cv2.putText(img, '%s' % (res.upper()), (100, 400), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 4)
                    cv2.putText(img, '(score = %.5f)' % (float(score)), (100, 450), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (255, 255, 255))
                    mem = res
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    sio.emit(
                        'cv2server',
                        {
                            'image': self.encode_frame(img),
                            'text': res
                        })



if __name__ == "__main__":
    try:
        start_connection()
    except TypeError:
        print("[INFO] Connection failed")
    DetectSign().solve()
