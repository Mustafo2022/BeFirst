from django.urls import path
from .views import HomeView, AboutView, RulesView

urlpatterns = [
    path('', HomeView, name='home'),
    path('about/', AboutView, name='about'),
    path('rules/', RulesView, name='rules'),
]