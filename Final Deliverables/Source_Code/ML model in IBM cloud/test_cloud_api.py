import requests
import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "YgTKlJaXJfw0Buhk6_FCGdcAAtzUwBNBznleRI9fJ-KB"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": ['Age','Sex','Chest pain type','BP','Cholesterol','FBS over 120','EKG results','Max HR','Exercise angina','ST depression',
                                             'Slope of ST','Number of vessels fluro',
         'Thallium'], "values": [[ 44, 1, 3, 140, 235, 0, 2, 180, 0, 0, 1, 0, 3]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/2102715e-0bc9-42dd-9036-6a7eaf97aed5/predictions?version=2022-11-18', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions=response_scoring.json()
pred=predictions['predictions'][0]['values'][0][0]
if(pred =='Presence'):
    print("You have high probability to heart Disease Kindly approach a Doctor Take care")
else:
    print("Hey! Your Normal Take care")
