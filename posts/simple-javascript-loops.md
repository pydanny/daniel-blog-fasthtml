---
date: "2021-08-01"
published: true
slug: javascript-loops-are-fun
tags:
  - javascript
  - cheatsheet
  - tutorial
time_to_read: 5
title: "JavaScript Loops Are Fun!"
description: This tutorial is a cookbook of my favorite JavaScript looping techniques.
---

This tutorial is a cookbook of my favorite JavaScript looping techniques and to a lesser degree, object introspection. It should prove useful to anyone new to JavaScript, especially if you are coming from languages with `for...in` (python in particular). 

I'm doing this in my browser JavaScript console.

## Looping for values

Looping through elements of an array is easy in JavaScript. Use `for...of`!

``` javascript
> let arr = [5, 10, 15, 20]
> for (let i of arr){
    console.log(i)
  }
5
10
15
20
```

`for...of` returns the value of the loop iteration. It's the right tool for this operation.

# Looping for index

If you need to track the index of a loop, do this:

``` javascript
> for (let i=0; i < arr.length; i++){
    console.log(i)
  }
0
1
2
3
```

This technique is reliable and acts predictably. I've heard that this method runs more quickly than `for...of`, but JavaScript is very fast these days. Any slowdowns your code might have is probably due to latency or other bottlenecks rather than which JavaScript looping technique you choose to implement.

## What's the difference between `for...of` and `for...in`?

Let's use both techniques on the same array and see what we get. First, the `for...of` combination:

``` javascript
> let arr = [5, 10, 15, 20]
> for (let i of arr){
    console.log(i)
  }
5
10
15
20
```

Now, the `for...in` combination, **which isn't recommended**:

``` javascript
> let arr = [5, 10, 15, 20]
> for (let i in arr){
    console.log(i)
  }
0
1
2
3
```

It appears that `for...in` returns the index of the loop iteration, right? What's wrong with that? 

Read on!

## Problems using `for...in` with arrays

`for...in` can fool you into thinking it's the right tool for iterating over arrays for indexes instead of the more verbose approach of `(let i=0; i < arr.length; i++)`. This appeared to work:

``` javascript
> let arr = [5, 10, 15, 20]
> for (let i in arr){
  console.log(i)
}
0
1
2
3
```

But let's change things up a bit with some prototype manipulation:

``` javascript
> Array.prototype.icecream = function(){
  console.log("Ice cream!")
}
> let arr = [5, 10, 15, 20]
> arr
(4) [5, 10, 15, 20]
```

The array has been proven to have four elements. Now let's iterate over the array using `for...in`:

``` javascript
> for (let i in array){
  console.log(i)
}
0
1
2
3
icecream
```

Where did the `icecream` value come from? `icecream` function wasn't in the array but `for...in` called it anyway. What just happened?!?

What's going on is that the `for...in` is enumerating over the **properties** of the array, not the values or index. Even if you avoid using prototypes, the same cannot be said for any library installed from NPM. Finally, there is no guarantee that the elements will be returned `for...in` in numeric order.

## What about `forEach` loops?

The `forEach` loop requires a callback, making it a slightly advanced enough method of writing for loops in JavaScript. I'll cover that in a future article.

## Summary  

1. Use `for...of` for iterating over the values of an array.
2. Use `(let i=0; i < arr.length; i++)` for enumerating over the index of an array.
3. Avoid using `for...in` for iterating over arrays in any capacity.
