from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Instantiate the Flask app and connect it to the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://obiwan:456123@localhost:5432/hellothere'
db = SQLAlchemy(app)

#Create a class to represent the table we want to access
class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
db.create_all()

#Create the endpoint for the home page
@app.route('/')
def index():
    person = Person.query.first()
    return 'Hello there! <br/>General ' + person.name.split(" ")[-1] + '! You are a bold one!'

#Use the main method to override the default server settings
if __name__ == '__main__':
    #Allow other devices on the network to access this server through port 3030
    app.run(host="0.0.0.0", port="3030")