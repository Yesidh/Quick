"""
=======================================
Routers for csvfile app:
=======================================
"""

# Django
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# Local app crud
from csvfiles import views

urlpatterns = [
    path('csvclient/', views.CsvView.as_view()),
    path('uploadfile', views.CsvUploadFile.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
