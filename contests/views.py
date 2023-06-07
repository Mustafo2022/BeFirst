from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ContestsModel


class ContestsView(ListView):
    model = ContestsModel
    template_name = 'main/contests.html'
    paginate_by = 12