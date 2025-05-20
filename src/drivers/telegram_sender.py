import requests

from src.configs.credentials import get_credentials

credentials = get_credentials()


def send_telegram_message(message: str) -> None:
    requests.post(
        f"https://api.telegram.org/bot{credentials['token']}/sendMessage",
        json={"chat_id": credentials["chat_id"], "text": message},
    )
