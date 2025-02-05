from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),  # The home page handles the form submission
    path('login/',views.login,name='login'),
    path('dashboard/',views.home,name='dashboard'),
    path('login/',views.user_logout,name='login '),
    path('admindash/',views.admindash,name='admin'),
    path('send_email/',views.send_self_email,name='send_email')
]
