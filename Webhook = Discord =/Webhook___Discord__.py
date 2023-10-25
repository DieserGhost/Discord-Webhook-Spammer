import requests
import json
import time

creditstool = "Tool made by Ghost143 Team"

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    print(creditstool)
    
webhook_url = config['webhook_url']
webhook_name = config['webhook_name']
nachricht = config['nachricht']

while True:
    payload = {
        'content': nachricht,
        'username': webhook_name  
    }

    response = requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

    if response.status_code == 204:
        print(f"Nachricht erfolgreich an {webhook_name} gesendet.")
    else:
        print(f"Fehler beim Senden der Nachricht an {webhook_name}. Statuscode: {response.status_code}")
        print(response.text)

    time.sleep(0)