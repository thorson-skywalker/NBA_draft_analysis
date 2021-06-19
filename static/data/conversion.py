#%%
import pandas as pd
import numpy as np
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
data_2007_2020 = 'https://s3.amazonaws.com/parkerhiggins-nba-draft-bucket/07-20_MBB_StatsAndDraft.csv'
bball_stats = pd.read_csv(data_2007_2020)
bball_stats.head()
# %%
bball_essential_stats = bball_stats.drop(columns={'gp','mpg','fgm','fga','3PA','3PM','ftm','fta','pf','orb','drb','bpg','season_year','player1','draft_year'})
bball_essential_stats.head()
# %%
bball_essential_stats['draft_status'] = (bball_essential_stats['pk'].isnull().astype(bool))
bball_essential_stats.head()
# %%
bball_drafts = bball_essential_stats.drop(columns={'pk'})
bball_drafts.head()
# %%
drafted_players = bball_drafts[bball_drafts['draft_status'] == False]
undrafted_players = bball_drafts[bball_drafts['draft_status'] == True]
drafted_players.head()
#%%
undrafted_players.head()
# %%
drafted_avgs = drafted_players['FG%'].mean()
# %%
drafted_avgs
# %%
