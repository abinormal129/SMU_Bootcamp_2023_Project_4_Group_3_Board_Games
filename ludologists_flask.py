# Import the dependencies
import numpy as np
import pandas as pd
from flask import Flask, render_template, redirect

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/board_game_recommender")
def board_game_recommender():
    return render_template("board_game_recommender.html")

@app.route("/tableau01")
def tableau01():
    return render_template("tableau01.html")

@app.route("/tableau02")
def tableau02():
    return render_template("tableau02.html")

@app.route("/works_cited")
def works_cited():
    return render_template("works_cited.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/sample_data")
def sample_data():
    return render_template("sample_data.html")

@app.route("/write_up")
def write_up():
    return render_template("write_up.html")

# run the website
if __name__ == '__main__':
    app.run(debug=True)
