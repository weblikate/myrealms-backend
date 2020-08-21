from rest_framework import serializers
from posts.models import *

class WritePostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WritePosts
        fields = ['writeContent', 'writeTimestamp', 'contributer']

class ClickPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClickPosts
        fields = ['clickImage','clickContent', 'clickTimestamp',  'contributer']

class ArtPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtPosts
        fields = ['artImage','artContent', 'artTimestamp', 'contributer']