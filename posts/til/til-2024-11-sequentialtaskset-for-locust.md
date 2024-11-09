---
date: '2024-11-09T00:00:00.429101'
description: How to get Locust to not bash your server like a robot.
image: /public/logos/til-1.png
published: true
tags:
- TIL
- Python
- load testing
title: 'TIL: SequentialTaskSet for Locust'
twitter_image: /public/logos/til-1.png
---

`SequentialTaskSet` makes it so Locust tasks happen in a particular order, which ensures your simulated users are clicking around in a more human manner at a more human pace. Attribution goes to Audrey Roy Greenfeld.

You can see it in action in the now updated [previous entry on the topic of Locust for load testing](https://daniel.feldroy.com/posts/2024-11-using-locust-for-load-testing).
