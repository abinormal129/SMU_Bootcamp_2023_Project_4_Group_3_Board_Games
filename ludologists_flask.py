# Import the dependencies
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, text
from flask import Flask, render_template, redirect

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
hawaii_engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    """List all available api routes"""
    return (
        f"""<h1>The Data Ludologists:<h1><br/>
        <h4><a href="/api/v1.0/board_game_recommender" target="_blank">Get a Board Game Recommendation</a><h4><br/>
        <h4><a href="/api/v1.0/tableau" target="_blank">Interactive Board Game Analysis</a><h4><br/>
        <h4><a href="/api/v1.0/works_cited" target="_blank">Works Cited</a><h4><br/>
        <h4><a href="/api/v1.0/about_us" target="_blank">About Us</a><h4><br/>
        <h4><a href="/api/v1.0/sample_data" target="_blank">Sample Data</a><h4><br/>
        """
    )

@app.route("/api/v1.0/board_game_recommender")
def board_game_recommender():
    return render_template("board_game_recommender.html")

@app.route("/api/v1.0/tableau")
def tableau():
    return render_template("board_game_recommender.html")

@app.route("/api/v1.0/works_cited")
def works_cited():
    return render_template("works_cited.html")

@app.route("/api/v1.0/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/api/v1.0/sample_data")
def sample_data():
    return render_template("sample_data.html")

# run the website
if __name__ == '__main__':
    app.run(debug=True)
