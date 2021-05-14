import pika, json,os,django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

# from wishlists.models import Wishlists
from wishlists.serializers import WishlistsSerializer

params = pika.URLParameters('amqps://jhcbtqpw:x66trdbJZ8BU3nXEICqY2MrDdZBjkhxp@cow.rmq2.cloudamqp.com/jhcbtqpw')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    data = json.loads(body)
    print(data)
    if data:
        print(json.dumps(data))
        serializer = WishlistsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    print('Book is added to wishlist!')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
