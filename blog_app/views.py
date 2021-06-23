import json
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def about_page(request):

    return render(request, 'about.html', locals())

def post_page(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'post_page/index.html', locals())

def dashboard_page(request):
    if 'id' in request.session:
        tags = Tag.objects.all()
        return render(request, 'admin_page/index.html', locals())

    return redirect('/blog/login_page')


def login_page(request):
    if 'id' in request.session:
        return redirect('/blog/dashboard')
    return render(request, 'admin_page/login.html', locals())



def login(request):
    if request.method == 'POST':
        print(request.POST['id'])
        if 'id' in request.POST:
            account_id = request.POST['id']
            print(account_id)
            if account_id:
                request.session['id'] = account_id
                return redirect('/blog/dashboard')
    return redirect('/blog/login_page')

def post(request):
    if request.method == 'POST':
        title = request.POST['title']
        tag = None
        if 'tag' in request.POST:
            tag = Tag.objects.get(name=request.POST['tag'])
            if not tag:
                tag  = Tag.objects.create(name=tag)
        content = request.POST['content']
        print(tag)
        post = Post.objects.create(title=title, tag=tag, content=content)
    return redirect('/blog/dashboard')
