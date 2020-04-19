from flask import Flask, send_file
import cv2

cam = cv2.VideoCapture(0)

def capture():
	ret, frame = cam.read()
	cv2.imwrite('image.png', frame)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	try:
		capture()
		return send_file('image.png', attachment_filename='image.png')
	except Exception as e:
		return str(e)
