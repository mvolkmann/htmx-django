from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),

    path('dogs', views.all_dogs, name='dogs'),
    path('form', views.form, name='form'),
    path('rows', views.rows, name='rows'),
]