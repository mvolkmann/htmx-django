Here are the steps I took to create this project.

- `cddev`
- `cd htmx`
- `mkdir htmx-django`
- `cd htmx-django`
- `python -m venv .venv`
- `. .venv/bin/activate`
- `pip install django`
- `django-admin startproject dogs`
- `cd dogs`
- `python manage.py startapp app` where "app" is the name of your app
- Edit `dogs/dogs/settings.py`
- Add the name of your app to the end of the `INSTALLED_APPS` list.
  For example:

  ```python
  INSTALLED_APPS = [
      ...
      "app"
  ]
  ```

- Edit the file `dogs/app/views.py` containing the following:

  ```python
  from django.shortcuts import render, HttpResponse

  def index(request):
      return HttpResponse("Hello, World!")
  ```

- Create the file `dogs/app/urls.py` containing the following:

  ```python
  from django.urls import path
  from . import views

  urlpatterns = [
      path('', views.index, name='index'),
  ]
  ```

- Edit the file `dogs/dogs/urls.py` to contain the following:

  ```python
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include("dogs.urls")),
  ]
  ```

- Create all the remaining files in this repo.
- Start the server by entering `./run`
- Browse localhost:5000
