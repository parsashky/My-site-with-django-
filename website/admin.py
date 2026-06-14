from django.contrib import admin
from website.models import contact , newsletter
# Register your models here.
class contactadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','created_date')
    list_filter = ('email',)
    search_fields = ('name','message')
admin.site.register(contact,contactadmin)
admin.site.register(newsletter)