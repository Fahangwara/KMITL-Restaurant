"""myrestauant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

import sys
sys.path.append("../")

from django.contrib import admin
from django.urls import path
from homepage import views as homepage_views
from django.conf.urls import url
from login import views as login_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_views.homepage, name='index'),
    path('detail/<restaurant_id>/', homepage_views.detail_page),
    path('login/', login_views.auth_login, name='user_login'),
    path('admin/homepage/restaurant/<int:restaurant_id>/change/', homepage_views.restaurant_edit, name='restaurant_edit'),
    path('index/', login_views.auth_logout, name='auth_logout'),


]
