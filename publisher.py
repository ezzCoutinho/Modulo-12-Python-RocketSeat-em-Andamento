import json

import pika
from dotenv import load_dotenv

from src.configs.credentials import get_credentials

load_dotenv()

credentials = get_credentials()


class RabbitMQPublisher:
    def __init__(self) -> None:
        self.__host = credentials["host"]
        self.__port = credentials["port"]
        self.__username = credentials["username"]
        self.__password = credentials["password"]
        self.__exchange = credentials["exchange"]
        self.__routing_key = credentials["routing_key"]
        self.__channel = self.create_channel()

    def create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password,
            ),
        )
        connection = pika.BlockingConnection(connection_parameters)
        channel = connection.channel()
        print(f"Channel created: {channel}")
        return channel


rabbitmq_publisher = RabbitMQPublisher()
