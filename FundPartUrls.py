from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from FundPart import views

urlpatterns = patterns('',
                       
                       )

# API endpoints
urlpatterns += format_suffix_patterns([
    url(r'login/$', views.LoginViewSet.as_view()),
    url(r'users/$',
        views.UsersList.as_view(),
        name='user-list'),
    url(r'usercreate/$',
        views.UserCreate.as_view(),
        ),
    url(r'users/(?P<pk>[0-9]+)/$',
        views.UsersDetail.as_view(),
        name='user-detail'),
    url(r'urlpublish/$',
        views.UrlPublishList.as_view(),
        name='url-publish-list'),
    url(r'urlpublish/(?P<pk>[0-9]+)/$',
        views.UrlPublishPatch.as_view(),
        name='url-publish-detail'),
    url(r'urlpublsih/(P<username>[0-9]+)/$',
        views.UrlPublishList.as_view,
        name='url-publish-detail-gets'),
    url(r'urlcomment/$',
        views.UrlCommentList.as_view(),
        name='url-comment-list'),
    url(r'articlelist/$',
        views.ArticleList.as_view(),
        name='articlelist'),
    url(r'articlelist/(?P<pk>[0-9]+)/$',
        views.ArticleDetail.as_view(),
        name='url-publish-detail'),
    url(r'articlepublish/$',
        views.ArticlePublishView.as_view()),
    url(r'articlecomment/',
        views.ArticleCommentList.as_view()),
    url(r'suggestion/',
        views.SuggestionList.as_view()),
])
