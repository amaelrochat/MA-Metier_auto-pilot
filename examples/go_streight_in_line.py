import requests
import time
import math

URL_API = "http://10.229.41.253/api/aircraft"
CAP_VOULU_DEG = 90.0 

# Gains PID ajustés
KP = 0.015  
KI = 0.0005   
KD = 0.01     
erreur_precedente = 0
somme_erreurs = 0

def calculer_correction_pid(cap_actuel_deg):
    global erreur_precedente, somme_erreurs
    
    erreur = CAP_VOULU_DEG - cap_actuel_deg
    if erreur > 180: erreur -= 360
    if erreur < -180: erreur += 360

    P = KP * erreur
    
    somme_erreurs += erreur
    somme_erreurs = max(min(somme_erreurs, 20), -20)
    I = KI * somme_erreurs
    
    variation = erreur - erreur_precedente
    D = KD * variation
    

    commande = P + I + D

    commande = max(min(commande, 0.25), -0.25)
    
    erreur_precedente = erreur
    return commande, erreur

print(f"Auto-pilote activé. Cible : {CAP_VOULU_DEG}°")

while True:
    try:
        start_time = time.time()
        
        response = requests.get(URL_API, timeout=0.5)
        data = response.json()
  
        raw_heading = data.get('heading', 0)
        cap_deg = math.degrees(raw_heading) 
        
        action, erreur_cap = calculer_correction_pid(cap_deg)
        requests.post(URL_API, json={"aileron_position": action}, timeout=0.5)       
        
        print(f"Cap: {cap_deg:5.1f}° | Erreur: {erreur_cap:5.1f}° | Aileron: {action:6.3f}")
        
    except Exception as e:
        print(f"Erreur de connexion : {e}")

    
    elapsed = time.time() - start_time
    time.sleep(max(0.01, 0.1 - elapsed))