from django.urls import path

from . import views

urlpatterns = [
    # read views.py and execute index function
    # read views.py and execute menu function
    path('', views.home, name='Home'),
<<<<<<< HEAD
    path('Home', views.home, name='Home'),
=======
>>>>>>> d281ac15d6ec70f8d3dc28d65dd6438777ffab07
    path('register', views.Register, name='Register'),
    path('login2', views.login2, name='login2'),
    path('table', views.table, name='table'),
    

    



]   
