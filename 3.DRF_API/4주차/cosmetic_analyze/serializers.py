from cosmetic_analyze.models import Cosmetic, Category, Ingredient, Comment#, Profile
from django.contrib.auth.models import User
from rest_framework import serializers
'''
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    #user = serializers.ReadOnlyField(source='user.username')
    user = serializers.ReadOnlyField(source='Profile.user')
    #joined_at = serializers.ReadOnlyField(source='user.date_joined')
    class Meta:
        model = Profile
        fields = '__all__'
        #fields = ['__all__','joined_at']
'''

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'date_joined']

class CosmeticSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cosmetic
        fields = '__all__'
        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    #author = serializers.HyperlinkedRelatedField(many=True, view_name='comments:Comment-detail', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        #extra_kwargs = {'url': {'view_name': 'comments:user-detail'}}


