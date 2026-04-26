from  django.urls import path
from . import views

urlpatterns = [
    path('save/', views.save),
    path('list/', views.get_list)
]