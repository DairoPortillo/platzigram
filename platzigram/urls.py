"""platzigram URL Configuration

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
from django.contrib import admin
# para arreglar problema con imagenes
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from platzigram import views as local_views
from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', local_views.helloWorld, name="hello_world"),
    path('hi/<str:name>/<int:age>', local_views.say_hi),
    path('', posts_views.PostsFeedView.as_view(), name='feed'),

    path('users/login/', users_views.LoginView.as_view(), name='login'),
    path('users/logout/', users_views.LogoutView.as_view(), name='logout'),
    path('users/signup/', users_views.SignupView.as_view(), name='signup'),

    path('users/me/profile/', users_views.UpdateProfileView.as_view(),
         name='update_profile'),

    path('posts/new/', posts_views.CreatePostView.as_view(), name='create_post'),

    path('users/<str:username>/',
         users_views.UserDetailView.as_view(template_name='users/detail.html'), name='detail')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
