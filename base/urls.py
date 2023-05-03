from django.urls import path
from .import views
from django.http import HttpResponse


urlpatterns = [

    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('play',views.play,name="play"),
    path('restart',views.restart,name='restart'),
    path('checkanspuzz1',views.checkanspuzzle1,name='checkanspuzz1'),
    path('puzzle1hint1',views.puzzle1hint,name='puzzle1hint'),
    path('imghintpuzz1',views.imghintpuzz1,name='imghintpuzz1'),
    path('checkanspuzz2',views.checkanspuzz2,name='checkanspuzz2'),
    path('playcrossword',views.playcrossword,name='playcrossword'),
    path('checkanspuzz3',views.checkanspuzz3,name='checkanspuzz3'),
    path('puzzle3hint',views.puzzle3hint,name='puzzle3hint'),
    path('checkanspuzz4',views.checkanspuzz4,name='checkanspuzz4'),
    path('puzzle4hint',views.puzzle4hint,name='puzzle4hint'),
    
    


]
