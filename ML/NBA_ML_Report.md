# NBA Draft Analysis

## Model Summary and Results

## Report Deliverables:

### Description of data preprocessing

  Data is pulled from the S3 storage location as a .csv file directly into pandas. In preprocessing, all text columns are dropped, leaving the only numerical data and an ID provided from the database. The data is then further reduced to include only features commonly found in basketball players' individual statistics. Because of the large disparity in undrafted players (>1900 per season) and drafted players (<60 per season), combination over- and under-sampling is then done using SMOTEENN. The final stage of preprocessing is to split the data into training and test datasets and scale the X data.

### Description of feature engineering and the feature selection, including the team's decions-making progress

  Basketball statistics are primarily numerical in nature, so the intial feature cut to remove all text columns resulted in only removing the players' position, name, and team. Redundant features (such as Field Goals Attempted, Field Goals Made, and Field Goal %) were also present and needed to be removed. Finally, the most common basketball statistics (points, rebounds, assists, steals, turnovers, and minutes per game, as well as games played). These were selected because they are the most commonly tracked statistics that all players considering entering the draft from college will have readliy available. This step also took care of removing the redundant features, as they were not included in the list of features to keep.

### Description of how data was split into training and testing sets



### Explanation of model choice, including limitations and benefits



### Explanation of changes in model choice (if changes occurred between the Segment 2 & 3 deliverables)



### Description of how model was trained (or retrained, if they are using an existing model)



### Description and explanation of model's confusion matrix, including final accuracy score



### Model addresses the question or problem the team is solving


_Note: If statistical analysis is not included as part of the current analysis, include a description of how it would be included in the next phase of the project_








## Week 3: Machine Learning (06/13/2021)

The third segment of the machine learning part of the NBA Draft Analysis was two parts - first, save and export the model using python's `pickle` module, and second, to test the model using a real draft class.

The first part of the segment was successful in exporting the trained model as a `.sav` file, using the following code:

```py
model_filename = 'nba_rf_model.sav'
pickle.dump(rf, open(model_filename, 'wb'))
```
The second part of the segment, however, exposed errors in the machine learning model. 

Using the training and test sets created during preprocessing, the model was performing with a >0.97 accuracy score, which included precision and recall above 0.98 for predicting drafted players. 

This week, however, draft data 2020 was removed entirely from the training data to be used as a test. After multiple iterations finding the best `RandomForestClassifier` parameters, the best accuracy score achieved using the 2020 draft data as a test was 0.95, which is still acceptable. However, for predicting players who would be drafted, the precision and recall dropped to 0.15 and 0.28, respectively. This indicates that in its current stage, the model is unable to reliably predict that a player will be drafted, but, due to the low number of false negatives (28 of 2000 data points), it can tell a prospective player if he has very little chance of being drafted.

### Using the Model

The most recent versions of the Random Forest, Logistic Regression, SVM, and Gradient Boosting models are saved in the `ML` directory within the main folder of the project. At the time of writing, the model `lr_2007_2019.sav` is the model with the least number of false positives and should be used. To use within a file saved in the main project directory:

```py
import pickle

# Load the trained model
rel_file_path = './ML/lr_2007_2019.sav'
model = pickle.load(open(rel_file_path, 'rb'))

# Make predictions on single player
# The input of this is a dataframe with a row for each player to be predicted
prediction = model.predict(player_data_df)
```
Calling `prediction` will then return a ndarray in which the first value is either a 1 (indicating the player has a chance of being drafted) or a 0 (indicating the player has very little chance of being drafted).

## Week 2: Machine Learning (06/06/2021)

### Deliverables for ML Model:

**Description of preliminary data preprocessing**  
  
  Data is pulled from the S3 storage location as a .csv file directly into pandas. In preprocessing, all text columns are dropped, leaving the only numerical data and an ID provided from the database. The data is then further reduced to include only features commonly found in basketball players' individual statistics. Because of the large disparity in undrafted players (>1900 per season) and drafted players (<60 per season), combination over- and under-sampling is then done using SMOTEENN. The final stage of preprocessing is to split the data into training and test datasets and scale the X data.

**Description of preliminary feature engineering and preliminary feature selection, including their decision-making process**

  Basketball statistics are primarily numerical in nature, so the intial feature cut to remove all text columns resulted in only removing the players' position and names. Redundant features (such as Field Goals Attempted, Field Goals Made, and Field Goal %) were also present and needed to be removed. Finally, the most common basketball statistics (points, rebounds, assists, steals, turnovers, and minutes per game, as well as games played). These were selected because they are the most commonly tracked statistics that all players considering entering the draft from college will have readliy available. This step also took care of removing the redundant features, as they were not included in the list of features to keep.

**Description of how data was split into training and testing sets**

The default 0.75/0.25 train/test split was used with sklearn's train_test_split function.

**Explanation of model choice, including limitations and benefits**

  Logistic regression, random forest, support vector machines, and gradient boosting machine learning techniques were all tested with the same scaled and over/under sampled dataset. Of the four models, random forest and gradient boosting were both above an accuracy score of 0.90, while the other two are at 0.79. Of the two ensemble learners, random forest outscored gradient boosting by a score of 0.97 to 0.94 and was selected based on that merit. 

  Aside from having the highest accuracy score, the random forest model is robust against overfitting and to outliers and non-linear data, making it ideal for the NBA draft analysis dataset. The limitations of a random forest model are not significant to the data being used. The main disadvantages large amount of compute needed to test the model in real time (which will not be happening as the model will be updated only once per year) and that the model is not as good for regression but only for prediction, which is already the purpose of the model.