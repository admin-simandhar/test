from django.conf.urls import url
from django.urls import include, path,re_path
from .import views 
urlpatterns = [
    path('',views.Student.as_view()),
    path('course',views.StudentCourse.as_view()),
]