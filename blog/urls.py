from django.conf.urls import url
from . import views

url(r'^snake', views.snake, name ="snake")
