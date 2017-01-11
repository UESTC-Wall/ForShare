# -*- coding:utf-8 -*- 
from django.conf.urls import url,include
from django.contrib import admin

from rest_framework import routers

from FundPart.forms import BootstrapAuthenticationForm
from FundPart import views
from FundPart.admin import *
from FundPart.FundPartUrls import *


from datetime import datetime

# import xadmin
# from xadmin.plugins import xversion

# xadmin.autodiscover()


# xversion.register_models()
# router = routers.DefaultRouter()
# router.register(r'users',views.UserList)
# router.register(r'urlpublish',views.UrlPublishList)
# router.register(r'urlcomment',views.UrlCommentList)

urlpatterns = [
    #url(r'xadmin/', include(xadmin.site.urls)),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^$', 'FundPart.views.index'),
    url(r'^fundpart/',include('FundPart.FundPartUrls')),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^$', include(router.urls)),
    url(r'^docs/',include('rest_framework_docs.urls')),
]

from rest_framework.urlpatterns import format_suffix_patterns
from FundPart import views

# API endpoints
# urlpatterns += format_suffix_patterns([
#     url(r'users/$',
#         views.UsersList.as_view(),
#         name='user-list'),
#     url(r'users/(?P<pk>[0-9]+)/$',
#         views.UsersDetail.as_view(),
#         name='user-detail'),
#     url(r'urlpublish/$',
#       views.UrlPublishList.as_view(),
#       name='url-publish-list'),
#     url(r'urlpublish/(?P<pk>[0-9]+)/$',
#       views.UrlPublishDetail.as_view(),
#       name='url-publish-detail'),
#     url(r'urlcomment/$',
#       views.UrlCommentList.as_view(),
#       name='url-comment-list'),
#     url(r'urlcomment/(?P<pk>[0-9]+)/$',
#       views.UrlCommentDetail.as_view(),
#       name='url-comment-detail')
# ])