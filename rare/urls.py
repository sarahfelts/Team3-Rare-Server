"""
URL configuration for rare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from rareapi.views import RareUserView, PostView, CategoryView, TagView, PostTagView, register_user, check_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', RareUserView, basename='rareuser')
router.register(r'posts', PostView, 'post')
router.register(r'categories', CategoryView, 'category')
router.register(r'tags', TagView, 'tag')
router.register(r'posttags', PostTagView, 'posttag')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('users/register_user', views.register_user, name='register_user'),
    path('users/<int:pk>/update_active_user/', views.RareUserView.as_view({'put': 'update_active_user'}), name='update_active_user'),
    path('checkuser', check_user),
    
]