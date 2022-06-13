from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Article

# Create your views here.

def index(request):
    article = Article.objects.all()
    context = {'article': article}
    return render(request, 'base.html', context)


def detail(request, article_id):
    article = Article.objects.get(id = article_id)
    context = {'article': article}
    return render(request, 'detail.html', context)

def add_articles(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        article = Article(title=title, content=content)
        article.save()
        return redirect('/')
    return render(request, 'form.html')
    