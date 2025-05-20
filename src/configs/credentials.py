import os

from dotenv import load_dotenv

load_dotenv()

credentials = {
    "host": os.getenv("HOST_RABBITMQ"),
    "port": int(os.getenv("PORT_RABBITMQ")),
    "username": os.getenv("USERNAME_RABBITMQ"),
    "password": os.getenv("PASSWORD_RABBITMQ"),
    "exchange": os.getenv("EXCHANGE_RABBITMQ"),
    "routing_key": os.getenv("ROUTING_KEY_RABBITMQ"),
    "queue": os.getenv("QUEUE_RABBITMQ"),
    "token": os.getenv("TOKEN_TELEGRAM"),
    "chat_id": os.getenv("CHAT_ID_TELEGRAM"),
}


def get_credentials():
    return credentials
