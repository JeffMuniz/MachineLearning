endpoint = 'http://8371efdf-c760-403c-82c7-cb6aab295fdf.brazilsouth.azurecontainer.io/score' #Replace with your endpoint
key = 'NXgnZ5XJcOwoDFcxKgqgd2vvI5ZG8a9u' #Replace with your key

import json
import requests

#Features for a patient
x = [{"PatientID": 1,
      "Pregnancies": 5,
      "PlasmaGlucose": 181.0,
      "DiastolicBloodPressure": 90.6,
      "TricepsThickness": 34.0,
      "SerumInsulin": 23.0,
      "BMI": 43.51,
      "DiabetesPedigree": 2.11,
      "Age": 21.0}]

#Create a "data" JSON object
input_json = json.dumps({"data": x})

#Set the content type and authentication for the request
headers = {"Content-Type":"application/json",
           "Authorization":"Bearer " + key}

#Send the request
response = requests.post(endpoint, input_json, headers=headers)

#If we got a valid response, display the predictions
if response.status_code == 200:
    y = json.loads(response.json())
    #Get the first prediction in the results
    print("Prediction:", y["result"][0])
    if y["result"][0] == 1:
        print('Diabetic')
    else:
        print("Not Diabetic")
else:
    print(response)