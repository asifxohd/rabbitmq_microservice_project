import pika
import json
from bck.models import Message

def callback(ch, method, properties, body):
    message = json.loads(body)
    uuid = message.get('uuid')
    content = message.get('content')
    message_obj = Message.objects.create(uuid=uuid, content=content)
    message_obj.save()
    
    print("save aaayin mwonnoseeee")

def consume_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='pass')
    channel.basic_consume(queue='pass', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
