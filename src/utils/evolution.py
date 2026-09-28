import requests

class EvolutionAPI:
    def __init__ (self):
        self
    def enviar_mensagem(self, instance, apikey, sender_number, message):
        url = f"http://localhost:8080/message/sendText/{instance}"
        payload = {
            "number": sender_number,
            "text": message,
            "delay": 2000
        }
        headers = {
            "apikey": apikey,
            "Content-Type": "application/json"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        return response
        
    

        
