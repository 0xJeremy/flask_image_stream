import requests

url = 'http://192.168.1.49:8080/'

def Get_Image():
	try:
		data = requests.get(url + 'get_image')
		print(data)
	except Exception as e:
		print(e)
		data = None
	return data

Get_Image()