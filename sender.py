import requests

from src.configs.credentials import get_credentials

credentials = get_credentials()


def send_telegram_message(message: str):
    requests.post(
        f"https://api.telegram.org/bot{credentials['token']}/sendMessage",
        json={"chat_id": credentials["chat_id"], "text": message},
    )


send_telegram_message(
    "Lee, oh Lee, o que foi que eu fiz? Olha só para você, nem está consciente e continua se empenhando em mostrar para o mundo o que pode fazer."
)
