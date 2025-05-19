from dotenv import load_dotenv
import os

load_dotenv()

credentials = {
    "host": os.getenv("HOST_RABBITMQ"),
    "port": int(os.getenv("PORT_RABBITMQ")),
    "username": os.getenv("USERNAME_RABBITMQ"),
    "password": os.getenv("PASSWORD_RABBITMQ"),
    "exchange": os.getenv("EXCHANGE_RABBITMQ"),
    "routing_key": os.getenv("ROUTING_KEY_RABBITMQ"),
}


def get_credentials():
    return credentials
