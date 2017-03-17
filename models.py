# -*- coding:utf-8 -*- 
import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class UserList(User):
    user_rank_score = models.IntegerField(default=0)
    user_create_date = models.DateField(auto_now_add=True)
    user_profile = models.ImageField(
        default=os.path.join(settings.MEDIA_ROOT, 'images', 'generic_profile_photo.jpg'),
        upload_to='img',
        height_field=None,
        width_field=None,
        max_length=100,
        null=True)
    user_email = models.EmailField(null=True)
    user_class = models.IntegerField(blank=True)

    class Meta:
        ordering = ['user_create_date']

    def __unicode__(self):
        return self.username


class UrlPublish(models.Model):
    username_id = models.ForeignKey(UserList, editable=False, on_delete=models.CASCADE,verbose_name=u'用户名')
    urlmessage = models.URLField(verbose_name=u'url信息')
    urlintroduce = models.CharField(max_length=100,verbose_name=u'url介绍')
    urlpublish_time = models.DateTimeField(auto_now_add=True,verbose_name=u'发布时间')
    urlreadcount = models.IntegerField(default=0, verbose_name=u'阅读量')
    taglist = models.CharField(max_length=150,blank=True)
    class Meta:
        ordering = ['-urlpublish_time']

    def __unicode__(self):
        return u'url:%d:%s' % (self.id,self.urlintroduce)

class UrlComment(models.Model):
    comment1 = models.ForeignKey(UrlPublish, editable=False, on_delete=models.CASCADE)
    usernameid = models.ForeignKey(UserList, editable=False)
    comment_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=2000)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return u'%s %s %s' % (self.usernameid, self.comment_time, self.content)

class ArticlePublish(models.Model):
    usernameid = models.ForeignKey(UserList, editable=False,on_delete=models.CASCADE,verbose_name=u'用户')
    article = models.TextField()
    article_abstract = models.CharField(max_length=150)
    article_readcount= models.IntegerField(default=0,editable=False)
    publish_time = models.DateTimeField(auto_now_add=True)
    tag_list = models.CharField(max_length=150,blank=True)
    class Meta:
        ordering = ['-publish_time']

    def __unicode__(self):
        return u'article:%d:%s' %(self.id,self.publish_time)


class ArticleComment(models.Model):
    comment1 = models.ForeignKey(ArticlePublish, editable=False, on_delete=models.CASCADE)
    usernameid = models.ForeignKey(UserList, editable=False)
    comment_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=2000)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return u'%s %s %s' % (self.usernameid, self.comment_time, self.content)

class SuggestionSubmit(models.Model):
    name = models.CharField(max_length=15,default=u'匿名用户')
    content = models.TextField()

class TagList(models.Model):
    tagname = models.CharField(max_length=150,unique=True)

    class Meta:
        ordering = ['tagname']

    def __unicode__(self):
        return u'%s' %(self.tagname)