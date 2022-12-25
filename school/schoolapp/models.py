from django.db import models
from PIL import Image, ImageDraw
from datetime import datetime


# Create your models here.
class News(models.Model):
    title = models.TextField(max_length=70)
    description = models.TextField(max_length=2000)
    img = models.ImageField(upload_to='news/')
    date = models.DateField()

    def __str__(self):
        return f' {self.title}'


class Photo(models.Model):
    title = models.TextField(max_length=70)
    img = models.ImageField(upload_to='photo/')
    date = models.DateField()

    def __str__(self):
        return f' {self.title}'
