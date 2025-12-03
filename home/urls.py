from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('me/', views.personal_page, name='me')
]