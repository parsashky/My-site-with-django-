from django import template
from blog.models import post


register = template.Library()

@register.inclusion_tag("blog/latest-post.html")
def latestpost():
    posts = post.objects.filter(status=True).order_by('published_date')[:3]