import numpy as np
import pickle
from flask import Flask,request,render_template


app=Flask(__name__)

model=pickle.load(open('models/stdgrades.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=model.predict(features)
    
    output=(prediction)
    
    return render_template('index.html',prediction_text='Predicted Grade is: {}'.format(output))

if __name__ == '__main__':
    app.run()
