# -*- coding:utf-8 -*- 
import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserList(User):
    user_rank_score = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now())
    user_introduce = models.CharField(max_length=200,default=u'暂无介绍')
    user_profile = models.CharField(max_length=1000,null=True)
    user_email = models.EmailField(null=True)
    user_class = models.IntegerField(null=True,blank=True)
    class Meta:
        ordering = ['created']

    def __unicode__(self):
        return self.username

class FollowRelation(models.Model):
    followerid = models.ForeignKey(UserList,editable=False,on_delete=models.CASCADE,related_name='follower')
    followedid = models.ForeignKey(UserList,editable=False,on_delete=models.CASCADE,related_name='followed')
    created = models.DateTimeField(auto_now_add=True,blank=True)

class Group(models.Model):
    groupownerid = models.ForeignKey(UserList,max_length=50,editable=False,on_delete=models.CASCADE)
    groupname = models.CharField(max_length=50,unique=True)
    groupintroduce = models.TextField(default=u'暂无介绍')
    created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.groupname

class GroupMember(models.Model):
    groupid = models.ForeignKey(Group,editable=False,on_delete=models.CASCADE) 
    memberid = models.ForeignKey(UserList,editable=False,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s,%s' % (self.memberid,self.member_username)

class UrlPublish(models.Model):
    usernameid = models.ForeignKey(UserList, editable=False, on_delete=models.CASCADE,verbose_name=u'用户名')
    urlmessage = models.URLField(verbose_name=u'url信息')
    urlintroduce = models.CharField(max_length=100,verbose_name=u'url介绍')
    created = models.DateTimeField(auto_now_add=True,verbose_name=u'发布时间')
    urlreadcount = models.IntegerField(default=0, verbose_name=u'阅读量')
    taglist = models.CharField(max_length=150,blank=True)
    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s, %s' % (self.usernameid,self.urlintroduce)

class UrlComment(models.Model):
    comment1 = models.ForeignKey(UrlPublish, editable=False, on_delete=models.CASCADE)
    usernameid = models.ForeignKey(UserList, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=2000)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return u'%s %s %s' % (self.usernameid, self.created, self.content)

class ArticlePublish(models.Model):
    usernameid = models.ForeignKey(UserList, editable=False,on_delete=models.CASCADE,verbose_name=u'用户')
    article = models.TextField()
    article_abstract = models.CharField(max_length=150)
    article_readcount= models.IntegerField(default=0,editable=False)
    created = models.DateTimeField(auto_now_add=True)
    tag_list = models.CharField(max_length=150,blank=True)
    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s,%s' %(self.usernameid,self.created)

class ArticleComment(models.Model):
    comment1 = models.ForeignKey(ArticlePublish, editable=False, on_delete=models.CASCADE)
    usernameid = models.ForeignKey(UserList, editable=False)
    created= models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=2000)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return u'%s,%s,%s' % (self.usernameid, self.created, self.content)

class SuggestionSubmit(models.Model):
    name = models.CharField(max_length=15,default=u'匿名用户')
    content = models.TextField()

class TagList(models.Model):
    tagname = models.CharField(max_length=150,unique=True)

    class Meta:
        ordering = ['tagname']

    def __unicode__(self):
        return u'%s' %(self.tagname)