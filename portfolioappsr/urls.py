from django.urls import path
from portfolioappsr import views

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('projects/', views.projects,name='projects'),
    path('certificates/', views.certificates,name='certificates'),
    path('blogs/', views.blogs,name='blogs'),
    path('', views.exploremore,name='exploremore'),
    path("signup",views.signup,name='signup'),
    path("login",views.handlelogin,name='handlelogin'),
    path("logout/",views.handlelogout,name='handlelogout'),
    
]