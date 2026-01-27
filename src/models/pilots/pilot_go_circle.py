import requests
import time

url = "http://10.229.41.253/api/aircraft"


def maintain_angle(angle_to_maintain):
    current_state = requests.get(url).json()
    current_angle = current_state['plane_angle']

    angle_difference = angle_to_maintain - current_angle
    aileron_adjustment = angle_difference * 0.5

    aileron_adjustment = max(-1.0, min(1.0, aileron_adjustment))

    requests.post(url, json={
          "aileron_position": aileron_adjustment,
         "elevator_position": 0.06
    })

while True:
     plane_state = requests.get(url).json()
     print(
         f"Angle: {plane_state['plane_angle']} | "
         f"Heading: {plane_state['heading']} | "
         f"Altitude: {plane_state['altitude']} | "
        f"Aileron: {plane_state['aileron_position']}"
    )

     maintain_angle(0.5)
     time.sleep(0.05)
