from django.urls import include, path
from rest_framework import routers
from . import views
from .views import PostCreateView, PostRetrieveUpdateDestroyView


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts', PostCreateView.as_view(),name='create'),
    path('posts/<int:pk>', PostRetrieveUpdateDestroyView.as_view(),name='details'),
]