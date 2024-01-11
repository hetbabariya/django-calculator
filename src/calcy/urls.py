from django.urls import path
from .views import calcOperation

urlpatterns = [
    path('',calcOperation.as_view())
]