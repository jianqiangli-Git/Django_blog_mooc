from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    articles = models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles})

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request,'blog/edit_page.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request,'blog/edit_page.html',{'article':article})

def action_page(request):
    modefy = request.POST.get('modefy',"MODEFY")
    title = request.POST.get('article_title','ARTICLE_TITLE')
    content = request.POST.get('article_content','ARTICLE_CONTENT')
    if str(modefy) == '0':
        article = models.Article.objects.create(title=title, content=content)
    else:
        article = models.Article.objects.get(pk=modefy)
        article.title = title
        article.content = content
        article.save()
    articles = models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles})

