from django.urls import path
from . views import signup_view, login_view#, custom_logout_view
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/auto/index/'), name='logout'),
    #path('logout/', custom_logout_view, name='logout'),

]