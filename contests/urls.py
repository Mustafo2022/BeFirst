from django.urls import path
from .views import ContestsView, contests2View

urlpatterns = [
    path('contests/', ContestsView.as_view(), name='contests'),
    path('contests/submit/', contests2View, name='contests2'),
]