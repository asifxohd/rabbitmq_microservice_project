import pika
import json


def saveComment(ch, method, properties, body):
    from .models import Comment  
    from .models import Posts
    message = json.loads(body)
    post_id = message.get('post_id')
    comment_content = message.get('comment')
    if post_id is not None and comment_content is not None:
        inst = Posts.objects.filter(id=post_id).first()
        if inst is not None:
            ob = Comment.objects.create(post=inst, comment=comment_content)
            ob.save()
            print("Comment saved successfully")
        else:
            print(f"Message with post_id {post_id} does not exist")
    else:
        print("post_id or comment content is null. Cannot save Comment.")
    
def consume_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='comment_queue_2')  
    channel.exchange_declare(exchange='posts_and_back', exchange_type='fanout')
    channel.basic_consume(queue='comment_queue_2', on_message_callback=saveComment, auto_ack=True) 
    print('Waiting for messages. To exit, press CTRL+C')
    channel.start_consuming()
