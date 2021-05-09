import pika, json

from main import Book, db

params = pika.URLParameters('amqps://jhcbtqpw:x66trdbJZ8BU3nXEICqY2MrDdZBjkhxp@cow.rmq2.cloudamqp.com/jhcbtqpw')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)

    if properties.content_type == 'book_created':
        book = Book(id=data['id'], title=data['title'], image=data['image'], isbn=data['isbn'], auth=data['author'], publisher=data['publisher'], status=data['status'])
        db.session.add(book)
        db.session.commit()
        print('Book Created')

    elif properties.content_type == 'book_updated':
        book = Book.query.get(data['id'])
        book.title = data['title']
        book.image = data['image']
        book.isbn = data['isbn']
        book.auth = data['auth']
        book.publisher = data['publisher']
        book.status = data['status']
        db.session.commit()
        print('Book Updated')

    elif properties.content_type == 'book_deleted':
        book = Book.query.get(data)
        print(book)
        db.session.delete(book)
        db.session.commit()


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
