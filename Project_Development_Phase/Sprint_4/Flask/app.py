from flask import Flask, request, render_template,session, url_for,redirect,flash
import pickle
import inputScript
from passlib.hash import  pbkdf2_sha256
import json


app = Flask(__name__,template_folder='templates')
model = pickle.load(open('Website_dt.pkl','rb'))

@app.route("/")
def helloworld():
    return render_template("/home.html")

@app.route("/predicturl")
def predicturl():
    return render_template("/predict1.html")

@app.route("/predict" ,methods=["POST","GET"] )
def predict():
    if request.method == 'POST':
        url = request.form['url']
        checkprediction = inputScript.main(url)
        print(url)
        print(checkprediction)
        prediction = model.predict(checkprediction)
        print(prediction)
        output=prediction[0]
    
        if output==1 :
            return render_template("/output1.html")
    
        elif output==-1 :
            return render_template("/output.html")

@app.route("/project_details")
def support():
    return render_template("/project_details.html")

@app.route("/addurl")
def addurl():
    return render_template("/addurl.html")

@app.route("/about")
def about():
    return render_template("/about.html")


if __name__ =="__main__":
    app.run(debug=True)