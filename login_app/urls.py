from django.conf.urls import url
from django.urls import path
from . import views
app_name="login_app"

urlpatterns = [
    path('',views.home,name="home"),
    path('signup/',views.signUp,name="signup"),
    path('signin/',views.signIn,name="signin"),
    path('signout',views.signOut,name='signout')
    ]
