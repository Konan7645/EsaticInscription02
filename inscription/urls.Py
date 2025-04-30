from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('inscription/', views.nouvelle_inscription, name='nouvelle-inscription'),
    path('confirmation/<int:pk>/', views.ConfirmationView.as_view(), name='confirmation'),
    path('pdf/<int:pk>/', views.generer_pdf, name='generer-pdf'),
]