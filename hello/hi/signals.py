from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Post)
def increment_post_count(sender, instance, created, **kwargs):
    if created:
        print(f"New post created by {instance.author.username}")

        profile = instance.author.profile
        profile.post_count += 1
        profile.save()

@receiver(post_delete, sender=Post)
def decrement_post_count(sender, instance, **kwargs):
    print(f"Post deleted: {instance.title}")

    profile = instance.author.profile
    
    if profile.post_count > 0:
        profile.post_count -= 1
        profile.save()


@receiver(post_save, sender=Follow)
def increment_followers_count(sender, instance, created, **kwargs):
    if created:
        profile = instance.following.profile 
        profile.followers_count += 1
        profile.save()

@receiver(post_delete, sender=Follow)
def decrement_followers_count(sender, instance, **kwargs):
    profile = instance.following.profile
    if profile.followers_count > 0:
        profile.followers_count -= 1
        profile.save()
