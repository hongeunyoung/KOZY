from django.db import models
from accounts.models import User

class Todo(models.Model):
    # user = models.ForeignKey(
    #     User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    user_id = models.TextField()

    def __str__(self):
        return self.title