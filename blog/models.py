from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class post(models.Model):
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category) 
    # tag 
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.title
    def snippets(self, length=100):
        if len(self.content) > length:
            return self.content[:length] + '...'
        else:
            return self.content
    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid': self.id})
