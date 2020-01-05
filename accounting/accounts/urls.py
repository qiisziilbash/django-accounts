from django.urls import path

from accounts import views

urlpatterns = [
    path('accounts/login/', views.sign_in),
    path('accounts/register/', views.sign_up),
]
