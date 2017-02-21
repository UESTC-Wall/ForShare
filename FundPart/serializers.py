from rest_framework import serializers

from FundPart.models import *

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, max_length=1024)
    password = serializers.CharField(required=True, max_length=1024)
    token = serializers.UUIDField()
    class Meta:
        model = UserList
        fields = ('id', 'username', 'password', 'token')

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
    owner = serializers.ReadOnlyField(source='username.username')
    urlintroduce = serializers.ReadOnlyField()
    urlcomment_set = serializers.StringRelatedField(
            many=True,
            allow_null=True,
            read_only=True,
        )

    class Meta:
		model = UrlPublish
		fields = ('username_id','owner','urlmessage','urlintroduce','urlpublish_time','urlreadcount','urlcomment_set')

class UrlCommentSerializer(serializers.ModelSerializer):
    comment_owner = serializers.ReadOnlyField(source='usernameid.username')
    class Meta:
		model = UrlComment
		fields = ('comment1','comment_owner','comment_time','content')


class ArticleListSerializer(serializers.ModelSerializer):
    article_owner = serializers.ReadOnlyField(source='usernameid.username')
    articlecomment_set = serializers.StringRelatedField(
            many = True,
            allow_null = True,
            read_only = True,
        )
    class Meta:
        model = ArticlePublish
        fields = ('usernameid','article_owner','id','article_abstract','article_readcount','publish_time','articlecomment_set')

class ArticleDetailSerializer(serializers.ModelSerializer):
    article_owner = serializers.ReadOnlyField(source='usernameid.username')
    class Meta:
        model = ArticlePublish
        fields = ('usernameid','article_owner','id','article','article_readcount','publish_time')


class ArticleCommentSerializer(serializers.ModelSerializer):
    comment_owner = serializers.ReadOnlyField(source='usernameid.username')
    class Meta:
        model = UrlComment
        fields = ('comment1','comment_owner','comment_time','content')