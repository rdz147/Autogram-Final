# auto/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.add_post, name='add_post'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
