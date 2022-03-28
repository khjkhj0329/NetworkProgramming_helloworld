from django.urls import path
from self_test import views

app_name = 'self_test'

urlpatterns = [
    path('hyunwook/', views.hyunwook, name='hyunwook'),
    path('seopahn/', views.secopahn, name='seopahn'),
]