import numpy as np
from flask import Flask,render_template,request
import pickle
import pandas as pd
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

   
   


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''#
    inp =  str(request.form.get("tweet"))
    inp = inp.lower()
    import re
    ct=[]
    ct.append(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",inp).split()))
    inp=ct[0]
    data=[[0,0,inp,inp]]
    df=pd.DataFrame(data,columns=['index','class','tweet','clean_tweet'])
    df.to_csv('input.csv',index=False)
    da2=[[0,inp,0]]
    daf=pd.DataFrame(da2,columns=['index','tweet','class'])
    daf.to_csv('labels.csv',index=False)
    import preprocess
    import importlib
    importlib.reload(preprocess)
    output=model.predict(preprocess.ye)
    if(output[0]==0):
        string="Hate Speech"
    if(output[0]==1):
        string="Offensive speech"
    if(output[0]==2):
        string="Not Hate speech"
    
    return render_template('index.html', prediction_text=string)





if __name__ == "__main__":
    app.run(debug=True)

