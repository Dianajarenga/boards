"""boards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from board import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('home/', views.home, name='home'),
                  path('signup/', accounts_views.signup, name='signup'),
                  path('logout/', auth_views.LogoutView.as_view(), name='logout'),

                  path('boards/<int:id>/new/', views.new_topic, name='new_topic'),
                  path('boards/<int:id>/', views.board_topics, name='board_topics'),
                  path('api/user', include('user.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
