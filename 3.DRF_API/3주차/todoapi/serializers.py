from django.contrib.auth.models import User
from todoapi.models import Todo,Comment
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Todo
        fields = '__all__'
        #fields = ['url','title','description','created_at','updated_at','username']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
