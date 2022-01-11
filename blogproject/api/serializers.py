from rest_framework import serializers

from .models import Posts

class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ('id','title', 'content','published_at','created_at','updated_at')
