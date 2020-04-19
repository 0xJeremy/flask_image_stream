import requests

url = 'http://192.168.1.49:5000/'

def Get_Image():
	try:
		data = requests.get(url)
		f = open('image.png', 'wb')
		f.write(data.content)
		f.close()
	except Exception as e:
		print(e)

Get_Image()
