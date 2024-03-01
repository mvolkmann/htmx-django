from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),

    path('deselect', views.deselect, name='deselect'),
    path('dog/<str:id>', views.dog, name='dog'),
    path('dogs', views.dogs, name='dogs'),
    path('form', views.form, name='form'),
    path('rows', views.rows, name='rows'),
    path('select/<str:id>', views.select, name='select')
]