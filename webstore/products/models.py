from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=155)
    price = models.FloatField()
    image_url = models.CharField(max_length=3000)