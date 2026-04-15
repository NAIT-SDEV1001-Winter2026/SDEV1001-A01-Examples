#Read the sigthings.csv file and display on the page as json 

from flask import Flask,jsonify
from csv import DictReader

app = Flask(__name__)

def load_ufo_data(filepath):
    sightings = []
    with open(filepath,"r",newline="")as f:
        reader = DictReader(f)
        for row in reader:
            sightings.append(row)
    return sightings


#Create a home page that diplays a heading(h1) "UFO Sightings"
@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>UFO Sightings</title>
        </head>
        <body>
            <h1>UFO Sightings</h1>
        </body>
    </html>
"""
#enclosing the string in """ allows us to return this literal format

#new route to display the content of the CSV file in JSON format. Call the route ufo_sightings_file
#path to the csv file is:    data/sightings.csv

#route 
@app.route("/ufo_sightings_file")
#function header
def get_sightings_info():
#load data
    sightings = load_ufo_data("data/sightings.csv")
#return as JSON
    return jsonify(sightings)
    