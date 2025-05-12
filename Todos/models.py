from django.db import models
import datetime
from User.models import UserModel

class TodoModel(models.Model):
    work =  models.TextField()
    deadline = models.DateTimeField(default=datetime.datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    is_finished = models.BooleanField(default=False)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)


    class Meta:
        db_table = 'todos'
        verbose_name = 'Todo'
        verbose_name_plural = 'Todolar'

    def __str__(self):
        return self.work