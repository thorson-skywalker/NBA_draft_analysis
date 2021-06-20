# NBA_draft_analysis

## Purpose
An analysis of college basketball statistics and their influence on getting selected in the NBA draft.

## Communication Protocol

- Primary Form of Communication: Slack
- Meetings on Mondays and Wednesdays 7:00pm - 9:00pm

## Hypothesis
> A college basketball player's season statistics can be used to determine whether or not that athlete will be drafted into the NBA.

## Presentation

[Presentation](https://docs.google.com/presentation/d/1axGv6Pm4fon6xYLTXVXtWeYSV64yRAL0FVUgOXtctLQ/edit?usp=sharing)

## Data Sources
- [College Statistics](https://basketball.realgm.com/ncaa/stats/2018/Averages/Qualified/All/Season/All/points/desc/1/)
- [2018 NBA Draft Results](https://www.basketball-reference.com/draft/NBA_2018.html)

## Dashboard

- [Heroku Dashboard](https://nba-draft-predictor.herokuapp.com/)

## Technologies Used

### Data Cleaning and Analysis
Using Python with the Pandas library, data was scraped from 2 sources. Saving each individual year as their own CSV for NCAA season stats and draft results. 
Cycled through each “season stats” CSV and cleaned accents, punctuation, and suffixes for data format consistency. Combined all “season stats” cleaned CSVs into a master CSV. 
Cycled through each “draft results” CSV and cleaned accents, punctuation, and suffixes for data format consistency. Combined all “draft results” cleaned CSVs into a master CSV. 

### Database Storage
The database engine that we’re using for the NBA Draft Analysis is PostgreSQL and pgAdmin as our client / management tool that we using to manipulate the data. So far, the database has a total of three tables that were storing for the NBA Draft Analysis.  The first table is storing college stats by player, the second is storing the NBA Draft results and the third we queried the two tables to combine the players stats with draft result by left join on the player’s names for the machine learning model to analyze.  The database is hosted in the cloud by Amazon Web Services (AWS) by using the Relational Database Service (RDS).  The cleaned data is then stored in an Amazon S3 bucket where it is made available to the team for the machine learning model to reference.

### Machine Learning

Using the NCAA men's basketball season statistics from 2007-2020, a logistic regression classificer was trained to predict if a player was statistically likely to be drafted in the upcoming NBA draft. The final model was unable to predict this with any precision, however, it was able to determine who was statistically unlikely to be drafted with high precision (>99%).
  
For full details on data preprocessing, feature selection, model selection, and results, please follow this [link](https://github.com/thorson-skywalker/NBA_draft_analysis/blob/main/ML/NBA_ML_Report.md).

### Dashboard
Using a template from BootStrap, a dashboard was built to display important information from our analysis. There is also included an interactive portion that will allow the user to evaluate their chances of being drafted by inputing their own stats. This will be accomplished using a javascript function that will run that data through our trained model.