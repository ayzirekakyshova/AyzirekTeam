from django.db import models
from django.contrib.auth import get_user_model

from main.models import Post

User = get_user_model()

class Comment(models.Model):
    author = models.ForeignKey(User,related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.author)       

class LikePost(models.Model):
    author = models.ForeignKey(User,related_name='post_likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='likes',on_delete=models.CASCADE)

class LikeComment(models.Model):
    author = models.ForeignKey(User, related_name='comment_likes', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='likes', on_delete=models.CASCADE)
