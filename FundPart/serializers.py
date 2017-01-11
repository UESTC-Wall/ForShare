from rest_framework import serializers

from FundPart.models import *

class UserSerializer(serializers.ModelSerializer):
    # tracks = serializers.HyperlinkedRelatedField(
    #     	many=True,
    #     	allow_null=True,
    #     	read_only=True,
    #     	view_name='track-urlpublish'
    # 	)
    class Meta:
        model = UserList  
        fields = ('id','username','user_rank_score','user_email','user_class')


class UrlPublishSerializer(serializers.ModelSerializer):
 # 	tracks = serializers.HyperlinkedRelatedField(
 #    	many=True,
 #    	allow_null=True,
 #    	read_only=True,
 #    	view_name='track-urlcomment'
	# )
	class Meta:
		model = UrlPublish
		fields = ('id','username','urlmessage','urlintroduce','urlpublish_time','urlreadcount')


class UrlCommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = UrlComment
		fields = ('comment1','username','comment_time','content')