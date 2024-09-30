from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name="index"),
    path('signup', views.signup, name= "signup"),
    path('register_user/',views.register_user, name="register_user"),
    path('home/', views.home, name='home'),
    path('logout/',views.logout, name= 'logout'),
    path('create_post/',views.create_post, name='create_post'),
    path('readmore/<int:id>/',views.readmore, name='readmore'),
    path('user_profile/', views.user_profile, name='user_profile')
    
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)