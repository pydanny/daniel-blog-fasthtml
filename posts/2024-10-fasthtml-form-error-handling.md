---
date: '2024-10-15T16:02:06.179868'
description: A pattern I have been exploring for handling form errors in FastHTML.
published: true
tags:
- FastHTML
- python
- forms
title: FastHTML form error handling
---

_A pattern I have been exploring for handling form errors in FastHTML._

[FastHTML](https://fastht.ml/) has useful tools for handling forms. Every HTML form input field has a value attribute that we can use tools like [fill_form](https://docs.fastht.ml/api/components.html#fill_form) to hang data onto.

However, form designs are often too different to apply any universals from a framework like FastHTML. For example, one library might place errors in divs, another in paragraphs. The DOM identifiers can't be guaranteed to match.

I have found this pattern supports reporting form errors in a maintainable way. Let's dig in!

## The Imports

The pattern relies on Python dataclasses and type hints:

- Dataclasses provide a mechanism to store and later retrieve type hints at runtime. 
- Tpe hints determine whether or not a value can be null

```python
from dataclasses import dataclass, fields
from types import NoneType
from typing import get_args

# FastHTML curates what is in common via __all__, 
# so is safe to use with '*' import
from fasthtml.common import *
```

## The Form Dataclass

Let's define a `Profile` [dataclass](https://docs.python.org/3/library/dataclasses.html) representing a user's information. The name and email fields are required, age is optional. We make age option by having the type for age be `int` or `None`. 

```python
@dataclass
class Profile:
    name: str
    email: str
    age: int|None = None
```

## The Form Builder

Some Fast HTML example apps from the core repo have functions prefixed with `mk_`. They define forms and other elements. We use the same technique here. It lets us use our form in several places. It also works well with FastHTML's [fill_form](https://docs.fastht.ml/api/components.html#fill_form) function.

We differ in the first few lines of code. They manage the `errors` dict. If needed, they set errors to be the `Small` FT component, which renders to `<small style="font-color: red"></small>`. This HTML element [is used by Pico for form helper text elements](https://picocss.com/docs/forms#helper-text).

For projects using other design frameworks, we may need to define a different error element in a different location. Nevertheless, this can serve as an example of how to build a form generator function that can handle blank and errored forms. 

```python
def mk_profile_form(errors: dict|None = None):
    # If no errors, we default to {}
    if errors is None: errors = {}
    # Loop through the errors, rewriting strings into Small(str) elements
    for k,v in errors.items():
        errors[k] = Small(v, style='font-color: red')
    # Return the form
    return Form(
        Fieldset(
            Label(
                'First name (required)',
                Input(name='name'),
                # Get the name error or a blank string
                errors.get('name', NotStr(''))
            ),
            Label(
                'Email (required)',
                Input(type='email', name='email'),
                # Get the email error or a blank string
                errors.get('email', NotStr(''))
            ),
            Label(
                'Age',
                Input(type='number', name='age'),
                # Get the age error or a blank string
                errors.get('age', NotStr(''))
            )
        ),
        Input(type='submit', value='Subscribe'),
        # Use HTMX to post the form and upon response update the form
        hx_post=update_profile
    )    
```

## Setting up the routes

It's time to set up the web pages. First, we need to instantiate the route handlers. 

```python
app, rt = fast_app()
```

Then we write our index view. You'll note that we call the `mk_profile_form()` function without any arguments. This will have it generate a blank form.

```python
@rt
def index():
    return Titled("Form error handling",
        mk_profile_form()
    )
```

The next view has less than 10 lines yet is packed with so much functionality that I'm going to comment on every line. The view accepts an instantiated `Profile` dataclass. We lean on some of the feature of dataclasses and types to check the validity of the user's submission.

This view uses the `NoneType` and `get_args` functions from Python's type hint system to check if a field is required. Yup, we're using runtime type checking to determine whether or not a field can accept a null value.

```python
@rt
def update_profile(profile: Profile): 
    # Create the errors dict
    errors = {}
    # Use dataclasses.fields to iterate through the values
    # in our Profile dataclass
    for field in fields(profile):
        # Get the value from the field, with None if no
        # field is found
        value = getattr(profile, field.name)
        # If the value is not Truthy, which is either that no
        # value was specified or there was a zero-length string,
        # then check if NoneType was in the dataclass field types
        if not value and NoneType not in get_args(field.type):
            # Set the error string here
            errors[field.name] = f'Missing {field.name}'
    # Make the form using the mk_profile_form function,
    # passing in the errors dict 
    form = mk_profile_form(errors)
    # Using FastHTML's fill_form function to add the data submitted
    # by the user then return it back as an HTMX fragment
    return fill_form(form, profile)
```

This final line serves the FastHTML app. The `serve()` function is a wrapper around uvicorn.

```python
serve()
```

## Improvements?

Some ideas for improvements: 

1. Moving the error handling from the update view into the `mk_profile_form` function. This would make the views much smaller and the form even more portable
2. Creating a pydantic implementation. This will involve a few extra steps, but pydantic's built-in validation system might reduce complexity in other places
3. Include toasts or some other means to notify that the data has been accepted
4. Implement the pattern for single form input elements, rather than the whole form. This would apply when a field's value changes. Then, validation and saving would happen without touching the rest of the form.

