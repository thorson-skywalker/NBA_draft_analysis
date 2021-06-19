# NBA Draft Analysis: Machine Learning Report

## Model Summary and Results

  Using the NCAA men's basketball season statistics from 2007-2020, a logistic regression classificer was trained to predict if a player was statistically likely to be drafted in the upcoming NBA draft. The final model was unable to predict this with any precision, however, it was able to determine who was statistically unlikely to be drafted with high precision (>99%).
  
  For full details on data preprocessing, feature selection, model selection, and results, please continue reading below.

# Machine Learning Details

## Data Preprocessing

  Data is pulled from the S3 storage location as a .csv file directly into pandas. In preprocessing, all text columns are dropped, leaving the only numerical data and an ID provided from the database. The data is then further reduced to include only features commonly found in basketball players' individual statistics. Because of the large disparity in undrafted players (>1900 per season) and drafted players (<60 per season), combination over- and under-sampling is then done using SMOTEENN. The final stage of preprocessing is to split the data into training and test datasets and scale the X data.

## Feature Engineering

  Basketball statistics are primarily numerical in nature, so the intial feature cut to remove all text columns resulted in only removing the players' position, name, and team. Redundant features (such as Field Goals Attempted, Field Goals Made, and Field Goal %) were also present and needed to be removed. Finally, the most common basketball statistics (points, rebounds, assists, steals, turnovers, and shooting percentages). These were selected because they are commonly tracked statistics that all players considering entering the draft from college will have readliy available. This step had the unintended benefit removed the redundant features.

## Training and Testing Datasets

  Initially, the data was being split into training and test sets using sklearn's `train_test_split()`. After the initial training of the model (using 2007 - 2020 data), the model was recreated using 2007 - 2019 data (removing the 2020 data), while the 2020 data and draft results were used to test the model over an entire draft class. The results for the 2020 draft class were considerably less accurate than what was found with the test dataset from `train_test_split()`, so the test size was reduced from the default 25% to only 5% for the training of the final model in order to improve the precision of the model.

## Initial Model Choice

  Logistic Regression, SVM (Support Vector Machines), Random Forest, and Gradient Boosting classifiers were all considered and tested for this project. Initially, when using only the train/test split dataset, random forest and gradient boosting were both above an accuracy score of 0.90, while the other two were below 0.80. Of the two ensemble learners, random forest outscored gradient boosting by a score of 0.97 to 0.94 and was selected based on that merit. 

  Aside from having the highest accuracy score, the random forest model is robust against overfitting and to outliers and non-linear data, making it ideal for the NBA draft analysis dataset. The limitations of a random forest model are not significant to the data being used. The main disadvantages large amount of compute needed to test the model in real time (which will not be happening as the model will be updated only once per year) and that the model is not as good for regression but only for prediction, which is already the purpose of the model.

## Final Model Choice

  After testing the initially-chosen random forest model with the 2020 season and draft data, it was clear that more testing was needed with various models and input parameters.

  A total of 38 varous model and input combinations were tested and logged in an excel workbook (snapshot below, link [here](https://github.com/thorson-skywalker/NBA_draft_analysis/blob/main/ML/2020_tests/2020_draft_model_testing.xlsx)). Model type, test set size, number of input features, number of estimators or iterations (depending on model type), over/under sampling technique, and scaled vs un-scaled data were all tested to find the best fit.

  None of the models were able to accurately predict which players were drafted in 2020 with high enough precision to be useful. The testing was able to provide several models that had high precision with players who were not drafted, indicating that they could predict which players would _**not**_ be drafted. Of the models with high precision with respect to undrafted players, a logistic regression classifier with a test data split of 5%, using eight features, 1000 estimators (trees), and smoteenn over/under sampling had the fewest number of false negatives (3 of 2000 test datapoints) and was selected for the final model.

## Model Training

  The model was trained using 95% of the data from the 2007 - 2020 NCAA basketball seasons and associated NBA drafts using the `fit()` method from `sklearn.LogisticRegression`.

## Final Confusion Matrix and Classification Report

  Using the test data from `train_test_split()`, the logistic regression classifier had 883 True Negatives, 1116 True Positives, 174 False Negatives, and 174 False Positives. It had a final accuracy score of 0.856, which was lower than many of the models tested using that same data.

  However, when using the 2020 data, the selected linear regression model had the confusion matrix and classification report shown below (_note: the confusion matrix shows, from upper left to lower right, True Negatives, False Positives, False Negatives, True Positives):

<img src='conf_matrix.png'>

  The confusion matrix shows only 3 false negatives (of 1460 total negative predictions), leading to a 99.8% precision when predicting players would not be drafted. The accuracy score is low, at only 74.7%, due to the high number of players being predicted as draftable. It is important to note that this model cannot tell a player that he is statistically likely to be drafted, but it can tell him if he is statistically unlikely to be drafted.

## Results

  The team set out to determine if common basketball statistics from a college player's most recent season could be used to predict, using machine learning, if that player would be drafted or not in the upcoming draft. The model was unable to predict with any percision if a player would be drafted, however, it was able to answer a similar question with high precision: _Is the player statistically unlikely to be drafted?_