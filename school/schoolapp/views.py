from django.shortcuts import render
from .models import News, Photo
from django.core.paginator import Paginator
from django.views.generic import ListView


class Index(ListView):
    queryset = News.objects.all().order_by('-date')[:5]
    template_name = 'schoolapp/index.html'
    context_object_name = 'news'


class NewsView(ListView):
    paginate_by = 5
    queryset = News.objects.all().order_by('-date')
    template_name = 'schoolapp/news.html'
    context_object_name = 'news'

    def get(self, request):
        order_field = request.GET.get('order_field')
        if order_field:
            self.queryest = self.queryset.order_by('date')
            print(self.queryset)
        return super().get(request)



class PhotoView(ListView):
    queryset = Photo.objects.all().order_by('-date')
    template_name = 'schoolapp/photo_album.html'
    context_object_name = 'photos'
