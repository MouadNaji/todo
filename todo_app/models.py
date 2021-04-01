from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Todo(models.Model):
    text=models.CharField(max_length=350)
    status=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
      return f"{self.text} - {self.status}"







