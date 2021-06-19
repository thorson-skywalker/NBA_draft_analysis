# %%
import pickle
import pandas as pd


# def predict_single_player(stats_df):
#     # data_url = './input.json'
#     print(type(stats_df))
#     player_df = stats_df

#     player_df = player_df[['ppg','rpg','apg','spg','tov','FG%','3P%','FT%']]

#     model_filename = './nba_LogReg_model.sav'
#     loaded_model = pickle.load(open(model_filename, 'rb'))

#     prediction = loaded_model.predict(player_df)

#     return prediction[0]
# %%
def predict_single_player(player_stats):
    model_filename = './nba_LogReg_model.sav'
    loaded_model = pickle.load(open(model_filename, 'rb'))
    prediction = loaded_model.predict(player_stats)
    return prediction[0]
#%%