# -*- coding:utf-8 -*- 
from django.conf.urls import url,include
from django.contrib import admin

from FundPart.forms import BootstrapAuthenticationForm
from FundPart.views import *
from FundPart.admin import *
from FundPart.FundPartUrls import *


from datetime import datetime

admin.autodiscover()

urlpatterns = [

    url(r'^admin/',include(admin.site.urls)),
    url(r'^$', 'FundPart.views.index'),
    # url(r'^contact$', 'FundPart.views.contact', name='contact'),
    # url(r'^about', 'FundPart.views.about', name='about'),
    url(r'^login/$',
       'django.contrib.auth.views.login',
       {
           'template_name': 'FundPages/login.html',
           'authentication_form': BootstrapAuthenticationForm,
           'extra_context':
           {
               'title': 'Log in',
               'year': datetime.now().year,
           }
       },
       name='login'),
  
    url(r'^fundpart/',include('FundPart.FundPartUrls')),
]

