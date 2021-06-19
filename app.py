# %%
from flask import Flask, render_template, request
from flask import jsonify
from predict_player import predict_single_player
import pandas as pd
# %%
app = Flask(__name__)
# %%


@app.route("/")
def main():
    return render_template('index.html')
# %%


@app.route("/schools")
def schools():
    return render_template('schools.html')
# %%


@app.route("/draftPicks")
def draftpicks():
    return render_template('index.html')
# %%


@app.route("/analysis")
def analysis():
    return render_template('analysis.html')
# %%


@app.route("/stats")
def stats():
    return render_template('stats.html')
# %%


@app.route("/averages")
def averages():
    return render_template('averages.html')
# %%


@app.route("/chances")
def chances():
    return render_template('chances.html')
# %%


@app.route("/prediction")
# function to pass the JSON though the module and return a bool
def prediction():

    player_stats = {}

    player_stats['ppg'] = request.args.get('ppg')
    player_stats['rpg'] = request.args.get('rpg')
    player_stats['apg'] = request.args.get('apg')
    player_stats['spg'] = request.args.get('spg')
    player_stats['tov'] = request.args.get('tov')
    player_stats['FG%'] = request.args.get('fg_percent')
    player_stats['3P%'] = request.args.get('threes')
    player_stats['FT%'] = request.args.get('freeThrows')
    player = []
    player.append(player_stats)
    player_df = pd.DataFrame(player)

    # Pass the input json through the prediction.py script and return a JSON with the results
    if predict_single_player(player_df):
        return render_template('draftable.html')

    return render_template('undraftable.html')
# %%