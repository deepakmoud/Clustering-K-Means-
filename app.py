# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 12:38:32 2021

@author: deepak
"""

import numpy as np
from flask import Flask, request, jsonify, render_template

import pickle


app = Flask(__name__)
model = pickle.load(open('linearregression.pkl','rb')) 


@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    
    
    
    '''
    For rendering results on HTML GUI
    '''
    exp = float(request.args.get('exp'))
    
    prediction = model.predict([[exp]])
    
        
    return render_template('index.html', prediction_text='Regression Model  has predicted salary for given experinace is : {}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)