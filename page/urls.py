from django.urls import path

from . import views

app_name = 'page'
urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('mail.html', views.mail, name='mail'),
    path('parcel.html', views.parcel, name='parcel'),
    path('logistics.html', views.logistics, name='logistics'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('comment', views.comment, name='comment'),
    path('profile', views.profile, name='profile')
]