---
date: '2024-09-18T15:30:00.926680'
published: true
tags:
  - python
  - fast.ai
  - courses
time_to_read: 5
title: "Practical Deep Learning for Coders: Lesson 0"
description: I'm going through the fast.ai course by Jeremy Howard. This is the course notes for lesson 0.
---

I'm going through the [Practical Deep Learning for Coders](http://course.fast.ai) course by Jeremy Howard. I’ll be sharing notes here on my site, all tagged with [fast.ai](https://daniel.feldroy.com/tags/fast.ai).

## About Lesson 0

This lesson is where [Jeremy Howard](https://en.wikipedia.org/wiki/Jeremy_Howard_(entrepreneur)) explains how to get the most out of his classes. He references [Meta-learning](https://rosmulski.gumroad.com/l/learn_machine_learning/blog) by [Radek Osmulski](https://radekosmulski.com/) frequently.


## How to take lessons

Follow these steps with each lesson of the [Practical Deep Learning for Coders](http://course.fast.ai) course:

1. **Watch lecture**
2. **Run notebook & experiment with the results**
   1. Play with it. Do different things  
3. **Reproduce results**
   1. Reproduce from scratch. With a fresh new notebook, can I recreate some of the models?  
4. **Repeat with a different dataset**
   1. Get own dataset and try it from scratch

Some people go through each lesson 2-3 times. It might be hard to do it the first time. That’s okay.

Once you think you understand a lesson, go through the `clean/` version of the notebooks and figure out each cell again, this time without prose or rendered outputs.

After that, complete the questionnaire. Use the questions to confirm you know every concept. If you can't answer a question, go back and learn it. 

When a lesson is 100% complete and you actually understand everyting, go to [forums.fast.ai](https://forums.fast.ai/) and announce your efforts in the "share your work" section.

## Tips and Tricks

These are from Jeremy Howard and Radek Osmulski.

* **The math in Deep Learning is matrix multiplication**. Where you multiply things together, then add them up.   
* **To get better at ML, like anything else: Practice!** Theory requires practice, practice provides context for understanding theory. So practice early and practice often. A few years ago I wrote about this concept [here](https://daniel.feldroy.com/posts/code-code-code)
* **The difference between machine learning code compared to other coding is we can generalize.** We can learn how to measure how well our code generalizes. This is in stark contrast to other types of coding where you are generally looking for very specific results.  
* **Proving ML code is accurate is really hard.** Jeremy assumes every line of ML code he writes is going to be wrong. Unlike web dev it is harder to determine if code is wrong. Make sure you have a strong baseline so it’s easy to check your work  
* **Competing in Kaggle, regardless of place, can be a great way to validate ML skills.** Even if you come in last place, you have to go through all the process of doing work as a ML engineer. Well, maybe not deployment, but everything early.  
* **Best path for winning at [Kaggle](https://www.kaggle.com/):**  
  * Start a competition early  
  * Read forums every day  
  * Make improvements to your competition set each day, this iterative process will serve as practice. [Code, code, code](https://daniel.feldroy.com/posts/code-code-code)!
  * Rinse and repeat: Early losses will serve as practice for when you are able to try to win  
* **Document process of learning in blogs, videos, and social media.** Just like any skill, including other types of coding, sets up the public footprint that you are skilled in your craft. So when people look you up, they identify you with your skills.

## References

* [Video lecture](https://www.youtube.com/watch?v=gGxe2mN3kAg&ab_channel=JeremyHoward) - Where these notes are taken from
* [course.fast.ai](http://course.fast.ai) - Lessons 1 onward
* [Book: "Meta-learning" by Radek Osmulski](https://rosmulski.gumroad.com/l/learn_machine_learning/blog)  
* [Book: "Deep Learning for Coders with fastai and PyTorch" by Jeremy Howard and Sylvain Gugger](https://www.amazon.com/Deep-Learning-Coders-fastai-PyTorch/dp/1492045527?tag=mlinar-20)

## Summary / Takeaway

My methodology for learning and teaching is similar, but Jeremy's approach focuses much more on repetition and questioning:

1. After you see a demo, you try it out yourself. 
2. You experiment, then you start from scratch and try to implement that yourself as well. 
3. You go over the lesson again, this time with only titles and code examples. 
4. Finally, you use the questionnaire to confirm if you missed a topic.

Classes I've constructed are different. They focus on repetition, but not on different versions of the lesson. Also they don't cover experimentation and play starting with lesson 1. That typically happens far into the class. 

What I find interesting is that Jeremy's approach closely matches how any decent martial art class with sparring works (Muay Thai, BJJ, fencing, kendo, HEMA, Tae Kwon Do, etc.). Typically in a class you'll learn or polish 1-2 moves, then be given specific drills to use to practice them. Then finally you might have free sparring, where if you can land the move(s) of the class it feels awesome.

I'm excited to dig into [lesson 1](https://course.fast.ai/Lessons/lesson1.html)!