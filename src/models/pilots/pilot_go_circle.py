import requests

url = "http://10.229.41.253/api/aircraft"

datas = {
  "aileron_position": 0.3,
  "elevator_position": 0.06,
  "rudder_position": 0.0
}


while True:
    response = requests.post(url, json=datas)

    if response.status_code != 200:
        print(f"Erreur : {response.status_code}")
        break