import uuid
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .producer import publish_message


class Posts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    

class Comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE , related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return f"Comment on {self.post.uuid}: {self.content}"
    
@receiver(post_save, sender=Posts)
def post_save_handler(sender, instance, created, **kwargs):
    if created:
        print("Post saved successfully")
        message = {'content': instance.content, 'uuid': str(instance.id)}
        publish_message(message)