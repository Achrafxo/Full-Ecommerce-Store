from django.db import models


class Product(models.Model):
    
    choices = (
        ('Indoor', 'Indoor'),
        ('Out door', 'Out door')
    )

    name = models.CharField(max_length=120, null=True)
    price = models.FloatField(null=True)
    description = models.TextField(max_length=1500, null=True)
    #picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    category = models.CharField(max_length=20, choices=choices)
    brand = models.CharField(max_length=20, null=True)
    color = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
