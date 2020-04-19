from flask import Flask, send_file
from threading import Thread
import cv2

class camera:
	def __init__(self, resolution=(640, 480), framerate=30):
		self.cam = cv2.VideoCapture(2)

	def capture(self):
		ret, frame = self.cam.read()
		cv2.imwrite('image.png', frame)

cam = camera()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	global camera
	try:
		cam.capture()
		return send_file('image.png', attachment_filename='image.png')
	except Exception as e:
		return str(e)
	