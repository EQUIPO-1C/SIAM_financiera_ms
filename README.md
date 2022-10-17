# Financiera_ms

This application is a REST API CRUD using Python Flask and mongodb module Flask-Pymongo

## Development

For developemnt first you need to create the virtual enviroment

In a directory other than the main directory use this command `virtualenv <NAME YOUR WANT FOR THE VENV>` 

Then go to the root folder of the project and use this command  to install dependencies `pip install -r requirements.txt`

Finally you can run the app with this commands `py ./src/app.py` or `python ./src/app.py`

## Docker
Build your image in the root directory of the project
	
	sudo docker build -t financiera_ms_devimg .

Run the container with the next template
	sudo docker run -d -p 8000:8000 -e DB_USER=procIns_ms_C -e DB_PSWD=arquisoft2022 --name financiera_ms financiera_ms_devimg



