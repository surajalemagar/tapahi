from django.db import models

# Create your models here.
class OrderCodeNumber(models.Model):
    order_number = models.IntegerField(unique=True)
    code = models.IntegerField()
    def __str__(self):
        return "order" + str(self.order_number)

