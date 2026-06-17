from django.db.models.manager import BaseManager
from django.shortcuts import render,get_object_or_404
from blog.models import post,Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def blog_view(request,cat_name=None,author_username=None,tag_name=None):
    posts = post.objects.filter(status=True)
    if cat_name:
        posts: BaseManager[post] = posts.filter(category__name=cat_name)
    if author_username:
        posts: BaseManager[post] = posts.filter(author__username = author_username)
    if tag_name:
        posts: BaseManager[post] = posts.filter(tag__name=tag_name)

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
    comments = Comment.objects.filter(post=Post,approved=True).order_by('-created_date')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Comment.objects.create(post=Post,name=name,email=email,subject=subject,message=message)
    context = {'post':Post,'comments':comments}
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