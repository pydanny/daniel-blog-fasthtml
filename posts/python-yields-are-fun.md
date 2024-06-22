---
date: '2013-11-22'
published: true
slug: python-yields-are-fun
tags:
- python
time_to_read: 3
title: Python Yields are Fun!
---

While you can optimize the heck out of your Python code with
`generators` and `generator expressions` I'm more interested in goofing
around and solving classic programming questions with the `yield`
statement.

**note:** For this article, since it's easier to explain things as they
happen, I'll be including a lot of inline comments.

Let's start with a simple function that returns a sequence of some of
my favorite values:

``` python
# yielding.py
def pydanny_selected_numbers():

    # If you multiple 9 by any other number you can easily play with
    #   numbers to get back to 9.
    #   Ex: 2 * 9 = 18. 1 + 8 = 9
    #   Ex: 15 * 9 = 135. 1 + 3 + 5 = 9
    #   See https://en.wikipedia.org/wiki/Digital_root
    yield 9

    # A pretty prime.
    yield 31

    # What's 6 * 7?
    yield 42

    # The string representation of my first date with Audrey Roy
    yield "2010/02/20"
```

**note:** When a function uses the `yield` keyword it's now called a
**generator**.

Let's do a test drive in the REPL:

``` python
>>> from yielding import pydanny_selected_numbers  # import ye aulde code

>>> pydanny_selected_numbers()  # create the iterator object
<generator object pydanny_selected_numbers at 0x1038a03c0>

>>> for i in pydanny_selected_numbers():  # iterate through the iterator
...     print(i)
...
9
31
42
"2010/02/20"

>>> iterator = pydanny_selected_numbers() # create the iterator object
>>> for i in iterator:  # iterate through the iterator object
...     print(i)
...
9
31
42
"2010/02/20"
```

Of course, if you know anything about generator expressions, you know I
could do this more tersely with the following:

``` python
>>> iterator = (x for x in [9, 31, 42, "2010/02/20"]) 
>>> for i in iterator:
...     print(i)
...
9
31
42
"2010/02/20"
```

While that is more terse, it doesn't give us the amount of control we
get by defining our own generator function. For example, what if I want
to present the Fibonacci sequence in a loop rather than with recursion?

``` python
# fun.py
def fibonacci(max):
    result = 0
    base = 1
    while result <= max:

        # This yield statement is where the execution leaves the function.
        yield result
        # This is where the execution comes back into the function. This is
        # just whitespace, but that it came back while preserving the state
        # of the function is pretty awesome.

        # Fibonacci code to increase the number according to
        #   https://en.wikipedia.org/wiki/Fibonacci_number
        n = result + base
        result = base
        base = n

if __name__ == "__main__":

    for x in fibonacci(144):
        print(x)
```

Let's try this out in the REPL:

``` python
>>> from fun import fibonacci
>>> fibonacci(10)
<generator object fibonacci at 0x10d49e460>
>>> for x in fibonacci(10):
...     print(x)
0
1
1
2
3
5
8
>>> iterator = fibonacci(5)
>>> iterator
<generator object fibonacci at 0x10d63c550>
>>> iterator.next()
0
>>> iterator.next()
1
```

What's nice about this is so much more than fibonacci logic in a
generator function. Instead, imagine instead of a lightweight
calculation I had done something performance intensive. By using
generator expressions I can readily control the execution calls with the
iterator object's `next()` method, saving processor cycles.

Very nifty.

Summary
=======

I admit it. Like many Python developers, I find using tools like yields
and generators to optimize the heck out of performance intensive things
a lot of fun.

If you are like me and like this sort of stuff, I recommend the
following resources:

-   [Matt Harrison's Treading on Python Volume 2: Intermediate
    Python](https://www.amazon.com/Treading-Python-Volume-Intermediate/dp/149055095X/ref=tmm_pap_title_0?tag=mlinar-20)
-   [Jeff Knupp's Improve Your Python: 'yield' and Generators
    Explained](https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/)

In the next article I'll demonstrate how to use the `yield` statement
to create context managers.

**Update**: [Nicholas Tollervey](https://twitter.com/ntoll) pointed me
at wikipedia's Digital root article, so I added it to the comments of
the first code sample.

**Update**: Oddthinking pointed out that I forgot a print statement. In
the REPL it's not really needed, but if this is translated to a script
then it's necessary.
