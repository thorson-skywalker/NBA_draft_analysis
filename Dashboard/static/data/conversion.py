#%%
import pandas as pd
#%%
predictions_df = pd.read_json('2021_predictions.json')
predictions_df.head(10)
# %%
predictions_df = predictions_df[['Player', 'Team', "PPG", 'RPG','APG','SPG','TOV','FG%','3P%','FT%']]
predictions_df.head(10)
#%%
predictions_df = predictions_df.reset_index(drop=True)
predictions_df.head(10)
#%%
predictions_df = predictions_df.rename(columns={"FG%": "fieldGoal_percent","3P%": "threes","FT%": "freeThrow_percent"})
#%%
for col in predictions_df.columns:
    print(col)
#%%
predictions_df.to_json('./cleaned_predictions.json', orient='records')
#%%
