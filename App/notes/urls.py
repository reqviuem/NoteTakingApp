from  django.urls import path
from .views import api_view

urlpatterns = [
    path('media/', api_view)
]