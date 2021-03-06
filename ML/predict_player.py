# %%
import pickle
import pandas as pd


def predict_single_player():
    data_url = './input.json'
    player_df = pd.read_json(data_url)

    model_filename = './nba_LogReg_model.sav'
    loaded_model = pickle.load(open(model_filename, 'rb'))

    prediction = loaded_model.predict(player_df)

    return prediction[0]
