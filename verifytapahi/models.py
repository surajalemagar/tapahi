from django.db import models

# Create your models here.
class Post(models.Model):
    order_number = models.CharField(max_length=200)
    code = models.PositiveIntegerField()