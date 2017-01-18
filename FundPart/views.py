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
from rest_framework import viewsets,generics, status   
from rest_framework import permissions

from django_filters.rest_framework import DjangoFilterBackend


from FundPart.serializers import *
from FundPart.models import *

def getImg(request):
	assert isinstance(request,HttpResponse)
	#file_content = ContentFile(request.FILES['img'].read())  
    #img = ImageStore(name = request.FILES['img'].name,img=request.FILES['img'])  
    #img.save()


# def contact(request):
#     """Renders the contact page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'webpage/contact.html',
#         context_instance=RequestContext(request,
#             {
#                 'title': 'Contact',
#                 'message': 'Your contact page.',
#                 'year': datetime.now().year,
#             }
#         )
#     )


# def about(request):
#     """Renders the about page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'webpage1/about.html',
#         context_instance=RequestContext(request, {
#                     'title': 'About',
#                     'message': 'Your application description page.',
#                     'year': datetime.now().year, })
# )


##目录
def index(request,page_num =1):
    start_url = (int(page_num) - 1) * 10
    end_url = int(page_num) * 10
    try:
    	publish_list = UrlPublish.objects.order_by('-urlpublish_time')[start_url:end_url-1]
    except Exception,e:
    	publish_list = UrlPublish.objects.order_by('-urlpublish_time')[start_url:]
    context = ({'publish_list': publish_list})
    return render(request,'FundPages/index.html',context) 
 

##搜索
# def search_blog(request):
# 	blog_list=[]
#     search_word = request.GET.get("search_word")
#     sql = "SELECT * FROM FundPart_UrlPublsih WHERE urlcomment LIKE '%%" + search_word + "%%' or blog_title LIKE '%%" + search_word + "%%'"
#     urlintroduce = UrlPublish.objects.raw(sql).order_by('publish_time')
#     context = ({'blog_list': blog_list})
#     return render(request, 'FundPages/index.html', context)

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

##注册
def userregister(request):
	error1 = "this name is already exist"
	valid = "this name is valid"
	if request.method == 'GET':
		return render(request, 'FundPages/register.html')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		group = Group.objects.get(name=u'基础用户组')
		if UserList.objects.filter(username=username):
			return render(request,'register.html',{'msg':"Name Exists"})
		user = UserList(username=username, password=password,groups=group)
		user.save()
		return render(request, 'FundPages/write.html')

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

###一级评论
def comment(request):  
    username = request.POST.get("username")
    content = request.POST.get("content")
    blog_id = request.POST.get("url_id")
    comment_time = timezone.now()
    comment = Comment(nickname=nickname, blog_id=blog_id, content= content, comment_time=comment_time, email=email)
    comment.save()
    return JsonResponse({'status':'OK'})

##二级评论
def sub_comment(request): 
    nickname = request.POST.get("username")
    parent_comment_id = request.POST.get("parent_comment_id")
    sub_comment_content = request.POST.get("sub_comment_content")
    email = request.POST.get("email")
    comment_time = timezone.now()
    comment = SubComment(nickname=nickname, comment_id=parent_comment_id, content=sub_comment_content, comment_time=comment_time, email=email)
    comment.save()
    return JsonResponse({'status': 'OK'})

##阅读量
def readconunt(request,urlid):
	assert isinstance(request,HttpResponse)
	UrlPublish.objects.filter(id=urlid).update(urlreadcount = urlreadcount+1).save()


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
	permission_classes = (
		permissions.IsAuthenticatedOrReadOnly,
	)

class UrlPublishDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = UrlPublish.objects.all()
	serializer_class = UrlPublishSerializer
	permission_classes = (
		permissions.IsAuthenticatedOrReadOnly,
	)

class UrlCommentList(generics.ListCreateAPIView):
	queryset = UrlComment.objects.all()
	serializer_class = UrlCommentSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('comment1',)
	permission_classes = (
		permissions.IsAuthenticatedOrReadOnly,
	)

class UrlCommentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = UrlComment.objects.all()
	serializer_class = UrlCommentSerializer
	filter_fields = ('comment1')
	permission_classes = (
		permissions.IsAuthenticatedOrReadOnly,
	)
