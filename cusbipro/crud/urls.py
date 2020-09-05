"""
=======================================
Routers for crud app:
=======================================
"""

# Django
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# Local app crud
from crud import views

urlpatterns = [
    path('client/', views.ClientView.as_view()),
    path('client/<int:pk>', views.ClientView.as_view()),
    path('bill/', views.BillView.as_view()),
    path('bill/<int:pk>', views.BillView.as_view()),
    path('product/', views.ProductView.as_view()),
    path('product/<int:pk>', views.ProductView.as_view()),
    path('billproduct/', views.BillProductView.as_view()),
    path('billproduct/<int:pk>', views.BillProductView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
