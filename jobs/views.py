from django.shortcuts import render
from django.views.generic import ListView

from .models import JobsModel


class JobsVIew(ListView):
    template_name = 'main/jobs.html'
    model = JobsModel


def Jobs2VIew(request):
    return render(request, 'main/jobs2.html')
