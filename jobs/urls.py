from django.urls import path

from .views import JobsVIew, Jobs2VIew

urlpatterns = [
    path('jobs/', JobsVIew.as_view(), name='jobs'),
    path('jobs/statistics/', Jobs2VIew, name='jobs2'),
]
