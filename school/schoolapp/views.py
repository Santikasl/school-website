from django.shortcuts import render
from .models import News, Photo
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView


class Index(ListView):
    queryset = News.objects.all().order_by('-date')[:5]
    template_name = 'schoolapp/index.html'
    context_object_name = 'news'


class OneNews(DetailView):
    model = News
    context_object_name = 'news'
    template_name = 'schoolapp/one_news.html'

    def get_object(self):
        object = super(OneNews, self).get_object()
        print(object.pk)
        return object



class NewsView(ListView):
    paginate_by = 5
    queryset = News.objects.all()
    template_name = 'schoolapp/news.html'
    context_object_name = 'news'

    def get_queryset(self):
        order_field = self.request.GET.get('order_field')
        order = ''
        if order_field == 'Новые':
            order = '-date'
        elif order_field == 'Старые':
            order = 'date'
        query = self.request.GET.get('search')
        if order_field:
            self.queryset = self.queryset.order_by(order)
            return self.queryset
        elif query:

            object_list = News.objects.filter(title__iregex=query)
            return object_list
        else:
            return self.queryset

    def get(self, request):
        super().get(request)
        order_field = self.request.GET.get('order_field')
        if order_field:
            context = self.get_context_data()
            context['order_field'] = order_field
            return self.render_to_response(context)
        else:
            context = self.get_context_data()
            context['order_field'] = "#"
            return self.render_to_response(context)


class PhotoView(ListView):
    queryset = Photo.objects.all().order_by('-date')
    template_name = 'schoolapp/photo_album.html'
    context_object_name = 'photos'
