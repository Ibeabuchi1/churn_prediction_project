
import requests

host = 'churn-serving-env.eba-xw9hfupp.us-east-2.elasticbeanstalk.com'
url = f'http://{host}/churn'

customer_id = 'abc-xyz'

customer = {
    "gender": "male",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "yes",
    "phoneservice": "yes",
    "multiplelines": "no",
    "internetservice": "no",
    "onlinesecurity": "no_internet_service",
    "onlinebackup": "no_internet_service",
    "deviceprotection": "no_internet_service",
    "techsupport": "no_internet_service",
    "streamingtv": "no_internet_service",
    "streamingmovies": "no_internet_service",
    "contract": "month-to-month",
    "paperlessbilling": "no",
    "paymentmethod": "mailed_check",
    "tenure": 12,
    "monthlycharges": 19.7,
    "totalcharges": 258.35,
}


response = requests.post(url, json=customer).json()

print(response)

if response['churn'] == True:
    print(f"send promo to {customer_id}")
else:
    print('No Promo')
