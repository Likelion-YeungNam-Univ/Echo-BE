from django.contrib import admin
from .models import Post, Comment, ReComment, PostImage

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ReComment)
admin.site.register(PostImage)