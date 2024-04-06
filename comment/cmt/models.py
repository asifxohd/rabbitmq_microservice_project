from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .producer import publish_message

class Comment(models.Model):
    post_id = models.CharField(max_length=255)
    content = models.TextField()

@receiver(post_save, sender=Comment)
def post_save_handler(sender, instance, created, **kwargs):
    if created:
        message = {'comment': instance.content, 'post_id': str(instance.post_id)}
        print(message)
        publish_message(message)
        print("Published saved successfully")
