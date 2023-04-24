from django.shortcuts import render
from .models import News

# Create your views here.
def home_page(request):
    articles_list = News.objects.all()
    context = {
        'articles' : articles_list
    }
    return render(request, 'articles.html', context)