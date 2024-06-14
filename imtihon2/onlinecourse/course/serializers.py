from rest_framework import serializers
from .models import Like, Course, Comment, CourseTheme, CourseComment


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CourseThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTheme
        fields = '__all__'


class CourseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseComment
        fields = '__all__'


class MailSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    text = serializers.CharField()


class LikeSerializer(serializers.Serializer):
    coursetheme = serializers.IntegerField()
    like = serializers.BooleanField()
    dislike = serializers.BooleanField()
