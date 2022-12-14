from django.db import models
from django.urls import reverse

# Create your models here.
class StaticPosts(models.Model):
    title = models.CharField(max_length=160)
    page_name = models.CharField(max_length=70)
    content = models.TextField()
    slug = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.title


# Create your models here.
class FooterData(models.Model):
    email = models.CharField(max_length=160, default="")
    phone =models.IntegerField(default=123456789)
    facebook = models.CharField(max_length=160,  default="", blank=True, null=True)
    instagram = models.CharField(max_length=160,  default="", blank=True, null=True)
    twitter = models.CharField(max_length=160,default="", blank=True, null=True)
    youtube = models.CharField(max_length=160,default="", blank=True, null=True)
    address = models.CharField(max_length=260,default="")
    made_by = models.CharField(max_length=160,default="")
    copyright = models.CharField(max_length=160,default="")
