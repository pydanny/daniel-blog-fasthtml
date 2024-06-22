---
date: '2011-05-26T05:40:00.000-07:00'
description: ''
published: true
slug: 2011-05-python-http-requests-for-humans
tags:
- rant
- python
- legacy-blogger
time_to_read: 5
title: Python HTTP Requests for Humans
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2011/05/python-http-requests-for-humans.html)*.

Ever try to use [Python's](https://python.org/) standard library for doing a [POST](https://en.wikipedia.org/wiki/POST_(HTTP))? Or a [GET](https://en.wikipedia.org/wiki/GET_(HTTP)),&nbsp;[PUT](https://en.wikipedia.org/wiki/PUT_(HTTP)), or [DELETE](https://en.wikipedia.org/wiki/DELETE_(HTTP))? What about when you have to deal with&nbsp;[HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication)?

In a word, ugh.

Let's face it, this is one part of Python that is really not for human consumption. While there are a million things you can do with things like&nbsp;[urllib](https://docs.python.org/library/urllib.html),&nbsp;[urllib2](https://docs.python.org/library/urllib2.html),&nbsp;[socket](https://docs.python.org/library/socket.html),&nbsp;[urlparse](https://docs.python.org/library/urlparse.html), the fact of the matter is that implementing anything beyond <b>urllib.urlopen()</b> is a matter of diving into arcane APIs.

Sure, thanks to works like [Doug Hellmann's Python Module of the Week](https://www.doughellmann.com/PyMOTW/)&nbsp;and [Michael Foord's documentation of urllib2](https://www.voidspace.org.uk/python/articles/urllib2.shtml)&nbsp;the problem isn't unsurmountable. Unfortunately, the eclectic mix of libraries and weird APIs means when you have to revisit your code in a few months your code feels like spaghetti.

Do you doubt me?

<pre class="prettyprint lang-py"># This sample gleefully taken from https://gist.github.com/973705

import urllib2

gh_url = 'https://api.github.com'
gh_user= 'user'
gh_pass = 'pass'

req = urllib2.Request(gh_url)

password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, gh_url, gh_user, gh_pass)

auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
opener = urllib2.build_opener(auth_manager)

urllib2.install_opener(opener)

handler = urllib2.urlopen(req)

print handler.getcode()
print handler.headers.getheader('content-type')

# ------
# 200
# 'application/json'</pre>
Really?

This much code to make a simple HTTP GET request with some auth?!?

<b>Really?!?</b>

This is a debugging nightmare! Especially when you have to deal with complex service APIs provided by Paypal, Amazon, Google, Authorize.net, and a million other systems.

I bet I could earn a decent living by charging Pythonistas a buck each time they took the shortcut of doing HTTP actions in the shell via curl or wget. 

Anyway, wouldn't it be great if we could just call a single function with the URL and auth data as parameters? And that the same dialogue would exist for GET, POST, PUT, DELETE or whatever? Wouldn't that be just plain wonderful? If only we could have that functionality in Python!!!

Fortunately for us, we do have that functionality courtesy of [Kenneth Reitz](https://kennethreitz.com/)'s [Requests](https://pypi.python.org/pypi/requests) library! Our verbose code sample above becomes the wonderfully terse and easy-to-memorize script as shown below:

<pre class="prettyprint lang-py"># This sample joyfully taken from https://gist.github.com/973705

import requests

r = requests.get('https://api.github.com', auth=('user', 'pass'))

print r.status_code
print r.headers['content-type']

# ------
# 200
# 'application/json'</pre>
Want to do a post with data? Try this:

<pre class="prettyprint lang-py"># This example cooked up by me!

import requests
post_data = {"amount":10000, "service":"writing blog posts"}

r = requests.post('https://example.com/api', post_data, auth=('user', 'pass'))

print r.status_code
print r.headers['content-type']

# ------
# 200
# 'application/json'</pre>
The [Requests](https://github.com/kennethreitz/requests) library is still young, but I've yet to run into any bugs or undocumented edge cases. The [documentation is awesome](https://docs.python-requests.org/en/latest/index.html), but you don't really need it at all. The library is intuitive, fun, and and there is clearly one way to do.

---

## 8 comments captured from [original post](https://pydanny.blogspot.com/2011/05/python-http-requests-for-humans.html) on Blogger

**Argentino said on 2011-05-26**

What about httplib2. I think it's pretty straightforward too.

**Douglas Camata said on 2011-05-26**

There's a similar API that can be used for http requests named Restfulie. It was made originally to work with RESTful and hypermedia resources, but it can handle simple requests as well in a simple and intuitive. 

And if you want, it can convert the response into Python objects (by default, only xml and json, but  you can add your own converters) and can convert the kwargs to request parameters (again, by default only to xml or json, but you can add your own converters).

Just converting the examples shown here to Restfulie:

response = Restfulie.at('https://api.github.com').auth('user', 'pass').get()
response.body
response.code
response.headers
# if you want it as an object
response_as_object = response.resource()

response = Restfulie.at('https://example.com/api').auth('user', 'pass').post(amount=1000, service=&quot;writing blog posts&quot;)
response.body
response.code
response.headers
# if you want it as an object and the content-type is application/json, Restfulie figures it out and use the right converter
response_as_object = response.resource()

If you want more information, like how to interact with hypermedia, please visit the project's page at github: https://github.com/caelum/restfulie-py

**Unknown said on 2011-05-26**

Faced the same problem with Ruby's NetHTTP. Tried to solve it in a way that wouldn't leave my eyes bleeding. See this [example](https://github.com/kaiwren/wrest/blob/master/examples/delicious.rb) demonstrating using the Delicious api.

**Rach said on 2011-05-26**

While the requests project looks interesting, it seems a little disingenuous for the project's author to compare usage snippets with appears to be a purposely inflated LoC count in the urllib2 case.

[That said it wouldn't make the urllib2 case much better if, for example, gh_url/gh_user/gh_pass were inlined as in the requests example.]

Would love to see a comparison to other libraries by someone with the experience too(not me :( ), with feature comparisons.  Like voidspace did with his mock comparison.

**Aramgutang said on 2011-05-26**

Another great &quot;feature&quot; of the requests library is that its developers are friendly and responsive. I submitted a pull request fixing a bug in cookie handling, and it was merged in within an hour (and they even added me to AUTHORS just for a 2-line change).

**pydanny said on 2011-05-27**

@Argentino - I've used httplib2 quite a bit but do not care for its API or response objects. It isn't intuitive. Tuples for the response? Why not an object like requests?

@Douglas Camata - Restfulie looks pretty neat - especially how it handles response objects. That said, I'm not so sure about the API. It is interesting that you fire it off with a .get() or .post() method, but the rest just seems a bit cumbersome.

@klotz - You raise a good point, in that it seems like Requests only allows dicts of data to be encoded. Seems like it should also accept a string, right?

@Rach - I'll see if I can come up with a good follow up post to demonstrate how the various libraries do this sort of thing. Maybe next week...

**Argentino said on 2011-05-27**

@pyDanny
I don't mind about doing:

resp, content = h.request(&quot;https://example.org/&quot;, &quot;GET&quot;)

But i agree that an object is much nicer.

thanks and nice post. ;-)

**andry said on 2011-11-11**

very good tutorial and can hopefully help me in building json in the application that I created for this lecture. thank you

