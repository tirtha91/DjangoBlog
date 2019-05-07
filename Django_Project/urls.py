"""Django_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

# for blog/ it will process blog/ and will go to 'myblogApp.urls' to check if any blank URLs are present for view
# for blog/about/ it will process blog/ and will go to 'myblogApp.urls' to check if the remaining about/ 
# has any matching URL patterns
# from django.contrib.auth import views as auth_views required to import default login and logout views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path , include
from userApp import views as userApp_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('blog/', include('myblogApp.urls')), -> To make Blog.home as home page of localhost:8000 make it
    path('register/' , userApp_views.register , name='register'),
    path('profile/' , userApp_views.profile , name='profile'),
    path('login/' , auth_views.LoginView.as_view(template_name='userAppTemplates/login.html') , name='login'),
    path('logout/' , auth_views.LogoutView.as_view(template_name='userAppTemplates/logout.html') , name='logout'),
    path('password-reset/' , auth_views.PasswordResetView.as_view(template_name='userAppTemplates/password_reset.html') , name='password_reset'),
    path('password-reset/done/' , auth_views.PasswordResetDoneView.as_view(template_name='userAppTemplates/password_reset_done.html') , name='password_reset_done'),
    path('', include('myblogApp.urls')),  
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


