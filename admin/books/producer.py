import pika, json

params = pika.URLParameters('amqps://jhcbtqpw:x66trdbJZ8BU3nXEICqY2MrDdZBjkhxp@cow.rmq2.cloudamqp.com/jhcbtqpw')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
