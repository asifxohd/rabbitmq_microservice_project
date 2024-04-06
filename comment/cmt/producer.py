import pika
import json
    
def publish_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='posts_and_back', exchange_type='fanout')
    channel.queue_declare(queue='comment_queue')
    channel.queue_declare(queue='comment_queue_2')
    channel.queue_bind(exchange='posts_and_back', queue='comment_queue')
    channel.queue_bind(exchange='posts_and_back', queue='comment_queue_2')
    message_json = json.dumps(message)
    channel.basic_publish(exchange='posts_and_back', routing_key='', body=message_json)
    connection.close()
