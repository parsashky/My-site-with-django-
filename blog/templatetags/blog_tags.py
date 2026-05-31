from django import template
from blog.models import post


register = template.library()

@register.inclusion_tag("blog/latestpost.html")
def latestpost():
    posts = post.objects.filter(status=True).order_by('published_date')[:3]