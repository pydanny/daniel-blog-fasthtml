---
date: "2012-05-22"
published: true
slug: simple-django-email-form
tags:
  - python
  - django
  - forms
  - howto
  - class-based-views
time_to_read: 1
title: Simple Django email form using CBV
---

Here's a simple `FormView` Class Based Views for
[Django](https://djangoproject.com). Here is a sample of how to do one as
a simple email form. There is no CAPTCHA in this example, that's the
topic of a future blog post.

This version requires the following packages `pip` installed into your
`virtualenv`.

- `django-crispy-forms` so we can do Python driven layouts.
- `django-floppyforms` so we get HTML5 elements for free.

They also need to be added to your list of `INSTALLED_APPS`:

```python
INSTALLED_APPS += (
    'crispy_forms',
    'floppyforms',
)
```

In myapp.forms.py:

```python
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import floppyforms as forms

class ContactForm(forms.Form):

    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(ContactForm, self).__init__(*args, **kwargs)
```

In myapp.views.py:

```python
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import FormView

from myapp.forms import ContactForm

class ContactFormView(FormView):

    form_class = ContactForm
    template_name = "myapp/email_form.html"
    success_url = '/email-sent/'

    def form_valid(self, form):
        message = "{name} / {email} said: ".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'))
        message += "\n\n{0}".format(form.cleaned_data.get('message'))
        send_mail(
            subject=form.cleaned_data.get('subject').strip(),
            message=message,
            from_email='contact-form@myapp.com',
            recipient_list=[settings.LIST_OF_EMAIL_RECIPIENTS],
        )
        return super(ContactFormView, self).form_valid(form)
```

In templates/myapp/email_form.html:

```html
{% extends 'base.html' %} {% load crispy_forms_tags %} {% block title %}Send an
email{% endblock %} {% block content %}
<div class="row">
  <div class="span6">
    <h1>Send an email</h1>
    {% crispy form form.helper %}
  </div>
</div>
{% endblock %} {% block extrajs %}
<script src="{{ STATIC_URL }}js/jquery-1.7.1.min.js"></script>
<script type="text/javascript">
  $(function () {
    $("#id_name").focus();
  });
</script>
{% endblock %}
```

# Tomorrow's blog post

In tomorrow's post I'll show how to add CAPTCHA into your project to
help reduce spam messages.

# Want to learn more?

Check out the Django book I co-wrote, [Two Scoops of Django: Best
Practices for Django
1.11](https://roygreenfeld.com/products/two-scoops-of-django-1-11)!
