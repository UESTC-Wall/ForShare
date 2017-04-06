# -*- coding:utf-8 -*- 
from django.contrib import admin
from FundPart.models import *


class UrlPublishAdmin(admin.ModelAdmin):
    list_display = ('usernameid', 'urlmessage', 'urlintroduce', 'created', 'urlreadcount')
    list_filter = ['created']
    search_fields = ['urlintroduce']


admin.site.register(UserList)
admin.site.register(UrlPublish, UrlPublishAdmin)
admin.site.register(UrlComment)
admin.site.register(ArticlePublish)
admin.site.register(ArticleComment)
admin.site.register(SuggestionSubmit)
