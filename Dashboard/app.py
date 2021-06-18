#%%
from flask import Flask, render_template, request
from flask import jsonify
from predict_player import predict_single_player
import pandas as pd
#%%
app = Flask(__name__)
#%%
@app.route("/")
def main():
    return render_template('index.html')
#%%
@app.route("/schools")
def schools():
    return render_template('schools.html')
#%%
@app.route("/draftPicks")
def draftpicks():
    return render_template('index.html')
#%%
@app.route("/analysis")
def analysis():
    return render_template('analysis.html')
#%%
@app.route("/stats")
def stats():
    return render_template('stats.html')
#%%
@app.route("/averages")
def averages():
    return render_template('averages.html')
#%%
@app.route("/chances")
def chances():
    return render_template('chances.html')
#%%
@app.route("/prediction")
# function to pass the JSON though the module and return a bool
def prediction():     
    # Request JSON
    ppg = request.args.get('ppg')
    rpg = request.args.get('rpg')
    apg = request.args.get('apg')
    spg = request.args.get('spg')
    tov = request.args.get('tov')
    fg_percent = request.args.get('fg_percent')
    threes = request.args.get('threes')
    freeThrows = request.args.get('freeThrows')
    inputStats = jsonify({
        "ppg" : ppg,
        "rpg" : rpg,
        "apg" : apg,
        "spg" : spg,
        "tov" : tov,
        "FG%" : fg_percent,
        "3P%" : threes,
        "FT%" : freeThrows
    })

    # Check to see inputStats being create correctly
    return jsonify({ "prediction" : ppg})

    # Pass the input json through the prediction.py script and return a JSON with the results
    # return jsonify({ "prediction" : predict_single_player(inputStats)})
#%%