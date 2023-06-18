from django.urls import path
from .views import LoginView, RegisterView, RealgisterView, PaymentView

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('account/', RegisterView, name='register'),
    path('registration/', RealgisterView, name='realgister'),
    path('payment/', PaymentView, name='payment'),
]