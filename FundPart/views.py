# -*- coding:utf-8 -*- 
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import UrlPublish,UserList


# Create your views here.
# def home(request):
#     return


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

def index(request,page_num):
    start_url = (int(page_num) - 1) * 10
    end_url = int(page_num) * 10
    publish_list = UrlPublish.objects.order_by('urlpublish_time')[start_url:end_url-1]
    context = {'publish_list': publish_list}
    return render(request,'FundPages/index.html',context) 
 

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

def userregister(request):
	error1 = "this name is already exist"
	valid = "this name is valid"
	if request.method == 'GET':
		return render(request, 'FundPages/register.html')
	if request.method == 'POST':
		username = request.POST.get['username']
		password = request.POST.get['password']
		if UserList.objects.get(username=username):
			return render(request,'register.html',{'msg':"Name Exists"})
		user = UserList(username=username, password=password)
		user.save()
		return redirect('/fundpart/login')

def urlpublish(request):
	if request.method == 'GET':
		return redirect('fundpart/index/1')
	if request.method == 'POST':
		username = request.session['username'] 
		urlcontent = request.POST.get['urlcontent']
		urlintroduce = request.POST.get['urlintroduce']
		pub = UrlPublish.objects.create(
			username = username,
			urlmessage = urlcontent,
			urlcomment = urlintroduce
			)
		pub.save()
		return render(request,'Success!')