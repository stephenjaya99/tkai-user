from django.urls import path

from . import views

urlpatterns = [
    path('get/', views.TokenView.as_view(), name='get-token')
]