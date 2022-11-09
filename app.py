from flask import Flask, render_template,request

import pandas as pd

# Unpickle model 
model = pd.read_pickle('lr_model.pickle') 

app=Flask(__name__)

@app.route("/")
def index():
    gre = int(request.args.get('g'))
    tof = int(request.args.get('t'))
    cgp = float(request.args.get('c'))
    print(gre)
    result = model.predict([[gre,tof,cgp]])
    print(result)
    print(type(result))
    return f"Chances are : {result[0] * 100:.2f}%"

    
@app.route('/form')
def about():
    return render_template('form.html')


if __name__=='__main__':
    app.run()

