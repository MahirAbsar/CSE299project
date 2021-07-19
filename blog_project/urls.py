from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('login_app.urls')),
    path('',views.home,name='home'),
]
