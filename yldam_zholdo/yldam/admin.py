from django.contrib import admin

from yldam.models import *
class yldam_newsAdmin(admin.ModelAdmin):
    list_display = ('id','title','time_create','photo','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','content',)
# Register your models here.
admin.site.register(yldam_news,yldam_newsAdmin)
admin.site.register(Contact)