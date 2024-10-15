---
date: '2013-03-02'
published: true
slug: we-are-not-using-paypal
tags:
- twoscoops
- python
- django
- rant
time_to_read: 5
title: We are not using PayPal
---

In January [Audrey Roy](https://audrey.roygreenfeld.com) and I launched a
[book](https://roygreenfeld.com/products/two-scoops-of-django-1-5) about Django called [Two Scoops of
Django: Best Practices for Django 1.5](https://roygreenfeld.com/products/two-scoops-of-django-1-5). We
decided to not use PayPal. Here's why:

Open Source Events Get Burned By PayPal
=======================================

PayPal has a long, sordid history of freezing the accounts of Python
related conferences and events around the world. In fact, this article
was born out of the fact [DjangoCon Europe 2013 had its PayPal account
frozen](https://blog.djangocircus.com/post/43806402173/back-on-track). In
the past, [DjangoCon Europe 2012](https://2012.djangocon.eu/), Plone
Conferences 2008, 2011, and at least one PyCon Australia dealt with the
same PayPal problem (DjangoCon 2013 was forewarned and took measures to
protect itself). We also have unconfirmed reports of other Python and
Django events also running into problems with PayPal freezing accounts.
Going with just confirmed conferences having issues with PayPal, this is
a combined total of assets in excess of over US$100,000 dollars.

It's not just a Python issue either, it's an issue that [strikes other
open source languages and
tools](https://conferencesburnedbypaypal.tumblr.com/). It's at the point
now where [conference organizers don't trust
PayPal](https://aralbalkan.com/3898/) and make a point telling each other
to use alternative payment gateways.

Fear, Shame, and PayPal
=======================

The terrifying thing to consider is that I suspect that the number of
technical conferences affected by PayPal freezes is much, much larger.
My reasoning is that **most conferences keep quiet about it** because
**they're afraid that raising a fuss will annoy PayPal's anti-fraud
division**. Let's also face the fact that **most people feel ashamed
when bank accounts they are responsible for get frozen**, so probably
don't publicize the issue.

The usual way conferences deal with these lockouts is conference
organizers beg and borrow from friends, family, take second mortgages,
local banking institutions, and pray that PayPal will eventually free
their account. When you deal with a hostile, inaccessible payment
gateway who won't let you provide for the hundreds or even thousands of
people who paid you their hard earned money, it's the only way to get
by.

The 'Needs' of PayPal's Anti-Fraud Division
==============================================

While I could respect the needs of PayPal's anti-fraud division when
dealing with non-fungible products like ticket sales, it's **simply
unacceptable** that prominent conferences for open source projects are
treated this way.

The software represented by these conferences drives the modern
e-commerce world, including the myriad of systems that use PayPal to
process sales. Yet PayPal continues to burn open source conferences year
after year, and we've never heard of any conference outreach by their
so-called 'developer evangelists' when a conference's account is
frozen.

Legal recourse against PayPal is folly
======================================

Ask any lawyer and they'll basically say against PayPal you have no
options. PayPal has an army of lawyers and in most places isn't a bank,
meaning your course of action is constrained from the beginning by your
agreeing to PayPal's Terms of Service (TOS). Also, in the United
States, their TOS prevents you from joining a class action lawsuit
against them. Whether or not that TOS clause is enforceable in court,
the fact that it is in their TOS greatly reduces any faith I might have
had in them because it paints a picture of a company hostile to my
needs.

In talking to authors and entrepreneurs, we've just heard (and read)
too many horror stories. For merchants of non-fungible goods such as
digital goods like the e-book I co-authored, PayPal seems even less
trustworthy.

Which means using PayPal places us at an unacceptable risk. We simply
don't have the deep pockets to deal with PayPal freezing our funds for
sales lost from a more reliable distribution system such as
[Stripe](https://stripe.com) that powers our sales through
[Gumroad](https://gumroad.com).

It is Wrong to Use PayPal
=========================

Considering PayPal's unacceptable behavior in regards to the open
source community I love and merchants who try to work in their system, I
feel it is wrong to support PayPal. Audrey agrees, and so our policy of
not using PayPal to sell the book is set.

PayPal is at Risk
=================

There was a day when Microsoft had what seemed to be an unassailable
lock on the commercial software world. On many levels, Microsoft is a
shadow of its former self, and I contend it wasn't just Apple's
competition. Instead, Microsoft's contempt for their own customers and
the developer community hurt them just as much.

PayPal is on the same path of self-destruction. The've gone from the
[scrappy
company](https://www.amazon.com/The-PayPal-Wars-Battles-Planet/dp/0977898431/?tag=ihpydanny-20)
helping people grow their business to the monolithic overlord that kills
businesses and well-meaning events.

PayPal's demise won't happen this year, or the next, but every time
they damage their customer base and the developer community it's
another nail in the coffin. I submit that unless PayPal changes its
ways, within 5 years PayPal will be a shadow of its former self as the
army of growing competitors such as [Stripe](https://stripe.com),
[Balanced Payments](https://www.balancedpayments.com/),
[wepay](https://www.wepay.com/), and
[Payoneer](https://www.payoneer.com/) expands their availability and
options around the world.

What PayPal Can Do for Conferences
==================================

PayPal does have to worry about ticket sales for bogus events, since
that separates people from their money, but identifying real conferences
is easy:

1.  PayPal developer evangelists and community managers need to track
    every valid developer event in the world. It's the job of people in
    these roles to have the connections and subject matter expertise to
    identify real events from fake ones.
2.  PayPal needs to sponsor these events. Why? See point #3.
3.  PayPal's anti-fraud division needs to be informed that any PayPal
    sponsored event is off-limits.

What PayPal Can Do for Small Business
=====================================

PayPal has its developer evangelists, community managers, and marketing
departments working hard. However, at the end of the day, if you treat
your customers with disrespect and a lack of trust, none of that
matters. Bad press and market forces will see their revenues drop as
customers will migrate to solutions that are more trustworthy and less
antagonistic.

I believe that PayPal needs to revise how its anti-fraud division
communicates with people who have frozen accounts. They need to change
the adversarial pose they take with their own customers to one that is
collaborative.

Note
====

If this makes you angry as it did me, take a deep breath and step back.
I've found [this
book](https://www.amazon.com/gp/product/0807012394/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=0807012394&linkCode=as2&tag=ihpydanny-20)
recommended by my friend Randall Degges useful in getting back on track
and staying productive.
