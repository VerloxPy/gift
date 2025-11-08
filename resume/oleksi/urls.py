from django.urls import path
from oleksi import views

app_name = 'players'

urlpatterns = [
    path('', views.home, name='home'),
    path('project1/', views.project1, name='about'),
    path('project2/', views.project2, name='about'),
    path('project3/', views.project3, name='about'),
    path('future/', views.future, name='about'),
]