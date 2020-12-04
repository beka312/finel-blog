from django.contrib import admin
from .models import Post, PostImage, Category, Comment, Admin
from main.models import User


class ImageInLine(admin.TabularInline):
    model = PostImage
    extra = 2
    fields = ('image', )

class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImageInLine,
    ]

    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Admin)

