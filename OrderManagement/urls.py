from django.urls import path
from .views import *

urlpatterns = [
    path('basic/', BasicApiView.as_view()),

    path('customer/', CustomerView.as_view()),
    path('customer/<int:id>/', CustomerView.as_view()),

    path('product/', ProductView.as_view()),
    path('product/<int:id>/', ProductView.as_view()),
]