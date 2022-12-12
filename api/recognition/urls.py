from django.urls import path
from recognition import views

urlpatterns = [
    path('', views.recognition_attempt)
]