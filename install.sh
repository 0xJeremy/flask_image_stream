git clone https://github.com/0xJeremy/flask_image_stream.git
cd flask_image_stream
echo "FLASK_APP=/home/pi/flask_image_stream/app.py" >> ~/.bashrc
echo "flask run --host=0.0.0.0" >> ~/.bashrc
source ~/.bashrc
echo "Done installing."