from django.urls import path
from . import views


app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('profile', views.profile, name='profile'),
    path('info', views.info, name='info')
]