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
    password = serializers.HiddenField(default=True)
    
    class Meta:
        model = UserList  
        fields = ('id','username','password','user_email','user_class','user_profile')

class FollowRelationSerializer(serializers.ModelSerializer):
    followername = serializers.ReadOnlyField(source='follower.username')
    followedname = serializers.ReadOnlyField(source='followed.username') 
    class Meta:
        model = FollowRelation
        fields = ('followerid','followername','followedid','followedname','created')


class GroupSerializer(serializers.ModelSerializer):
    groupownername = serializers.ReadOnlyField(source='groupowner.username')
    groupmember_set = serializers.StringRelatedField(
        many=True,
        allow_null=True,
        read_only=True,
        )
    class Meta:
        model = Group
        fields = ('id','groupownerid','groupownername','groupname','created','groupintroduce','groupmember_set')          


class GroupMemberSerializer(serializers.ModelSerializer):
    groupname = serializers.ReadOnlyField(source='group.groupname') 
    membername = serializers.ReadOnlyField(source='memberid.username')
    class Meta:
        model = GroupMember
        fields = ('groupid','groupname','memberid','membername','created')

class UrlPublishSerializer(serializers.ModelSerializer):
    url_owner = serializers.ReadOnlyField(source='usernameid.username')
    urlintroduce = serializers.ReadOnlyField()
    urlcomment_set = serializers.StringRelatedField(
            many=True,
            allow_null=True,
            read_only=True,
        )
    taglist = serializers.ReadOnlyField()

    class Meta:
		model = UrlPublish
		fields = ('id','usernameid','url_owner','urlmessage','urlintroduce','created','urlreadcount','urlcomment_set','taglist')

class UrlCommentSerializer(serializers.ModelSerializer):
    comment_owner = serializers.ReadOnlyField(source='usernameid.username')
    class Meta:
		model = UrlComment
		fields = ('comment1','comment_owner','created','content')


class ArticleListSerializer(serializers.ModelSerializer):
    article_owner = serializers.ReadOnlyField(source='usernameid.username')
    articlecomment_set = serializers.StringRelatedField(
            many = True,
            allow_null = True,
            read_only = True,
        )
    taglist = serializers.ReadOnlyField()

    class Meta:
        model = ArticlePublish
        fields = ('id','usernameid','article_owner','id','article_abstract','article_readcount','created','articlecomment_set','taglist')

class ArticleDetailSerializer(serializers.ModelSerializer):
    article_owner = serializers.ReadOnlyField(source='usernameid.username')
    taglist = serializers.ReadOnlyField()
    class Meta:
        model = ArticlePublish
        fields = ('usernameid','article_owner','id','article','article_abstract','article_readcount','created','taglist')


class ArticleCommentSerializer(serializers.ModelSerializer):
    comment_owner = serializers.ReadOnlyField(source='usernameid.username')
    class Meta:
        model = UrlComment
        fields = ('comment1','usernameid','comment_owner','created','content')

class SuggestionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = SuggestionSubmit
        fields = ('name','content')