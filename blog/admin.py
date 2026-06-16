from django.contrib import admin
from blog.models import post, Category
from django_summernote.admin import SummernoteModelAdmin  # این را تغییر دادیم

# ثبت مدل Category به صورت ساده
admin.site.register(Category)

# تعریف کلاس ادمین برای پست
class PostAdmin(SummernoteModelAdmin): # از SummernoteModelAdmin استفاده کنید
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_views', 'status', 'published_date', 'created_date')
    list_filter = ('status', 'author')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

# ثبت مدل post با تنظیمات PostAdmin
admin.site.register(post, PostAdmin)
