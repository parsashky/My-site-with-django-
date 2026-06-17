from django import template
from blog.models import Comment, post
from blog.models import Category


register = template.Library()

@register.inclusion_tag("blog/latest-post.html")
def latestpost():
    posts = post.objects.filter(status=True).order_by('published_date')[:3]

@register.simple_tag(name ="comments_count")
def function(pid):
     return Comment.objects.filter(post_id=pid, approved=True).count()

@register.inclusion_tag("blog/post-category.html")
def postcategories():
    posts = post.objects.filter(status=True)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category = name).count()
    return {'categories' : cat_dict}