---
date: "2022-01-14T22:20:50.52Z"
published: true
slug: whats-the-ultimate-reason-for-working-at-octopus-energy-part-2
image: /images/autodocumenting-makefiles.png
tags:
  - python
  - howto
  - references
time_to_read: 5
title: Autodocumenting Makefiles
description: Make Your Makefiles Make Your Day!
---

A few years ago [Fabio da Luz](https://twitter.com/luzfcb) taught me some Makefile tricks. This is an expansion on what he taught me (I added the output list and sort feature).

# Using PYSCRIPT to Print Documentation

At the top of your `Makefile`, put in this code:

``` makefile
.DEFAULT_GOAL := help # Sets default action to be help

define PRINT_HELP_PYSCRIPT # start of Python section
import re, sys

output = []
# Loop through the lines in this file
for line in sys.stdin:
    # if the line has a command and a comment start with
    #   two pound signs, add it to the output
    match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
    if match:
        target, help = match.groups()
        output.append("%-10s %s" % (target, help))
# Sort the output in alphanumeric order
output.sort()
# Print the help result
print('\n'.join(output))
endef
export PRINT_HELP_PYSCRIPT # End of python section

help:
    @python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)
```

Next, add concise docstrings for every `Makefile` command. Here's a trio of examples:

``` Makefile
env:  ## Activate the virtual environment
	source venv/bin/activate

test: ## Runs the test suite 
	python manage.py test --thing=stuff

run:  ## Start the dev server
	python manage.py runserver    
```

Notice how each command's docstring starts with two pound signs? The "##"? That's what the auto documenter code needs to find the docstring.

# Trying it out!

When I type just `make` without any arguments, by default that triggers the `help` function, which runs the Python script at the top of the makefile. What I get is this:

``` plaintext
$ make
env             Activate the virtual environment
run             Start the dev server
test            Runs the test suite 
```

The results have been alphabetized, with comments displayed for each command. Very useful!


# The Whole File
 
``` Makefile
.DEFAULT_GOAL := help # Sets default action to be help

define PRINT_HELP_PYSCRIPT # start of Python section
import re, sys

output = []
# Loop through the lines in this file
for line in sys.stdin:
    # if the line has a command and a comment start with
    #   two pound signs, add it to the output
    match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
    if match:
        target, help = match.groups()
        output.append("%-10s %s" % (target, help))
# Sort the output in alphanumeric order
output.sort()
# Print the help result
print('\n'.join(output))
endef
export PRINT_HELP_PYSCRIPT # End of python section

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

env:  ## Activate the virtual environment
	source venv/bin/activate

test: ## Runs the test suite 
	python manage.py test --thing=stuff

run:  ## Start the dev server
	python manage.py runserver    

``` 
![Autodocumenting Makefiles](/images/autodocumenting-makefiles.png)