# -*- coding:utf-8 -*- 
from __future__ import absolute_import

from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
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
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


from FundPart.serializers import *
from FundPart.models import *
from datareturn import gettitle2,addtag



 
def index(request):
    return render_to_response('index.html',locals())

class LoginViewSet(APIView):
    queryset = User.objects.all()
    serializer_class = AuthTokenSerializer
    permission_classes=()
    def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data)
		print request.data
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		login(request,user)
		token, created = Token.objects.get_or_create(user=user)
		return Response({'userid':user.id, 'username':user.username, 'token': token.key})       

class UsersList(generics.ListAPIView):
	queryset = UserList.objects.all()
	serializer_class = UserSerializer
	permission_classes =  (
	)


class UserCreate(APIView):
	queryset = UserList.objects.all()
	serializer_class = UserSerializer
	permission_classes =  (
	)
	def post(self, request, *args, **kwargs):
		if len(UserList.objects.filter(username=request.data['username']))!=0:
			return Response({'detail':'exist'},status = status.HTTP_200_OK)
		try:	 
		 	user = UserList()
		 	user.username = request.data['username']
		 	user.user_email = request.data['user_email']
		 	user.user_class = request.data['user_class']
		 	user.set_password(request.data['password'])
		 	user.is_active = True
		 	user.is_staff = True
		 	user.save()
		 	return Response({'detail':"Success"})
		except Exception,e:
			print e
			return Response({'detail':'Failed'},status = status.HTTP_400_BAD_REQUEST)			 



class UsersDetail(generics.RetrieveUpdateAPIView):
	queryset = UserList.objects.all()
	serializer_class = UserSerializer
	permission_classes =  (
		permissions.IsAuthenticatedOrReadOnly,
	) 


class PersonalUrls(generics.ListAPIView):
	queryset = UrlPublish.objects.all()
	serializer_class = UrlPublishSerializer
	permission_classes = (
		permissions.IsAuthenticatedOrReadOnly,
	)
	
	def get_queryset(self):
		return UrlPublish.objects.filter(username_id_id= self.request.user.id)
		

class PersonalArticles(generics.ListAPIView):
	queryset = ArticlePublish.objects.all()
	serializer_class = ArticleListSerializer
	permission_classes = (
		permissions.IsAuthenticatedOrReadOnly,
	)
	
	def get_queryset(self):
		return ArticlePublish.objects.filter(usernameid_id= self.request.user.id)
		

class FollowList(generics.ListCreateAPIView):
	queryset = FollowRelation.objects.all()
	serializer_class = FollowRelationSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('followed','follower') 
	permission_classes = (
		permissions.IsAuthenticatedOrReadOnly,
	)

	def perform_create(self,serializer):
		serializer.save(
			follower = UserList.objects.get(username=self.request.user.username),
			followed = UserList.objects.get(id=self.request.data['followed'])
		)

class GroupList(generics.ListCreateAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('groupowner',)
	permissions_classes = (
		permissions.IsAuthenticatedOrReadOnly,
	)
	def perform_create(self,serializer):
		serializer.save(groupownerid=UserList.objects.get(username=self.request.user.username))

class GroupMemberList(generics.ListCreateAPIView):
	queryset = GroupMember.objects.all()
	serializer_class = GroupMemberSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('group','member')
	permissions_classes = (
		permissions.IsAuthenticatedOrReadOnly,
	)
	def perform_create(self,serializer):
		serializer.save(
			memberid = UserList.objects.get(username=self.request.user.username),
			groupid = Group.objects.get(id=self.request.data['group'])
		)			
		

class UrlPublishList(generics.ListCreateAPIView):
	queryset = UrlPublish.objects.all()
	serializer_class = UrlPublishSerializer
	filter_backends = (OrderingFilter,DjangoFilterBackend,)
	filter_fields = ('username')
	ordering_fields = '__all__' 

	def perform_create(self, serializer):
		url=self.request.data['urlmessage']
		try:
			title = gettitle2(url).decode("utf-8")
			taglist = addtag(url)
		except Exception, e:
			title = u"暂无介绍"
			taglist= u"暂无标签"
		finally:
			serializer.save(
				username_id=UserList.objects.get(username=self.request.user.username),
				urlintroduce=title,
				taglist = taglist	
			)


class UrlPublishPatch(generics.RetrieveUpdateDestroyAPIView):
	queryset = UrlPublish.objects.all()
	serializer_class = UrlPublishSerializer
	permission_classes = (
		permissions.IsAuthenticatedOrReadOnly,
	)

class UrlCommentList(generics.ListCreateAPIView):
	queryset = UrlComment.objects.all()
	serializer_class = UrlCommentSerializer
	filter_backends = (DjangoFilterBackend,OrderingFilter,)
	filter_fields = ('comment1',)
	ordering_fileds = '__all__'
	permission_classes =(
		permissions.IsAuthenticatedOrReadOnly,
	) 

	def perform_create(self, serializer):
		serializer.save(comment1=UrlPublish.objects.get(
			id=int(self.request.GET.values()[0])),
			username=UserList.objects.get(username=self.request.user.username)
			)

class ArticleList(generics.ListAPIView):
	queryset = ArticlePublish.objects.all()
	serializer_class = ArticleListSerializer
	filter_backends = (DjangoFilterBackend,OrderingFilter,)
	filter_fields = ('comment1',)
	ordering_fields = '__all__'
	permission_classes =(
		permissions.IsAuthenticatedOrReadOnly,
	) 

class ArticlePublishView(generics.CreateAPIView):
	queryset = ArticlePublish.objects.all()
	serializer_class = ArticleDetailSerializer
	

	def perform_create(self, serializer):
		content= self.request.data['article']
		try:
			taglist = addtag(content) 
		except Exception, e:
			taglist = u"暂无标签"
			
		serializer.save(
			usernameid=UserList.objects.get(username=self.request.user.username),
			taglist = taglist
		)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ArticlePublish.objects.all()
	serializer_class = ArticleDetailSerializer
	permission_classes = (
		permissions.IsAuthenticatedOrReadOnly,
	)

class ArticleCommentList(generics.ListCreateAPIView):
	queryset = ArticleComment.objects.all()
	serializer_class = ArticleCommentSerializer
	filter_backends = (DjangoFilterBackend,OrderingFilter,)
	filter_fields = ('comment1',)
	ordering_fields = '__all__'
	permission_classes =(
		permissions.IsAuthenticatedOrReadOnly,
	) 

	def perform_create(self, serializer):
		serializer.save(comment1=UrlPublish.objects.get(id=int(self.request.GET.values()[0])),usernameid=UserList.objects.get(username=self.request.user.username))

class SuggestionList(generics.ListCreateAPIView):
	queryset = SuggestionSubmit.objects.all()
	serializer_class = SuggestionSerilizer
	permission_classes = ()
