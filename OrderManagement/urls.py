from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('customer/', CustomerView.as_view()),
    path('customer/<int:id>/', CustomerView.as_view()),
    path('product/', ProductView.as_view()),
    path('product/<int:id>/', ProductView.as_view()),

    path('order/', OrderDetailsView.as_view()),
    path('order/<int:id>/', OrderDetailsView.as_view()),

    path('token/', MyTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('test/post/', TestView.as_view()),
    path('test/post/<int:id>/', TestView.as_view()),

    path('sample/', Sample.as_view()),
]