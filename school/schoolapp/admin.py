from django.contrib import admin

# Register your models here.
from .models import News, Photo

admin.site.register(News)
admin.site.register(Photo)
