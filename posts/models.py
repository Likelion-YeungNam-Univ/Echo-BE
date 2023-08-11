from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile
from utils.models import TimestampZone

# Create your models here.


class Post(TimestampZone):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    body = models.TextField()
    #image = models.ImageField(upload_to='post/', default='default.png')
    likes = models.ManyToManyField(User, related_name='like_posts', blank=True)
    tag = models.CharField(max_length=150, default = '')

    class Meta:
        db_table = "posts"


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post/%Y/%m/%d")


class Comment(TimestampZone):
    comment = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)


    class Meta:
        db_table = "comments"


class ReComment(TimestampZone):
    recomment = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='recomments', on_delete=models.CASCADE, default = '')

    class Meta:
        db_table = "recomments"





