from django.db import models

class Message(models.Model):
    uuid = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"{self.uuid}: {self.content}"


class Comment(models.Model):
    post = models.ForeignKey(Message, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Comment on {self.post.uuid}: {self.content}"