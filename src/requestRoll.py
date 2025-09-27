import requests
import sys
import os

from dotenv import load_dotenv

load_dotenv()


url_DNS = os.getenv("DNS")
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