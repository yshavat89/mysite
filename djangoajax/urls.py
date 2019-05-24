from django.urls import path
from . import views


urlpatterns = [
    path('jsonview/', views.JSONView.as_view() ),
]