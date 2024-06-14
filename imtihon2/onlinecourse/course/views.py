from django.shortcuts import render
from .models import Like, Course, Comment, CourseTheme, CourseComment
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import (CourseSerializer, CommentSerializer, CourseThemeSerializer,
                          CourseCommentSerializer, MailSerializer, LikeSerializer)

from django.conf import settings
from django.core.mail import send_mail


# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseThemeViewSet(viewsets.ModelViewSet):
    queryset = CourseTheme.objects.all()
    serializer_class = CourseThemeSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CourseCommentViewSet(viewsets.ModelViewSet):
    queryset = CourseComment.objects.all()
    serializer_class = CourseCommentSerializer


class SendMail(APIView):

    def get(self, request):
        serializer = MailSerializer()
        return Response(serializer.data)

    def post(self, request):
        serializer = MailSerializer(data=request.data)
        serializer.is_valid()

        users = User.objects.all()
        for user in users:
            subject = serializer.validated_data.get('name')
            message = serializer.validated_data.get('text')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)

        return Response({'success': "Yuborildi"})


class FilterTheme(APIView):
    def get(self, request: Request):
        word = str(request.query_params.get('word'))
        coursetheme = CourseTheme.objects.filter(name__icontains=word)
        return Response({'coursetheme': CourseThemeSerializer(coursetheme, many=True).data})


class LikeAPIview(APIView):
    def get(self, request):
        serializer = LikeSerializer()
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = LikeSerializer(data=request.data)
        serializer.is_valid()

        if serializer.validated_data.get('like') == True:
            value = True
        else:
            value = False
            coursetheme_id = serializer.validated_data.get('coursetheme')
            coursetheme = CourseTheme.objects.get(pk=coursetheme_id)

        try:
            like = Like.objects.get(
                coursetheme=coursetheme,
                user=request.user
            )
            like.delete()
        except:
            pass

        Like.objects.create(
            coursetheme=coursetheme,
            user=request.user,
            likeordislike=value
        )

        return Response()
