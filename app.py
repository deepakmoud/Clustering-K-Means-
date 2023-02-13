!pip install flask-ngrok
import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_ngrok import run_with_ngrok
import pickle


app = Flask(__name__)
model = pickle.load(open('/content/drive/My Drive/kmeanscluster.pkl','rb'))   
run_with_ngrok(app)

@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
  '''
  For rendering results on HTML GUI
  '''
  income = int(request.args.get('income'))
  score = int(request.args.get('score'))
    
    
  predict = model.predict([[income,score ]])
  if predict==[0]:
    result="Customer is careless"

  elif predict==[1]:
    result="Customer is standard"
  elif predict==[2]:
    result="Customer is Target"
  elif predict==[3]:
    result="Customer is careful"

  else:
    result="Custmor is sensible"
    
        
  return render_template('index.html', prediction_text='Model  has predicted  : {}'.format(result))


app.run()
