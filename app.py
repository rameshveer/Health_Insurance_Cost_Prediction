#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:36:19 2020

@author: rameshveer
"""

import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_values = [float(x) for x in request.form.values()]
    input_array = [np.array(input_values)]
    pred_value = model.predict(input_array)

    charges = round(pred_value[0],1)

    return render_template('index.html', prediction_text='Health Insurance Predicted Cost = $ {}0'.format(charges))

if __name__ == "__main__":
    app.run(debug=True)
