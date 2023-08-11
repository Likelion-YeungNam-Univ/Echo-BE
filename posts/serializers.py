from rest_framework import serializers
from .models import Post, Comment, ReComment, PostImage
from users.models import Profile
from users.serializers import ProfileSerializer
from django.contrib.auth.models import User

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ("image")

class ReCommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = ReComment
        fields = ("pk", "recomment", "profile", "created_at")

class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    recomments = ReCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ("pk", "comment", "profile", "created_at", "recomments")

class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    images = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("pk", "profile", "body", "likes", "created_at", "updated_at", "comments", "images", "tag")

class ReCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReComment
        fields = ("recomment",)

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("comment",)


class PostCreateSerializer(serializers.ModelSerializer):
    image = serializers.ListField(child=serializers.ImageField(), required=False)
    class Meta:
        model = Post
        fields = ("body", "image" )








