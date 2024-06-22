---
date: "2015-06-09"
published: true
slug: why-doesnt-python-have-switch-case
tags:
  - python
  - django
  - howto
time_to_read: 3
title: Why Doesn't Python Have Switch/Case?
image: /images/aliens.png
---

[![Aliens](/images/aliens.png)](/images/aliens.png)

Unlike every other programming language I've used before, Python does
not have a switch or case statement. To get around this fact, we use
dictionary mapping:

```python
def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "nothing")
```

This code is analogous to:

```javascript
function(argument){
    switch(argument) {
        case 0:
            return "zero";
        case 1:
            return "one";
        case 2:
            return "two";
        default:
            return "nothing";
    };
};
```

While the Python code is often more terse than the standard method of
handling cases, I could argue it is more arcane. When I first started
Python it felt weird and distracting. Over time it grew on me, the use
of a dictionary key being the identifier in a switch becoming more and
more habitual.

# Dictionary Mapping for Functions

In Python we can also include functions or lambdas in our dictionary
mapping:

```python
def zero():
    return "zero"

def one():
    return "one"

def numbers_to_functions_to_strings(argument):
    switcher = {
        0: zero,
        1: one,
        2: lambda: "two",
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "nothing")
    # Execute the function
    return func()
```

While the code inside `zero()` and `one` are simple, many Python
programs use dictionary mappings like this to dispatch complex
procedures.

# Dispatch Methods for Classes

If we don't know what method to call on a class, we can use a dispatch
method to determine it at runtime.

```python
class Switcher(object):
    def numbers_to_methods_to_strings(self, argument):
        """Dispatch method"""
        # prefix the method_name with 'number_' because method names
        # cannot begin with an integer.
        method_name = 'number_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "nothing")
        # Call the method as we return it
        return method()

    def number_0(self):
        return "zero"

    def number_1(self):
        return "one"

    def number_2(self):
        return "two"
```

Pretty nifty, right?

# The Official Answer

The [official
answer](https://docs.python.org/2/faq/design.html#why-isn-t-there-a-switch-or-case-statement-in-python)
says, "You can do this easily enough with a sequence of
`if... elif... elif... else`". And that you can use dictionary mapping
for functions and dispatch methods for classes.

Arguably the official answer doesn't explain anything except for
workarounds. In other words, a "non-answer". In my opinion, what the
official answer is really trying to say is, "Python doesn't need a
case statement."

# Really?

Yup. But there's more. I've heard people I respect say that
switch/case statements in code can be really hard to debug.

Personally I find that argument breaks down as soon as you run into
gigantic nested dictionaries used for mapping of code branches. Think
about it, a 100+ element nested dictionary is just as hard to debug as a
nested switch and case block with 100+ cases.

# Maybe Dictionary Mapping Runs Faster?

Moot as Python doesn't have a case statement. Talking about benchmarks
from other languages is pointless as what is faster in one language is
not always faster in another. Let's move on.

# The Significant Advantage of Python's Approach

Every once in a while I walk into a scenario where Python's approach
just works better than a switch/case statement. This is when at runtime
I need to add or remove potential items from the mapping. When this
occurs, my years of practice of writing dictionary mappings and dispatch
methods pays off. I have insights now that I never had back in the day
when I relied on switch/case statements.

# Closing Thoughts

To me, that Python forced me to accumulate lots of practical experience
with mappings is a blessing in disguise. The constraint of not having
switch/case statements allowed me to create approaches and ideas I may
not have developed with it.

Intentional or not, Python's lack of switch/case has been a social
construct that made me a better coder.

Enough so that I think this accidental social construct is a better
answer than the official one of 'Do this instead!'

---

# 2022 Post Script

In the years since I wrote this article it and my person have been accused of having a [Stockhom Syndrome](https://en.wikipedia.org/wiki/Stockholm_syndrome)-like bias for what might be a shortcoming in Python. Perhaps that is the truth.

In any case, as of Python 3.10 there's a [PEP 634: Structural Pattern Matching](https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching) in Python, which is Python's feature-rich implementation of switch/case.
