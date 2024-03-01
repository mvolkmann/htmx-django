from django.shortcuts import HttpResponse, redirect, render
from django.views.decorators.http import require_http_methods
import uuid

dog_map = {}
selected_id = '';

def add_dog(name, breed):
    id = str(uuid.uuid4())
    dog = {'id': id, 'name': name, 'breed': breed}
    dog_map[id] = dog
    return dog

add_dog('Comet', 'Whippet')
add_dog('Oscar', 'German Shorthaired Pointer')

def index(request):
    return HttpResponse("Hello, World!")

def test(request):
    return HttpResponse("This is a test.")

def index(request):
    return redirect('/dogs')

@require_http_methods(["DELETE", "GET", "POST", "PUT"])
def dog(request, id):
    global dog_map, selected_id

    if request.method == 'DELETE':
      # Deletes the dog with a given id.
      del dog_map[id]
      return ''

    elif request.method == 'POST':
      # Creates a new dog.
      name = request.form.get('name')
      breed = request.form.get('breed')
      new_dog = add_dog(name, breed);
      return render(request, 'dog-row.html', {'dog': new_dog, 'status': 201});

    elif request.method == 'PUT':
      # Updates a dog

      name = request.form.get('name')
      breed = request.form.get('breed')
      updatedDog = {'id': id, 'name': name, 'breed': breed};

      dog_map[id] = updatedDog;
      selected_id = '';

      res = render(request, 'dog-row.html', {'dog': updatedDog, 'swap': True})
      res['HX-Trigger'] = 'selection-change'
      return res

    else: # assume GET
      # Gets JSON for a dog with a given id.
      dog = dog_map[id]
      return dog

# Gets the main page.
@require_http_methods(["GET"])
def dogs(request):
    return render(request, 'dogs.html')

# Deselects the currently selected dog.
@require_http_methods(["GET"])
def deselect():
    global selected_id
    selected_id = ''
    res = HttpResponse('')
    res['HX-Trigger'] = 'selection-change'
    return res

# Gets the proper form for either adding or updating a dog.
@require_http_methods(["GET"])
def form(request):
    dog = dog_map.get(selected_id)
    return render(request, 'form.html', {'dog': dog})

# Gets table rows for all the dogs.
@require_http_methods(["GET"])
def rows(request):
    sorted_dogs = sorted(dog_map.values(), key=lambda x: x['name'])
    return render(request, 'dog-rows.html', {'dogs': sorted_dogs})

# Selects a dog.
@require_http_methods(["GET"])
def select(request):
    global selected_id
    selected_id = id;
    res = HttpResponse('')
    res['HX-Trigger'] = 'selection-change'
    return res
