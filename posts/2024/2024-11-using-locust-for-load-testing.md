---
date: '2024-11-06T17:30:00.490082'
description: Quickstart guide for doing web application load testing with the Python powered locust library.
published: true
tags:
  - python
  - howto
  - load testing
title: Using locust for load testing
---

_Quickstart guide for doing web application load testing with the Python powered locust library._

[Locust](https://locust.io/) is a Python library that makes it relatively straightforward to write Python tests. This heavily commented code example explains each section of code. To use locust:

1. Install locust: `pip install locust`
2. Copy the file below into the directory where you want to run locust
3. In that directory, at the command-line, type: `locust`
4. Open [http://localhost:8089/](localhost:8089)

```python
# locustfile.py
# For more options read the following
#   https://docs.locust.io/en/stable/writing-a-locustfile.html

# Import Locust basics
from locust import HttpUser, task, between

# Imports for generating content
from string import ascii_letters
from random import randint, shuffle

def namer():
    "Create a random string of letters under 10 characters long"
    ascii_list = list(ascii_letters)
    shuffle(ascii_list)
    return ''.join(ascii_list[:10])

class CatsiteUser(HttpUser):
    """
    This class represents simulated users interacting with
    a website.
    """
    # how long between clicks a user should take
    wait_time = between(2, 5)
    # The default host of the target client. This can be changed
    # at any time
    host = 'http://localhost:5001/'

    def on_start(self):
        # Methods with the on_start name will be called for each
        # simulated user when they start. Useful for logins and
        # other 'do before doing other things'.
        pass

    def on_stop(self):
        # Methods with the on_stop name will be called for each
        # simulated user when they stop. Useful for logouts and
        # possibly data cleanup.
        pass    

    # TASKS!
    # Methods marked with the `@task` decorator is an action
    # taken by a user This example focuses on changes to a 
    # database, but provides a foundation for creating tests on
    # a more read-focused site

    @task
    def index(self):
        # User goes to the root of the project
        self.client.get('/')

    @task
    def create(self):
        # User posts a create form with the fields 'name'
        # and 'age'
        self.client.post('/create', dict(name=namer(), age=randint(1,35)))

    @task
    def update(self):
        # User posts an update form with the fields 'name'
        # and 'age'"
        with self.client.get('/random') as resp:
            pk = resp.text
            form_data = dict(id=pk, name=namer(), age=randint(1,35))
            self.client.post(f'/{pk}/update')

    @task
    def delete(self):
        # Represents the user getting a random ID and then
        # going to the delete page for it.
        with self.client.get('/random') as resp:
            pk = resp.text
            self.client.get(f'/{pk}/delete')
```

## Sample test site

For reference, this is the test site used to create the above locustfile. I'll admit that the above test is incomplete, a lot more tasks could be added to hit web routes. To use it:

1. Install FastHTML: `pip install python-fasthtml`
2. Copy the file into the directory you want to run it
3. In that directory, at the command-line, type: `python cats.py`
4. Open [http://localhost:5001/](localhost:5001)

```python
# cats.py
from fasthtml.common import *

# Set up the database and table
db = database('cats.db')
class Cat: name:str; age:int; id:int
cats = db.create(Cat, pk='id', transform=True)

# Instantiate FastHTML app and route handler
app, rt = fast_app()

def mk_form(target: str):
    return Form(
        P(A('Home', href=index)),
        Fieldset(
            Input(name='name'),
            Input(name='age', type='number'),

        ),
        Input(type='submit', value='submit'),
        hx_post=target, hx_swap="outerHTML"
    )

def cat_count():
    query = """select count(id) from cat;"""
    result = db.execute(query)
    return result.fetchone()[0]

@rt
def index():
    return Titled('Cats',
        P(
            A('Create cat', href='/create'), NotStr(' '),
            A('Random ID', href=random)),
        P(f'Number of cats: {cat_count()}'),        
        Ol(
            *[Li(A(f'{d.name}:{d.age}', href=f'/{d.id}')) for d in cats()]
        )
    )

@rt
def random():
    # Small dataset, we can get away with using the RANDOM() function
    query = """SELECT id FROM cat ORDER BY RANDOM() LIMIT 1;"""
    result = db.execute(query)
    return result.fetchone()[0]

@rt('/create')
def get():
    return Titled('Create Cat', 
        mk_form('/create')
    )

@rt('/create')
def post(cat: Cat):
    cat = cats.insert(Cat(name=cat.name, age=cat.age))
    return RedirectResponse(url=f'/{cat.id}')

@rt('/{id}')
def cat(id: int):
    cat = cats[id]
    return Titled(cat.name, 
        P(cat.age),
        P(A('update', href=f'/{id}/update')),
        P(A('delete', href=f'/{id}/delete')),
    )

@rt('/{id}/update')
def get(id: int):
    cat = cats[id]
    return Titled('Edit Cat',
        fill_form(mk_form(f'/{cat.id}/update'), cat)
    )

@rt('/{id}/update')
def post(cat: Cat, id: int):
    if id not in cats:
        return RedirectResponse(url=index)
    cat.id = id
    db.begin()
    try:
        cats.update(cat)
        db.commit()        
    except:
        db.rollback()
    return RedirectResponse(url=f'/{cat.id}')

@rt('/{id}/delete')
def cat(id: int):
    if id not in cats:
        RedirectResponse(url=index)
    # db.begin()
    cats.delete(id)
    # db.commit()
    return RedirectResponse(url=index)

serve()
```



