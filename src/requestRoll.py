import requests
import sys

url_DNS = "https://f307e5b0-69d8-4621-b2ec-3395aedfe928-00-3pw0ady9xg5l1.picard.replit.dev"
url_endPoint = "diceResult/"

def rollDice(characterName : str, nbDice : int, limit : int, bonus : int, type : str):
    url = f"{url_DNS}/{url_endPoint}"

    objectParameter = {
        "nom" : characterName,
        "roll" : {
            "number": nbDice,
            "dice": limit,
            "bonus": bonus,
            "type": type
        }
    }

    try:
        resultRoll = requests.post(url, json = objectParameter)
        return resultRoll.json()
    except Exception as e:
        print("Erreur lors du lancer de dé:", e, file=sys.stderr)
        return None