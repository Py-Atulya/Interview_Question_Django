from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('javascript/',views.javascript,name='javascript'),
    path('python/',views.python,name='python'),
    path('django/',views.django,name='django'),
    path('react/',views.react,name='react'),


]