import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "kritikat"
TOKEN = "lkjhgfdsa"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "graph1"
graph_config = {
    "id" : GRAPH_ID,
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai",
}

headers = {
    "X-USER-TOKEN" : TOKEN
}
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
DATE = today.strftime("%Y%m%d")

pixel_config = {
    "date" : DATE,
    "quantity" : "6.8",
}

#response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
#print(response.text)

update_endpoint = f"{pixel_endpoint}/{DATE}"

update_config = {
    "quantity": "11"
}

#response = requests.put(url=update_endpoint, json=update_config, headers=headers)
#print(response.text)

delete_endpoint = update_endpoint

response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)