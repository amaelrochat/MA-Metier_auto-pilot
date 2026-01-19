import requests

url = "https://api.exemple.com/data"

response = requests.get(url)


if response.status_code == 200:
    print("Successful request")
    data = response.json()
    print(data)
else:
    print(f"Error : {response.status_code}")



