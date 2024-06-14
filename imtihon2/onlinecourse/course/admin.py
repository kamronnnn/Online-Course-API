from django.contrib import admin
from .models import Course, CourseTheme, Comment, CourseComment

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'started', 'duration', 'price')


class CourseThemeAdmin(admin.ModelAdmin):
    list_display = ('course', 'name')
    list_display_links = ('course', 'name')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('coursetheme',)


class CourseCommentAdmin(admin.ModelAdmin):
    list_display = ('course',)


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseTheme, CourseThemeAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CourseComment, CourseCommentAdmin)
