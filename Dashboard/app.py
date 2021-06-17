#%%
from flask import Flask, render_template
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
# @app.route("/prediction")
# def prediction():
#     # Have the JSON pass though the module and return a bool

#     # If true render template for draftable, if false: undraftable, else error template.
#     if True:
#         return render_template('draftable.html')
#     elif False:
#         return render_template('undraftable.html')
#     else
#         return render_template('error.html')