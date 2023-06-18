from django.urls import path
from .views import HomeView, AboutView, RulesView, ExpertsView, ResultsView

urlpatterns = [
    path('', HomeView, name='home'),
    path('about/', AboutView, name='about'),
    path('rules/', RulesView, name='rules'),
    path('experts/', ExpertsView, name='experts'),
    path('results/', ResultsView, name='results'),
]