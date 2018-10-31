from django.conf.urls import url
from . import views
urlpatterns= [
    url(r'^snake', views.snake, name ="snake"),
]
