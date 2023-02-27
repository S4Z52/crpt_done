from django.urls import path, re_path
from .views import PageHome , ViewFile
from . import views
urlpatterns = [

path('', views.home, name = "home"),
re_path(r'^upload/', PageHome.as_view(), name='upld'),
path('viewer/',ViewFile.as_view(), name='list_file'),

]