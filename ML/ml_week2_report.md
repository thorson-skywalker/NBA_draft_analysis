# NBA Draft Analysis
## Week 2: Machine Learning (06/06/2021)

### Deliverables for ML Model:

**1. Description of preliminary data preprocessing**  
  
  Data is pulled from the S3 storage location as a .csv file directly into pandas. In preprocessing, all text columns are dropped, leaving the only numerical data and an ID provided from the database. The data is then further reduced to include only features commonly found in basketball players' individual statistics. Because of the large disparity in undrafted players (>1900 per season) and drafted players (<60 per season), combination over- and under-sampling is then done using SMOTEENN. The final stage of preprocessing is to split the data into training and test datasets and scale the X data.

**2. Description of preliminary feature engineering and preliminary feature selection, including their decision-making process**

  Basketball statistics are primarily numerical in nature, so the intial feature cut to remove all text columns resulted in only removing the players' position and names. Redundant features (such as Field Goals Attempted, Field Goals Made, and Field Goal %) were also present and needed to be removed. Finally, the most common basketball statistics (points, rebounds, assists, steals, turnovers, and minutes per game, as well as games played). These were selected because they are the most commonly tracked statistics that all players considering entering the draft from college will have readliy available. This step also took care of removing the redundant features, as they were not included in the list of features to keep.

**3. Description of how data was split into training and testing sets**

The default 0.75/0.25 train/test split was used with sklearn's train_test_split function.

**4. Explanation of model choice, including limitations and benefits**

  Logistic regression, random forest, support vector machines, and gradient boosting machine learning techniques were all tested with the same scaled and over/under sampled dataset. Of the four models, random forest and gradient boosting were both above an accuracy score of 0.90, while the other two are at 0.79. Of the two ensemble learners, random forest outscored gradient boosting by a score of 0.97 to 0.94 and was selected based on that merit. 

  Aside from having the highest accuracy score, the random forest model is robust against overfitting and to outliers and non-linear data, making it ideal for the NBA draft analysis dataset. The limitations of a random forest model are not significant to the data being used. The main disadvantages large amount of compute needed to test the model in real time (which will not be happening as the model will be updated only once per year) and that the model is not as good for regression but only for prediction, which is already the purpose of the model.