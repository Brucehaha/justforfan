import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='hello', durable=True) # durable keep the queue over there but information is gone, need delivery_mode in publish in producer


print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print("-->", ch, method, properties)
    print(" [x] %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(callback,
                      queue='hello', # if get the news then Call Callback to handle information
                      # no_ack=True
                      )


channel.start_consuming()
