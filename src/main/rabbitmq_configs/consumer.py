import json

import pika

from src.configs.credentials import get_credentials

credentials = get_credentials()


class RabbitMQConsumer:
    def __init__(self) -> None:
        self.__host = credentials["host"]
        self.__port = credentials["port"]
        self.__username = credentials["username"]
        self.__password = credentials["password"]
        self.__queue = credentials["queue"]
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

        channel = pika.BlockingConnection(connection_parameters).channel()
        channel.queue_declare(
            queue=self.__queue,
            durable=True,
        )
        channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=self.rabbitmq_callback,
        )
        return channel

    def start(self):
        print("Sistema conectado ao RabbitMQ")
        self.__channel.start_consuming()

    def rabbitmq_callback(self, ch, method, properties, body):
        msg = body.decode("utf-8")
        msg_dict = json.loads(msg)
        print(msg_dict["message"])


rabbitmq_consumer = RabbitMQConsumer()
rabbitmq_consumer.start()
