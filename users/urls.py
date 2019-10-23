"""为应用程序users定义URL模式"""
from django.contrib.auth.views import LoginView
from django.urls import include, path
from . import views

urlpatterns = [
    # 登陆界面
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register')
]
app_name = 'login'