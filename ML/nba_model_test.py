# %%
import pandas as pd
import nba_ml
# %%
data_2007_2020 = 'https://s3.amazonaws.com/parkerhiggins-nba-draft-bucket/07-20_MBB_StatsAndDraft.csv'
# %%
raw_nba_data = nba_ml.import_data(data_2007_2020)
raw_nba_data.head()

# %%
training_data = nba_ml.preprocess_raw_data(raw_nba_data)
# %%
rf_model_trained = nba_ml.random_forest_model(
    training_data[0], training_data[1])
# %%
fake_player_stats = {'ppg': 19.2, 'mpg': 29.9, 'rpg': 3.8,
                     'apg': 3.6, 'spg': 0.8, 'gp': 33, 'tov': 0.4}

player_draft_pred = nba_ml.predict_player(fake_player_stats, rf_model_trained)
# %%
player_draft_pred
# %%
raw_data[raw_data['pk'] == 8]
# %%
training_data[0]
# %%
training_data[1]
# %%
type(rf_model_trained)

# %%
