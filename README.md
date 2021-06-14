# NBA_draft_analysis

## Purpose
An analysis of college basketball statistics and their influence on getting selected in the NBA draft.

## Responsibilities Due by 5/30
- Luke: Dashboard, README/GitHub
- Parker: Database
- Brady: Machine Learning
- Brooks: ETL

~~## Responsibilities Due by 5/23:~~
- ~~Luke - README/GitHub~~
- ~~Parker - Build Sample Database - House data~~
- ~~Brady - Logistic Regression Model~~
- ~~Brooks - Gather sample datasets/ estimate framework~~

## Communication Protocol

- Primary Form of Communication: Slack
- Meetings on Mondays and Wednesdays 7:00pm - 9:00pm
- Meetings between memebers regarding collaboration on related segments to be setup as needed through slack.

*** Note: Luke will be unavailable Thursday 5/27 and Saturday 5/29, but will have some availability periodically on Friday***

## Hypothesis
> A college basketball player's season statistics can be used to determine whether or not that athlete will be drafted into the NBA.

## Presentation

[Google Slides](https://docs.google.com/presentation/d/1axGv6Pm4fon6xYLTXVXtWeYSV64yRAL0FVUgOXtctLQ/edit?usp=sharing)

## Data Sources
- [College Statistics](https://basketball.realgm.com/ncaa/stats/2018/Averages/Qualified/All/Season/All/points/desc/1/)
- [2018 NBA Draft Results](https://www.basketball-reference.com/draft/NBA_2018.html)

## Technologies Used

### Data Cleaning and Analysis
Using Python with the Pandas library, data was scraped from 2 sources. Saving each individual year as their own CSV for NCAA season stats and draft results. 
Cycled through each “season stats” CSV and cleaned accents, punctuation, and suffixes for data format consistency. Combined all “season stats” cleaned CSVs into a master CSV. 
Cycled through each “draft results” CSV and cleaned accents, punctuation, and suffixes for data format consistency. Combined all “draft results” cleaned CSVs into a master CSV. 

### Database Storage
The database engine that we’re using for the NBA Draft Analysis is PostgreSQL and pgAdmin as our client / management tool that we using to manipulate the data. So far, the database has a total of three tables that were storing for the NBA Draft Analysis.  The first table is storing college stats by player, the second is storing the NBA Draft results and the third we queried the two tables to combine the players stats with draft result by left join on the player’s names for the machine learning model to analyze.  The database is hosted in the cloud by Amazon Web Services (AWS) by using the Relational Database Service (RDS).  The cleaned data is then stored in an Amazon S3 bucket where it is made available to the team for the machine learning model to reference.

### Machine Learning
. Description of preliminary data preprocessing

Data is pulled from the S3 storage location as a .csv file directly into pandas. In preprocessing, all text columns are dropped, leaving the only numerical data and an ID provided from the database. The data is then further reduced to include only features commonly found in basketball players' individual statistics. Because of the large disparity in undrafted players (>1900 per season) and drafted players (<60 per season), combination over- and under-sampling is then done using SMOTEENN. The final stage of preprocessing is to split the data into training and test datasets and scale the X data.

2. Description of preliminary feature engineering and preliminary feature selection, including their decision-making process

Basketball statistics are primarily numerical in nature, so the intial feature cut to remove all text columns resulted in only removing the players' position and names. Redundant features (such as Field Goals Attempted, Field Goals Made, and Field Goal %) were also present and needed to be removed. Finally, the most common basketball statistics (points, rebounds, assists, steals, turnovers, and minutes per game, as well as games played). These were selected because they are the most commonly tracked statistics that all players considering entering the draft from college will have readliy available. This step also took care of removing the redundant features, as they were not included in the list of features to keep.

3. Description of how data was split into training and testing sets

The default 0.75/0.25 train/test split was used with sklearn's train_test_split function.

4. Explanation of model choice, including limitations and benefits

Logistic regression, random forest, support vector machines, and gradient boosting machine learning techniques were all tested with the same scaled and over/under sampled dataset. Of the four models, random forest and gradient boosting were both above an accuracy score of 0.90, while the other two are at 0.79. Of the two ensemble learners, random forest outscored gradient boosting by a score of 0.97 to 0.94 and was selected based on that merit.

Aside from having the highest accuracy score, the random forest model is robust against overfitting and to outliers and non-linear data, making it ideal for the NBA draft analysis dataset. The limitations of a random forest model are not significant to the data being used. The main disadvantages large amount of compute needed to test the model in real time (which will not be happening as the model will be updated only once per year) and that the model is not as good for regression but only for prediction, which is already the purpose of the model.

### Dashboard
Using a template from BootStrap, a dashboard will be built to display important information from our analysis. There will also be included an interactive portion that will allow the user to evaluate their chances of being drafted by inputing their own stats. This will be accomplished using a javascript function that will run that data through our trained model.