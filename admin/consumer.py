import pika


from wishlists.serializers import WishlistsSerializer

params = pika.URLParameters('amqps://jhcbtqpw:x66trdbJZ8BU3nXEICqY2MrDdZBjkhxp@cow.rmq2.cloudamqp.com/jhcbtqpw')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    # if properties.content_type == 'book_to_wishlist':
    serializer = WishlistsSerializer(data=body)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    print('Book is added to wishlist!')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
