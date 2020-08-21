from django.db import models
import datetime
# Create your models here.

class WritePosts(models.Model):
    writeContent = models.TextField(max_length=10000)
    writeTimestamp = models.DateTimeField(auto_now=True)
    #writeAuthor = models.CharField(max_length=255, default="anonymous")
    contributer = models.ForeignKey(
        "myuser.User", on_delete=models.CASCADE, related_name="writer", blank=False, null=True)

    class Meta:
        ordering=['writeTimestamp']


class ClickPosts(models.Model):
    clickImage = models.ImageField(upload_to='media/images/ClickImages')
    clickContent = models.TextField(max_length=10000)
    clickTimestamp = models.DateTimeField(auto_now=True)
    #clickAuthor = models.CharField(max_length=255, default="anonymous")
    contributer = models.ForeignKey(
        "myuser.User", on_delete=models.CASCADE, related_name="photographer", blank=False, null=True)

    class Meta:
        ordering=['clickTimestamp']

class ArtPosts(models.Model):
    artImage = models.ImageField(upload_to='media/images/ArtImages')
    artContent = models.TextField(max_length=10000)
    artTimestamp = models.DateTimeField(auto_now=True)
    #artAuthor = models.CharField(max_length=255, default="anonymous")
    contributer = models.ForeignKey(
        "myuser.User", on_delete=models.CASCADE, related_name="artist", blank=False, null=True)

    class Meta:
        ordering=['artTimestamp']

