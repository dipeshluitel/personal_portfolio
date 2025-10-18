from django.urls import path
from myPortfolio import views
urlpatterns = [
    path('about/', views.about, name='about'),
    path('projects/', views.project, name='about'),
    path('contact/', views.contact, name='about'),
]
