from django.shortcuts import render,get_object_or_404
from blog.models import post
# Create your views here.
def blog_view(request):
    posts = post.objects.filter(status=True)
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