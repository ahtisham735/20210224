from django.shortcuts import render
from rest_framework import generics
from .Serializer import UserSerializer
from .models import User
# Create your views here.
class UserView(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

def index(request):
    return render(request,"index.html")