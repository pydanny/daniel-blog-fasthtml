---
date: "2012-05-23"
published: true
slug: django-email-form-recaptcha
tags:
  - python
  - django
  - forms
  - howto
  - class-based-views
time_to_read: 2
title: "Django Class Based View: email form with CAPTCHA"
---

[Yesterday I showed how to implement a simple email
form](/simple-django-email-form.html) for
[Django](https://djangoproject.com) using Class Based Views. Today I'm
going to extend yesterday's work to use the excellent
[RECAPTCHA](https://www.google.com/recaptcha) service to help reduce spam
content.

This version requires `pip` installing the following into your
`virtualenv`.

- `pip install django-crispy-forms` so we can do Python driven
  layouts.
- `pip install django-floppyforms` so we get HTML5 elements for free.
- `pip install django-recaptcha` to do the RECAPTCHA work.

Don't forget to add the app to your INSTALLED_APPS in settings.py:

```python
INSTALLED_APPS += (
    'crispy_forms',
    'floppyforms',
    'captcha',
)
```

Generate your KEYs from the RECAPTCHA site and add them in settings.py:

```python
RECAPTCHA_PUBLIC_KEY = '6LcVu9ESAAAAANVWwbM5-PLuLES94GQ2bIYmSNTG'
RECAPTCHA_PRIVATE_KEY = '6LcVu9ESAAAAAGxz7aEIACWRa3CVnXN3mFd-cajP'
```

In myapp.forms.py:

```python
from captcha.fields import ReCaptchaField  # Only import different from yesterday
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import floppyforms as forms

class ContactForm(forms.Form):

    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField()  # Only field different from yesterday

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(ContactForm, self).__init__(*args, **kwargs)
```

In myapp.views.py:

```python
# Unchanged from yesterday. :-)
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

In `templates/myapp/email_form.html`:

```html
{# Also unchanged from yesterday. :-) #} {% extends 'base.html' %} {% load
crispy_forms_tags %} {% block title %}Send an email{% endblock %} {% block
content %}
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

# What I did

- Using `pip` I installed three packages into my Python environment.
- Added those three packages into the `INSTALLED_APPS` setting.
- Set the RECAPTCHA keys for my site.
- Modified the `forms.py` file from yesterday to include the RECAPTCHA
  field.
- Reduced spam content.

# What I could do

- Pin the app versions for a particular release. This is what you
  should be doing in normal development and in production, but for a
  blog entry I'm avoiding it because release numbers become quickly
  dated.
- Rather than change the `ContactForm` from yesterday, I could have
  extended it via inheritance.

# Want to learn more?

Check out the Django book I co-wrote, [Two Scoops of Django: Best
Practices for Django](https://www.feldroy.com/books/two-scoops-of-django-3-x)!
