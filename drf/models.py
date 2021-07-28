from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=CASCADE)

    def __str__(self):
        return self.title