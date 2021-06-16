import pickle

# Load the trained model
rel_file_path = './lr_2007_2019.sav'
model = pickle.load(open(rel_file_path, 'rb'))

# Make predictions on single player
# The input of this is a dataframe with a row for each player to be predicted
prediction = model.predict(player_data_df)