from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_form, name='feedback_form'),
    path('report/', views.feedback_report, name='feedback_report'),
]
