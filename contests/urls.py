from django.urls import path
from .views import ContestsView

urlpatterns = [
    path('contests/', ContestsView.as_view(), name='contests')
]