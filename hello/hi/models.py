from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Post(models.Model):
    title = models.CharField(max_length=40, null=False)
    content = models.TextField(blank=True, default=':)')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    followers_count = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999999)], default=0)
    post_count = models.IntegerField(default=0)

    def __str__(self):
        return f'profile is created for user {self.user}'


class Follow(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'following')

    def __str__(self):
        return f"{self.user.username} follows {self.following.username}"