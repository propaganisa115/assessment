from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import PostsSerializer
from .models import Posts

class PostCreateView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer