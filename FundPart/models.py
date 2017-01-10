# -*- coding:utf-8 -*- 
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserList(User):
	user_rank_score = models.IntegerField(default=0)
	user_create_date = models.DateField(auto_now_add=True)
	user_profile = models.ImageField(
			default = os.path.join(settings.MEDIA_ROOT,'images','generic_profile_photo.jpg'),
			upload_to='img',
			height_field=None,
			width_field=None, 
			max_length=100,
			null=True)
	user_email = models.EmailField(null=True)
	user_class = models.IntegerField()

	class Meta:
		permissions = (
			("can_deliver_message","can_deliver_message"),
			)
		default_permissions = ('change')
		ordering = ['user_rank_score','user_create_date']


class UrlPublish(models.Model):
	username = models.CharField(max_length=100)
	urlmessage = models.URLField()
	urlcomment = models.CharField(max_length=100)
	urlpublish_time = models.DateTimeField(auto_now_add=True)
	urlreadcount= models.IntegerField(default=0,editable=False)

class UrlComment(models.Model):
    blog = models.ForeignKey(UrlPublish, on_delete = models.CASCADE)
    username = models.TextField(max_length=20)
    comment_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length = 2000)

class SubComment(models.Model):
    comment = models.ForeignKey(UrlComment, on_delete = models.CASCADE)
    nickname = models.TextField(max_length=20)
    comment_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=2000)
