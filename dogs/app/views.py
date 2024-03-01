from django.shortcuts import HttpResponse, redirect, render
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

def all_dogs(request):
    return render(request, 'dogs.html')

# @app.route('/dogs/<id>')
# def one_dog(id):
#     dog = dog_map[id]
#     return dog # returns JSON

# # Deletes the dog with a given id.
# @app.route('/dog/<id>', methods=['DELETE'])
# def delete_dog(id):
#     global dog_map
#     del dog_map[id]
#     return ''

# # Deselects the currently selected dog.
# @app.route('/deselect')
# def deselect():
#     global selected_id
#     selected_id = ''
#     res = Response('')
#     res.headers['HX-Trigger'] = 'selection-change'
#     return res

# Gets the proper form for either adding or updating a dog.
def form(request):
    dog = dog_map.get(selected_id)
    return render(request, 'form.html', {'dog': dog})

# Gets table rows for all the dogs.
def rows(request):
    sorted_dogs = sorted(dog_map.values(), key=lambda x: x['name'])
    return render(request, 'dog-rows.html', {'dogs': sorted_dogs})

# # Selects a dog.
# @app.route('/select/<id>')
# def select(id):
#     global selected_id
#     selected_id = id;
#     res = Response('')
#     res.headers['HX-Trigger'] = 'selection-change'
#     return res

# # Creates a dog.
# @app.route('/dog', methods=['POST'])
# def create(request):
#     name = request.form.get('name')
#     breed = request.form.get('breed')
#     new_dog = add_dog(name, breed);
#     return render(request, 'dog-row.html', {'dog': new_dog, 'status': 201});

# # Updates a dog
# @app.route('/dog/<id>', methods=['PUT'])
# def update(request, id):
#     name = request.form.get('name')
#     breed = request.form.get('breed')
#     updatedDog = {'id': id, 'name': name, 'breed': breed};

#     global dog_map
#     dog_map[id] = updatedDog;

#     global selected_id
#     selected_id = '';

#     res = make_response(
#         render_template('dog-row.html', {'dog': updatedDog, 'swap': True})
#     )
#     res.headers['HX-Trigger'] = 'selection-change'
#     return res