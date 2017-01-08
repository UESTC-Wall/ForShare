from django.conf.urls import patterns, url

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

