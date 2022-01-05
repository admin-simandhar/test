from django.conf.urls import url
from django.urls import include, path,re_path
from .import views 
urlpatterns = [
    # path('',views.DataAssetMasterClass.as_view()),
    path('',views.LoginManager.as_view()),

]