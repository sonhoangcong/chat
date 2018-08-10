from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group_name = models.TextField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
