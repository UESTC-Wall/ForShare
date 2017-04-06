# -*- coding:utf-8 -*- 
from django.conf.urls import url,include
from django.contrib import admin

from rest_framework import routers

from FundPart.forms import BootstrapAuthenticationForm
from FundPart import views
from FundPart.admin import *
from FundPart.FundPartUrls import *


from datetime import datetime
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^$', schema_view),
    url(r'^fundpart/',include('FundPart.FundPartUrls'),name="基础管理"),
    url(r'^docs/',include('rest_framework_docs.urls')),
]