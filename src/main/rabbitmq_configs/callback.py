import json

from src.drivers.telegram_sender import send_telegram_message


def rabbitmq_callback(ch, method, properties, body):
    msg = body.decode("utf-8")
    msg_dict = json.loads(msg)
    send_telegram_message(msg_dict["message"])
