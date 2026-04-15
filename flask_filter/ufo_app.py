#read the sightings.csv file and display on the page

from flask import Flask, jsonify,request
import csv #or from csv import dictreader


app = Flask(__name__)

def load_ufo_data(filepath):
    sightings = []
    with open(filepath,"r",newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sightings.append(row)
    return sightings



#create a home page that displays a heading(h1) "UFO Sightings"
@app.route("/")
def home():
    #return a semantic webpage
    return """
    <html>
        <head>
            <title>UFO Sightings</title>
        </head>
        <body>
            <h1>UFO Sightings</h1>
        </head>
    <html>
    """

#enclosing the return string in """ allows us to write it out literaly like we would in an html file. Easier to read

#page to display contents of CSV file as json called ufo_sightings_file

#decorator
@app.route("/ufo_sightings_file")
#function header
def get_sightings_info():
#load data
    sightings = load_ufo_data("data/sightings.csv")
#return the json data
    return jsonify(sightings)

#formatted output with HTML
@app.route("/ufo_sightings_formatted")
def get_sightings_formatted():
    sightings = load_ufo_data("data/sightings.csv")

    ufo_html = ""
    for sighting in sightings:
        ufo_html += f"<li>{sighting["city"]}, {sighting["state"]}</li>"

    return f"""
    <html>
        <body>
            <h1>UFO sighting locations</h1>
            <ul>
                {ufo_html}
            </ul>
        </body>
    </html>
    """

@app.route("/ufo_sightings_country",methods=['GET'])
def get_country_sightings():
    #get the arguments from the querystring. If it is not there return''
    country = request.args.get('country','')
    sightings = load_ufo_data("data/sightings.csv")
    #make a copy of the sightings list
    filter_sightings = sightings.copy()
    for sighting in sightings:
        #If there is a country argument and it does not match the current row(sighting), remove it from filtered sightings
        if country and sighting['country'].lower() != country.lower():
            filter_sightings.remove(sighting)
    #return the filtered list
    return jsonify(filter_sightings)

#Instead of removing rows that do not match, start with an empty filtered_sightings and add the ones that do match
@app.route('/ufo_sightings_add', methods=['GET'])
def get_sightings_add():
    country = request.args.get('country', '')
    sightings = load_ufo_data("data/sightings.csv")
    filtered_sightings = []

    for sighting in sightings:
        if not country or sighting['country'].lower() == country.lower():
                filtered_sightings.append(sighting)
    return jsonify(filtered_sightings)

@app.route("/ufo_sightings_comments",methods=["GET"])
def get_sightings_comments():
    comment = request.args.get("comment", "")
    sightings = load_ufo_data("data/sightings.csv")
    filtered_sightings = []

    for sighting in sightings:
        comments = sighting.get("comments","").lower()

        if comment in comments:
            filtered_sightings.append(sighting)
    return jsonify(filtered_sightings)