#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:03:57 2020

@author: rameshveer
"""

import pandas as pd
import pickle

df = pd.read_csv('insurance.csv')

df['sex'] = pd.get_dummies(df['sex'])
df['smoker'] = pd.get_dummies(df['smoker'])

#To assign 4 different numeric values to regions, we use label encoding 

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
df['region']= label_encoder.fit_transform(df['region'])

x = df.drop('charges', axis=1)
y = df['charges']

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

### Gradient Boosting..

from sklearn.ensemble import GradientBoostingRegressor

gb_reg = GradientBoostingRegressor()

gb_reg.fit(x_train, y_train)

## Performance evaluation..

from sklearn.metrics import r2_score

R2 = r2_score(y_test, gb_reg.predict(x_test))

print("r2 score: ", R2)

# Saving model to disk
pickle.dump(gb_reg, open('model.pkl','wb'))


# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
charges = model.predict([[19,0,27.9,	0,0,3]])
print("Health Insurance Cost: $",round(charges[0],2))

