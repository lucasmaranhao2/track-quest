from django.urls import include, path
from . import views

app_name = 'user'

url_patterns = [
    path('', views.index_view, name = 'index')
]