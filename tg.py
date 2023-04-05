import requests
from constants import TELEGRAM_TOKEN

def getUpdates():
  url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
  return requests.get(url).json()

def sendMessage(message, chat_id):
  url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
  return requests.get(url).json()
