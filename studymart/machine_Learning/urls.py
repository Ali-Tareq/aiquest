from django.urls import path
from . import views

urlpatterns = [
    path('machine/',views.machine_learning),
    path('rf/',views.random_forest),
]
