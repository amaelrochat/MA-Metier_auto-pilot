import requests

url = "http://10.229.41.253/api/aircraft"

response = requests.get(url)


if response.status_code == 200:
    print("Successful request")
    data = response.json()
    print(data)
else:
    print(f"Error : {response.status_code}")
