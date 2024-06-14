from django.urls import path, include
from rest_framework import routers

from .views import (CourseViewSet, CommentViewSet, CourseThemeViewSet,
                    CourseCommentViewSet, SendMail, FilterTheme, LikeAPIview)

router = routers.DefaultRouter()

router.register('course-list', CourseViewSet)
router.register('course-theme', CourseThemeViewSet)
router.register('comment', CommentViewSet)
router.register('course-comment', CourseCommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('send-mail/', SendMail.as_view()),
    path('filter-theme/', FilterTheme.as_view()),
    path('like-dislike/', LikeAPIview.as_view()),
]
