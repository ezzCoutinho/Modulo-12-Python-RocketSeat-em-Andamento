## 17/05


Hoje estudamos o RabbitMQ, que é um sistema de mensageria que funciona de maneira diferente das requisições HTTP tradicionais. Enquanto em uma requisição HTTP precisamos esperar uma resposta imediata, o RabbitMQ permite:

- Enviar mensagens de forma assíncrona
- Processar múltiplas respostas simultaneamente
- Não precisar esperar por uma resposta imediata
- Melhor escalabilidade para sistemas distribuídos


## 18/05 


Hoje aprendemos sobre a routingKey em filas do RabbitMQ. Quando uma routingKey é definida para uma fila específica, se uma mensagem for enviada sem essa routingKey, ela não será entregue à fila correspondente. Além disso, mesmo que uma mensagem com uma routingKey compatível seja enviada, ela não será entregue se não houver uma correspondência exata.
Isso se aplica a filas do tipo direct. Por outro lado, se a fila for do tipo fanout, a mensagem será enviada independentemente da routingKey.
O RabbitMQ também possui argumentos que podem ser configurados nas filas, como:
x-max-length: Define o número máximo de mensagens que a fila pode armazenar. Quando esse limite é atingido, as mensagens mais antigas são descartadas.
x-max-length-bytes: Define o tamanho máximo em bytes que a fila pode ocupar. Assim como o x-max-length, quando o limite é atingido, as mensagens mais antigas são descartadas.
x-message-ttl: Define o tempo de vida (TTL) das mensagens na fila. Após esse tempo, as mensagens são descartadas.
x-expires: Define o tempo de expiração da fila. Se a fila não for utilizada por um determinado período, ela será automaticamente excluída.
x-dead-letter-exchange: Especifica uma exchange para onde as mensagens que não puderem ser entregues (por exemplo, devido a um erro de roteamento) serão enviadas.
x-dead-letter-routing-key: Define a routing key para as mensagens que são enviadas para a exchange de dead-letter.


## 19/05


Hoje finalizamos o módulo sobre RabbitMQ. Implementamos o RabbitMQ e iniciamos o sistema através do arquivo run.py em Python. Também adicionamos a classe RabbitMQConsumer, que é responsável por decodificar as mensagens de bytes para strings, utilizando a biblioteca json para convertê-las em dicionários.
Além disso, incluímos novas bibliotecas em nosso módulo, como requests, que nos permite fazer requisições HTTP. Criamos o arquivo sender.py, onde realizamos testes de envio de mensagens diretas utilizando nosso bot do Telegram.
Por fim, concluímos o módulo interligando o RabbitMQ, com a implementação do consumidor e o callback do publicador.