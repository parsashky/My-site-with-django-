from django.db.models.manager import BaseManager
from django.shortcuts import render,get_object_or_404
from blog.models import post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def blog_view(request,cat_name=None,author_username=None):
    posts = post.objects.filter(status=True)
    if cat_name:
        posts: BaseManager[post] = posts.filter(category__name=cat_name)
    if author_username:
        posts: BaseManager[post] = posts.filter(author__username = author_username)
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
       posts = posts.get_page(posts.num_pages)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    Post = get_object_or_404(post,id=pid,status=True)
    context = {'post':Post}
    return render(request,'blog/blog-single.html',context)
def test(request,pid):
    Post = get_object_or_404(post,id=pid)
    context = {'post':Post}
    return render(request,'test.html',context)
def blog_category(request,cat_name):
    posts = post.objects.filter(status=True)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_search(request):
    posts = post.objects.filter(status=True)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)