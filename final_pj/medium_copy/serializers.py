from rest_framework import serializers
from .models import Post, Comment, UserProfile, User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['bio']


class UserSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(source='userprofile.bio', required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'bio']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        userprofile_data = validated_data.pop('userprofile', {})
        bio = userprofile_data.get('bio', '')  

        user = User(username=validated_data['username'])
        user.set_password(validated_data['password']) 
        user.save()

        UserProfile.objects.create(user=user, bio=bio)

        return user
