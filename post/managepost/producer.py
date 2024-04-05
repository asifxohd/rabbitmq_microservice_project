import pika
import json

def publish_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='pass')
    message_json = json.dumps(message)
    channel.basic_publish(exchange='',routing_key='pass',body=message_json)
    connection.close()
