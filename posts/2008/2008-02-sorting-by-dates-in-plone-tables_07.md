---
date: "2008-02-07T07:35:00.001-08:00"
description: ""
published: true
slug: 2008-02-sorting-by-dates-in-plone-tables_07
tags:
  - javascript
  - plone
  - legacy-blogger
time_to_read: 5
title: Sorting by dates in Plone tables
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/02/sorting-by-dates-in-plone-tables_07.html)_.

This is a little harder than it seems, and thats because of the 'magic' of JavaScript and how it handles alphanumeric sorts. Lets your dates are rendered thus in a table (along with some other columns):

```
January 30, 1991
April 01, 2007
March 15, 2000
July 30, 2000
```

Now a user clicks on the dates column and you've got problems:

```
April 01, 2007
January 30, 1991
July 30, 2000
March 15, 2000
```

We are still sorting alphanumerically, and not by dates! Now I could jump into the Plone JavaScript and hack a fix, but that would be lots of work and would mean I would have to be able to handle any variations on localization. Not a good thing! So instead I do this:

```
19910130 January 30, 1991
20070401 April 01, 2007
20000315 March 15, 2000
20000730 July 30, 2000
```

As you can see, sorts will be accurate (albeit ugly). The way to fix the ugliness is to put a span around the ugly part and give it a style of 'display:none;'.

_But why not just use the unformatted date like 2000/01/01 instead of a format without slashes?_

Good question. The reason is that the Plone JavaScript has problems with forward slashes. You'll start seeing funny errors in your sorts, such as dates set in July 2000 showing up before items in June 2000. I think the JavaScript is evaluating (numbers with slashes and then sorting them as shown in this case:

```
2000/03/15 March 15, 2000 = 44 March 15, 2000
2000/07/30 July 30, 2000 = 7 July 30, 2000
```

Hence you see the mad purpose of my fix and also what happens with loosely typed languages if you are not careful.
