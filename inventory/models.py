from django.db import models


# Create your models here.

class Inventory(models.Model):
    type = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()
    choices = (
        ('AVAILABLE', 'Item ready to be purchase'),
        ('SOLD', 'Item sold'),
        ('RESTOCKING', 'Item restocking in few days'),
    )
    status = models.CharField(max_length=10, choices=choices, default='SOLD')
    issue = models.CharField(max_length=100, default='No issues')

    def __str__(self):
        return 'type : {0} price : {0}'.format(self.type, self.price)
