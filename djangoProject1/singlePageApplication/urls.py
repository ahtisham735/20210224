from django.urls import path
from . import views
app_name="singlePage"
urlpatterns=[path("",views.index,name="index")]

