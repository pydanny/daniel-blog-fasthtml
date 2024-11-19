---
date: '2024-05-25T12:42:48.161069'
description: A management command for quickly generating tests based off Django's URL routing mechanism.
published: true
tags:
  - django
  - python
  - howto
  - testing
title: Rapidly creating smoke tests for Django views
---

*A management command for quickly generating tests based off Django's URL routing mechanism.*

Recently [Peter Baumgartner](https://lincolnloop.com/about/peter-baumgartner/) of [Lincoln Loop](https://lincolnloop.com/) wrote a [fantastic article](https://www.linkedin.com/posts/pbaumgartner_ever-pick-up-a-legacy-project-that-has-activity-7186794287362183168-Bpcw) about the technique of writing smoke tests for Django views. Go read it, Peter provides really good justification for these smoke tests, especially for taking on legacy project without tests. Heck, the reason why I'm writing this post is so I have it in the bookmark service that is my blog.

Inspired as I was by Peter's article, I wrote a little management command to help build out smoke tests quickly. It's not perfect, and chances are you'll need to modify the results for the tests to be accurate. Certainly you'll need to add filtering like what I did with the `admin` to account for third-party packages that already have tests. Nevertheless, I've found it a useful tool for writing out smoke tests quickly.

In this example, it generates smoke tests to be called by `pytest` via [pytest-django](https://pypi.org/project/pytest-django/). It can be modified to work with standard Django unit tests.

```python
# myapp/management/commands/make_smoke_tests.py
from django.core.management.base import BaseCommand
from django.urls import get_resolver


class Command(BaseCommand):
    help = 'Generates smoke tests for projects.'

    def handle(self, *args, **options):
        urlconf = get_resolver(None)
        self.generate_smoke_tests(urlconf)

    def generate_smoke_tests(self, urlconf, prefix=''):
        views = []
        for pattern in urlconf.url_patterns:
            if hasattr(pattern, 'app_name') and pattern.app_name == 'admin':
                continue
            if hasattr(pattern, 'name'):
                self.stdout.write(f"def test_{pattern.name}(client):")
                self.stdout.write(f'    response = client.get("/{pattern.pattern}/")')
                self.stdout.write('    assert response.status_code == 200')
                self.stdout.write('')
            if hasattr(pattern, 'url_patterns'):
                more_views = self.generate_smoke_tests(pattern, prefix + pattern.pattern.regex.pattern)
                views.extend(more_views)
        return views
```

Writing output to the terminal:

```bash
./manage.py make_smoke_tests
```

Writing output to a file on OSX and Linux:

```bash
./manage.py make_smoke_tests > tests/test_smoke.py
```

Try it and tell me what you think!

# Update May 25, 2024

[Ejay Aito](https://github.com/aitoehigie) aka [pystar](https://x.com/pystar) made improvements which you can see [here](https://gist.github.com/aitoehigie/5bff431082b67f52e993465334422e6d). He added the features listed below. Check out his work!

1. added an argument for the output file path. If no output file is specified, it defaults to `smoke_tests.py`. 
2. The script now properly handles URL parameters by extracting them with a regex and replacing them with sample values.
3. Tests can also be generated for POST, PUT, and DELETE methods.