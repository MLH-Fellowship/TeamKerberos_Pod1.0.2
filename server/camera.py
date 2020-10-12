# import the necessary packages
import os
import time
import base64
import cv2
import socketio
import io
from imageio import imread

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


def predict(image_data, sess, softmax_tensor, label_lines):
    """Predicts the Character using the frame of the video"""

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


def generate_video(im):
    """Generates frames after prediction"""

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

        res, score = '', 0.0
        i = 0
        mem = ''
        consecutive = 0
        sequence = ''

        ret = True
        img = im
        img = cv2.flip(img, 1)

        if ret:
            x1, y1, x2, y2 = 100, 100, 300, 300
            img_cropped = img[y1:y2, x1:x2]

            c += 1
            image_data = cv2.imencode('.jpg', img_cropped)[1].tostring()
            res_tmp, score = predict(image_data, sess, softmax_tensor, label_lines)
            mem = res
            detected = {
                'text': res_tmp
            }
            return detected


def encode_frame(frame):
    """Takes video frames and encode it into base64 jpeg image"""

    ret, jpeg = cv2.imencode('.jpg', frame)
    frame = base64.b64encode(jpeg).decode('utf-8')
    return "data:image/jpeg;base64,{}".format(frame)


def strtonumpy(s):
    img = imread(io.BytesIO(base64.b64decode(s[22:])))
    return img

