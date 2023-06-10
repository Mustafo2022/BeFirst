from django.urls import path
from .views import LoginView, RegisterView

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('registration/', RegisterView, name='register'),
]