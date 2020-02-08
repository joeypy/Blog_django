from django.contrib import admin
from blog.models import Post

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'updated', 'created',)
    list_filter = ('title',)
    search_fields = ('title',)
    ordering = ['-created']


admin.site.register(Post, BlogAdmin)