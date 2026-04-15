# What is Flask?
# A lightweight/micro webserver for development of web pages using Python (along with HTML and other tools)
# to run the website: flask --app flask_library run --reload

from flask import Flask #importing the Flask module
from flask import jsonify # turns python data (lists, dictionaries) into JSON format

app = Flask(__name__) #Create a Flask object called app. __name__ is where the app lives

#a route is a webpage
# / is the root webpage
# @ is called a decorator
# a route is always followed by a function that returns what the page should display
@app.route("/")
def home(): #function called home (could be any name)
    return "<h1>Welcome to the books library!</h1>"#Note, this is not semanticaly correct due to missing <html><head><title>. We will add those in later examples

books = [
{"title":"1984", "author":"George Well"},
{"title":"Grilled Cheese", "author":"Shane Bell"}
]

#page to display a list of book dictionaries as json
@app.route("/books") #route for new page called books
def books_list():
    return jsonify(books)#return the books list as JSON format
