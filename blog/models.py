#_*_coding:utf-8_*_
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey("Category")
    head_img = models.ImageField(upload_to="uploads")
    content = models.TextField()
    author = models.ForeignKey("UserProfile")
    publish_date = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField(default=True)
    priority = models.IntegerField(default=1000)

    def __unicode__(self):
        return "<%s, author:%s>" % (self.title, self.author)


class ThumbUp(models.Model):
    article = models.ForeignKey('Article')
    user = models.ForeignKey('UserProfile')
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "<user: %s>" %(self.user)

    class Meta:
        unique_together = ('user', 'article')        


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    groups = models.ManyToManyField('UserGroup')

    def __unicode__(self):
        return self.name


class Comments(models.Model):
    article = models.ForeignKey(Article)
    user = models.ForeignKey("UserProfile")
    parent_comment = models.ForeignKey('self', related_name='p_comment', blank=True, null=True)
    comment = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "<%s, user:%s>" % (self.comment, self.user)


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    admin = models.ForeignKey('UserProfile')

    def __unicode__(self):
        return self.name


class UserGroup(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name



