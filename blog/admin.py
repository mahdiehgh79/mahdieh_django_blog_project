from django.contrib import admin
from .models import Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','statues','datetime_modified',)
    ordering = ('-statues',)



admin.site.register(Post, PostAdmin)
