import requests

url = 'http://192.168.1.49:5000/'

def Get_Image():
	try:
		data = requests.get(url)
		with open('image.png', 'wb') as f:
			f.write(data.content)
	except Exception as e:
		print(e)

Get_Image()
