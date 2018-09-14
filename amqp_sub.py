import pika


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


if __name__ == '__main__':
    parameters = pika.URLParameters('amqp://guest:guest@maragi-rabbit:5672/%2F')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.exchange_declare(exchange='sensor_audio', exchange_type='fanout')
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange='sensor_audio', queue=queue_name)
    print(' [*] Waiting for logs. To exit press CTRL+C')
    channel.basic_consume(callback, queue=queue_name, no_ack=True)
    channel.start_consuming()
