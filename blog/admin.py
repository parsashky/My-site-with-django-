from django.contrib import admin
from blog.models import post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class postadmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','author','counted_views','status','published_date','created_date')
    list_filter = ('status','author')
    #ordering = ['published_date']
    search_fields = ['title','content']
    summernote_fields = ('content',)
class Commentadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name','post','email','subject','approved','created_date')
    list_filter = ('approved',)
    search_fields = ['name','email','subject','message']

admin.site.register(Comment,Commentadmin)
admin.site.register(post,postadmin)
admin.site.register(Category)