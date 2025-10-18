from django.urls import path
from myPortfolio import views

app_name = 'myPortfolio'
urlpatterns = [
    path('about/', views.about, name='about'),
    path('projects/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),
]
