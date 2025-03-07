from django.urls import path
from .views import FeedView, PostDetailView, add_post, like_post, add_comment
from accounts.views import login_view as user_login  # Corrigido para importar de accounts.views
from . import views
from accounts.views import signup_view
from .views import index_view, feed_view

urlpatterns = [
    path('', index_view, name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', add_post, name='add_post'),
    path('post/<int:pk>/like/', like_post, name='like_post'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),
    path('signup/', signup_view, name='signup'),
    
]