# Health_Insurance_Cost_Prediction

  Cost incurred for Healthcare is one of the major growing problems in the world, 
  getting an insight about the costs before hand based on your health condition would be 
  beneficial for the people & the industry.
  
We will be predicting cost based on a public dataset which considers the below factors,
* age
* sex
* bmi
* children
* smoker
* region
* charges (Dependent variable)

# Algorithm's Tested for tis dataset,
1. Linear
  a. Lasso
2. Decision Tree
3. Random Forrest
4. Boosting
  a. Gradient Boosting
  b. AdaBoost
  c. xgboost

#### Gradient Boosting provides better r2 score of 0.89 and doesn't overfit between testing & training set.

#### A Web App was created with the above ML Model using Flask and deployed with Heroku.

#### Webapp can be accessed in below link,
  https://health-insurance-cost-predict.herokuapp.com
  

