from django.urls import include, path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index_view, name = 'index')
]