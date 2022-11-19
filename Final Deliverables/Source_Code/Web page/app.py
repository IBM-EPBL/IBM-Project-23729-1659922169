import numpy as np
from flask import Flask,request,jsonfy,render_template
import requests
import json
import requests
import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "YgTKlJaXJfw0Buhk6_FCGdcAAtzUwBNBznleRI9fJ-KB"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/y_predict,methods=['POST'])
def y_predict():
    Sex=request.from("Sex")
    Chestpaintype=request.from("Chest pain type")
    FBSover120=request.from("FBS over 120")
    EKGresults=request.from("EKG results")
    Exerciseangina=request.from("Exercise angina")
    SlopeofST=request.from("Slope of ST")
    Numberofvesselsfluro=request.from("Number of vessels fluro")
    Thallium=request.from("Thallium")
    Age=request.from("Age")
    BP=request.from("BP")
    Cholesterol=request.from("Cholesterol")
    MaxHR=request.from("Max HR")
    STdepression=request.from("ST depression")

    if(Sex=="Male"):
        Sex=1
    if(Sex=="Female"):
        Sex=0
    
    if(Chestpaintype=="Typical angina"):
        Chestpaintype=0
    if(Chestpaintype=="Atypical angina"):
        Chestpaintype=1
    if(Chestpaintype=="Non-anginal pain"):
        Chestpaintype=2
    if(Chestpaintype=="Asymptomatic"):
        Chestpaintype=3
    
    if(FBSover120=="No"):
        FBSover120=0
    if(FBSover120=="Yes"):
        FBSover120=1
    
    if(EKGresults=="Normal"):
        EKGresults=0
    if(EKGresults=="Abnormal"):
        EKGresults=1
    
    if(Exerciseangina=="No"):
        EKGresults=0
    if(Exerciseangina=="Yes"):
        EKGresults=1
    
    if(SlopeofST=="Unsloping"):
        SlopeofST=1
    if(SlopeofST=="Flat"):
        SlopeofST=2
    if(SlopeofST=="Downsloping"):
        SlopeofST=3
    
    if(Numberofvesselsfluro="Zero"):
        Numberofvesselsfluro=0
    if(Numberofvesselsfluro="One"):
        Numberofvesselsfluro=1
    if(Numberofvesselsfluro="Two"):
        Numberofvesselsfluro=2
    if(Numberofvesselsfluro="Three"):
        Numberofvesselsfluro=3
    
    if(Thallium=="Normal"):
        Tallium=3
    if(Thallium=="fixed defect"):
        Tallium=6
    if(Thallium=="reversibe defect"):
        Tallium=7
    
    t=[[int(Sex),int(Chestpaintype),int(FBSover120),
    int(EKGresults),int(Exerciseangina)
    ,int(SlopeofST),int(Numberofvesselsfluro),
    int(Tallium),int(Age),int(BP)
    ,int(Cholesterol),int(MaxHR),int(STdepression)]]
    print(t)
    payload_scoring={"input_data":[{"field":[["Sex","Chestpaintype","FBSover120","EKGresults","Exerciseangina","SlopeofST","Numberofvesselsfluro"
    ,"Tallium","Age","BP","Cholesterol","MaxHR","STdepression"],values:t]}]}    
    
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/2102715e-0bc9-42dd-9036-6a7eaf97aed5/predictions?version=2022-11-18', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    predictions=response_scoring.json()
    pred=predictions['predictions'][0]['values'][0][0]
    if(pred =='Presence'):
        print("You have high probability to heart Disease Kindly approach a Doctor Take care")
    else:
        print("Hey! Your Normal Take care")
    return render_template('index.html',prediction_text=output)  
if __name__=="__main__":


    
    