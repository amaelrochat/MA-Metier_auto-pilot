import requests
import time
import math

# --- CONFIGURATION ---
URL_API = "http://10.229.41.253/api/aircraft"
CAP_VOULU_DEG = 90.0 
KP = 0.005 

def calculer_correction(cap_actuel_deg):
    erreur = CAP_VOULU_DEG - cap_actuel_deg
    
    # Correction du passage 360/0
    if erreur > 180: erreur -= 360
    if erreur < -180: erreur += 360
    
    commande = erreur * KP
    
    commande = max(min(commande, 0.2), -0.2)
    
    return commande, erreur

print("Autopilote")

while True:
    try:
        
        response = requests.get(URL_API, timeout=1)
        data = response.json()
  
        raw_heading = data.get('heading', 0)
        cap_deg = math.degrees(raw_heading) 
        
     
        action, erreur_cap = calculer_correction(cap_deg)
        
        requests.post(URL_API, json={"aileron_position": action})
        
        print(f"Cap: {cap_deg:.1f}° | Erreur: {erreur_cap:.1f}° | Commande: {action:.3f}")

    except Exception as e:
        print(f"Erreur : {e}")

    time.sleep(0.1)