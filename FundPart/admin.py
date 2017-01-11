# -*- coding:utf-8 -*- 
from django.contrib import admin
from FundPart.models import UserList,UrlPublish,UrlComment

admin.site.register(UserList)
admin.site.register(UrlPublish)
admin.site.register(UrlComment)
