# -*- coding:utf-8 -*- 
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import Group
from django.core.files.base import ContentFile   
from django.template import loader, Context  

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import viewsets,generics   
from rest_framework import permissions

from django_filters.rest_framework import DjangoFilterBackend


from FundPart.serializers import *
from FundPart.models import *
from datareturn import gettitle2

def index(request,page_num =1):
    start_url = (int(page_num) - 1) * 10
    end_url = int(page_num) * 10
    try:
    	publish_list = UrlPublish.objects.order_by('-urlpublish_time')[start_url:end_url-1]
    except Exception,e:
    	publish_list = UrlPublish.objects.order_by('-urlpublish_time')[start_url:]
    context = ({'publish_list': publish_list})
    return render(request,'FundPages/index.html',context) 
 

##登陆
def userlogin(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		request.session.set_expiry(0)
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			request.session['username']= username
			return redirect('/fundpart/index/1')
		else:
			return render(request,'FundPages/userlogin.html')
	else:	
		return render(request,'FundPages/userlogin.html')

##登出
def userlogot(request):
	assert isinstance(request,HttpResponse)
	if request.method == 'GET':
		logout(request,request.user)
		logout(request,request.session['username'])
		del request.session['username']
		return redirect('fundpart/index/1')


##url发布
@login_required()
def urlpublish(request):
	if request.method == 'GET':
		return render(request, 'FundPages/write.html')
	if request.method == 'POST':
		name = request.session['username'] 
		urlcontent = request.POST['urlcontent']
		urlintroduce = request.POST['urlintroduce']
		try:
			print 1
			user = UserList.objects.get(username=name)
			UrlPublish.objects.get_or_create(
				username = user,
				urlmessage = urlcontent,
				urlintroduce = urlintroduce
				)
			context = ({'msg': 'Thank You!'})
		except Exception,e:
			print e
			context = ({'msg':'Something Wrong...'})
		return render(request, 'FundPages/write.html', context)

class LoginViewSet(APIView):
    queryset = User.objects.all()
    serializer_class = AuthTokenSerializer
    permission_classes=()
    def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		login(request,user)
		token, created = Token.objects.get_or_create(user=user)
		return Response({'userid':user.id, 'username':user.username, 'token': token.key})       

class UsersList(generics.ListCreateAPIView):
	queryset = UserList.objects.all()
	serializer_class = UserSerializer
	permission_classes =  (
		permissions.IsAuthenticatedOrReadOnly,
	)


class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = UserList.objects.all()
	serializer_class = UserSerializer
	permission_classes =  (
		permissions.IsAuthenticatedOrReadOnly,
	) 


class UrlPublishList(generics.ListCreateAPIView):
	queryset = UrlPublish.objects.all()
	serializer_class = UrlPublishSerializer

	def perform_create(self, serializer):
		url=self.request.data['urlmessage']
		title = gettitle2(url)
		print title
		serializer.save(username_id=UserList.objects.get(username=self.request.user.username),urlintroduce=title.decode("utf-8"))


class UrlCommentList(generics.ListCreateAPIView):
	queryset = UrlComment.objects.all()
	serializer_class = UrlCommentSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('comment1',)
	permission_classes =(
		permissions.IsAuthenticatedOrReadOnly,
	) 

	def perform_create(self, serializer):
		serializer.save(comment1=UrlPublish.objects.get(id=int(self.request.GET.values()[0])),username=UserList.objects.get(username=self.request.user.username))

class ArticleList(generics.ListAPIView):
	queryset = ArticlePublish.objects.all()
	serializer_class = ArticleListSerializer

class ArticlePublishView(generics.CreateAPIView):
	queryset = ArticlePublish.objects.all()
	serializer_class = ArticleDetailSerializer
	def perform_create(self, serializer):
		serializer.save(usernameid=UserList.objects.get(username=self.request.user.username))

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ArticlePublish.objects.all()
	serializer_class = ArticleDetailSerializer

class ArticleCommentList(generics.ListCreateAPIView):
	queryset = ArticleComment.objects.all()
	serializer_class = ArticleCommentSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('comment1',)
	permission_classes =(
		permissions.IsAuthenticatedOrReadOnly,
	) 

	def perform_create(self, serializer):
		serializer.save(comment1=UrlPublish.objects.get(id=int(self.request.GET.values()[0])),usernameid=UserList.objects.get(username=self.request.user.username))

