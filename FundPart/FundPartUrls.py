from django.conf.urls import  patterns,url

urlpatterns = patterns('',
    (r'index/(?P<page_num>[0-9]*)$', 'FundPart.views.index'),
    (r'userlogin/$','FundPart.views.userlogin'),
    (r'register/$','FundPart.views.userregister'),
    (r'logout/$',
       'django.contrib.auth.views.logout',
       {
           'next_page': '/fundpart/index/1',
       }),
)

from rest_framework.urlpatterns import format_suffix_patterns
from FundPart import views

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'users/$',
        views.UsersList.as_view(),
        name='user-list'),
    url(r'users/(?P<pk>[0-9]+)/$',
        views.UsersDetail.as_view(),
        name='user-detail'),
    url(r'urlpublish/$',
    	views.UrlPublishList.as_view(),
    	name='url-publish-list'),
    url(r'urlpublish/(?P<pk>[0-9]+)/$',
    	views.UrlPublishDetail.as_view(),
    	name='url-publish-detail'),
    url(r'urlcomment/$',
    	views.UrlCommentList.as_view(),
    	name='url-comment-list'),
    url(r'urlcomment/(?P<pk>[0-9]+)/$',
    	views.UrlCommentDetail.as_view(),
    	name='url-comment-detail')
])