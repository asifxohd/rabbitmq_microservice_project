import pika
import json

def callback(ch, method, properties, body):
    from .models import Message  
    message = json.loads(body)
    uuid = message.get('uuid')
    content = message.get('content')
    message_obj = Message.objects.create(uuid=uuid, content=content)
    message_obj.save()
    print("Message saved successfully")
    
def saveComment(ch, method, properties, body):
    from .models import Comment  
    from .models import Message
    message = json.loads(body)
    post_id = message.get('post_id')
    comment_content = message.get('comment')
    if post_id is not None and comment_content is not None:
        inst = Message.objects.filter(uuid=post_id).first()
        if inst is not None:
            ob = Comment.objects.create(post=inst, content=comment_content)
            ob.save()
            print("Comment saved successfully")
        else:
            print(f"Message with post_id {post_id} does not exist")
    else:
        print("post_id or comment content is null. Cannot save Comment.")
    

def consume_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='pass')
    channel.basic_consume(queue='pass', on_message_callback=callback, auto_ack=True)
    channel.exchange_declare(exchange='posts_and_back', exchange_type='fanout')
    channel.queue_declare(queue='comment_queue')
    channel.basic_consume(queue='comment_queue', on_message_callback=saveComment, auto_ack=True)
    print('Waiting for messages. To exit, press CTRL+C !!!!!!!!!')
    channel.start_consuming()
