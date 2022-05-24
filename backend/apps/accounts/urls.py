from django.urls import path

from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='sign_in'),
    path('register/', UserRegisterView.as_view(),name='register'),
    path('register_done/', RegisterDoneView.as_view(), name='register_done'),
    path('logout/', user_logout, name = 'logout'),
]
