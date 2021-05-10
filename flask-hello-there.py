from flask import Flask

#Instantiate the Flask app
app = Flask(__name__)

#Create the endpoint for the home page
@app.route('/')
def index():
    return 'Hello there!'