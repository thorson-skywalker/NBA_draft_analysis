#%%
import pandas as pd

df = pd.read_csv(r"07-20_MBB_StatsAndDraft.csv", index_col='player')
#%%

#%%
df.to_json(r'statsJSON')
# %%