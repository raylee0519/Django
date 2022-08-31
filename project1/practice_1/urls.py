from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.hello),
    path('jwt',views.jwtfuc),
    path('get_data',views.get_data),
    path('post_data',views.post_data),
    path('jwtfuc',views.jwtfuc),
    path('login',views.login),
    path('signup/',views.sign_up),
    path('all/',views.get_all_mem)
]