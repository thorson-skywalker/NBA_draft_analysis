# %%
import pickle
import pandas as pd

# %%
def predict_single_player(player_stats):
    model_filename = './nba_LogReg_model.sav'
    loaded_model = pickle.load(open(model_filename, 'rb'))
    prediction = loaded_model.predict(player_stats)
    return prediction[0]
#%%