"""movieblog URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('api/', include('blog.api_urls')),

    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', blog_views.register, name='register'),
]
