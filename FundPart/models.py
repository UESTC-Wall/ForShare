import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class UserList(User):
	user_rank_score = models.IntegerField(default=0)
	user_create_date = models.DateField(auto_now_add=True)
	user_profile = models.ImageField(
			default = os.path.join(settings.MEDIA_ROOT,'images','generic_profile_photo.jpg'),
			upload_to='img',
			height_field=None,
			width_field=None, 
			max_length=100,
			null=True)
	user_email = models.EmailField(null=True)
	user_class = models.IntegerField()

	class Meta:
		ordering = ['user_create_date']

	def __unicode__(self):
		return self.username 




class UrlPublish(models.Model):
	username = models.ForeignKey(UserList,editable=False,on_delete=models.CASCADE)
	urlmessage = models.URLField()
	urlintroduce = models.CharField(max_length=100)
	urlpublish_time = models.DateTimeField(auto_now_add=True)
	urlreadcount= models.IntegerField(default=0,editable=False)

	class Meta:
		ordering = ['-urlpublish_time']

	def __unicode__(self):
		return u'%s %s %s' %(self.username.username,self.urlpublish_time,self.urlintroduce)

class UrlComment(models.Model):
    comment1 = models.ForeignKey(UrlPublish,editable=False,on_delete = models.CASCADE)
    username = models.ForeignKey(UserList,editable=False)
    comment_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length = 2000)
    class Meta:
    	ordering = ['id']  

    def __unicode__(self):
    	return u'%s %s %s' %(self.username,self.comment_time,self.content)


# class SubComment(models.Model):
#     comment2 = models.ForeignKey(UrlComment, on_delete = models.CASCADE)
#     username = models.ForeignKey(UserList)
#     comment_time = models.DateTimeField(auto_now_add=True)
#     content = models.TextField(max_length=2000)
#     class Meta:
#     	ordering = ['id']
