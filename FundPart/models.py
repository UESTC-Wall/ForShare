# -*- coding:utf-8 -*- 
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserList(User):
	user_rank_score = models.IntegerField(default=0)
	user_create_date = models.DateField(auto_now_add=True)

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
