from django.urls import path
from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.sessfun, name='sessfun'),
    path('', views.cookie, name='cookie')
]
