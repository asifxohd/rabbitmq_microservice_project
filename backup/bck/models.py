from django.db import models

class Message(models.Model):
    uuid = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"{self.uuid}: {self.content}"
