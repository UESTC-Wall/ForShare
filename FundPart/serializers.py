from rest_framework import serializers

from FundPart.models import *

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, max_length=1024)
    password = serializers.CharField(required=False, max_length=1024)

    class Meta:
        model = UserList
        fields = ('id', 'username', 'password')

class UserSerializer(serializers.ModelSerializer):
    urlpublish_set = serializers.StringRelatedField(
            many=True,
            allow_null=True,
            read_only=True,   
    	)
    class Meta:
        model = UserList  
        fields = ('id','username','user_rank_score','user_email','user_class','urlpublish_set')


class UrlPublishSerializer(serializers.ModelSerializer):
    urlcomment_set = serializers.StringRelatedField(
            many=True,
            allow_null=True,
            read_only=True,
        )
    
    class Meta:
		model = UrlPublish
		fields = ('username','urlmessage','urlintroduce','urlpublish_time','urlreadcount','urlcomment_set')


class UrlCommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = UrlComment
		fields = ('comment1','username','comment_time','content')