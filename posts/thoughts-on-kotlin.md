---
date: "2019-11-07"
description: My notes and impressions about this Android-friendly JVM language.
published: true
slug: thoughts-on-kotlin
tags:
  - kotlin
  - hackathon
time_to_read: 10
title: Thoughts on Kotlin
type: post
---

This past weekend Audrey and I competed in the Los Angeles edition of the [Tech to Protect Challenge](https://www.techtoprotectchallenge.org/) hackathon. It was fun, we came up with ideas to increase people's safety, talked to first responders, and learned how to build Android apps with [Kotlin](https://kotlinlang.org/). We won in our [category](https://www.techtoprotectchallenge.org/contest/contest-005/), but that's a blog post for another day.

This blog post contains my notes on [Kotlin](https://kotlinlang.org/).

# Variable Declaration

Kotlin has two variable types, mutable and immutable. You distinguish between them by defining them with `val` for immutable and `var` for mutable. You can specify type, but Kotlin can infer type based on how you declare it.

```kotlin
// immutables
val a = "I am an immutable string"
val b:String = "I am an immutable string with an explicit declared type of String"

// mutables
var c = "I am a mutable string"
var d:String = "I am an string with an explicit declared type of String"
```

# Char vs String / Single Quotes vs Double Quotes

This caught me completely off-guard. Especially as I prefer using single quotes. It's one less key to press on the US keyboard.

You see, unlike Python and Javascript, Kotlin differentiates between `Char` and `String` types. In simplest terms, a `Char` must have a single character and is surrounded by single quotes and `String` has zero to many characters and is surrounded by double quotes.

```kotlin
// Char example, throws an error if variable has more than 1 character
val singleLetterVariable:Char = 'a'

// String examples
val emptyString:String = ""
val singleLetterVariable2:String = "b"
val manyLettersVariable:String = "Learning is fun"
```

# When Instead of Switch/Case

[Python doesn't have a switch or case statement](/why-doesnt-python-have-switch-case.html), and neither does Kotlin. Instead it has a `when` keyword that very much shortens the dialogue necessary for branch control. Rather than using this traditional switch/case style code:

```javascript
function numberToString(argument) {
  switch (argument) {
    case 0:
      return "zero";
    case 1:
      return "one";
    case 2:
      return "two";
    default:
      return "nothing";
  }
}
```

In Kotlin you describe it thus with [when](https://kotlinlang.org/docs/reference/control-flow.html#when-expression):

```kotlin
fun numberToString(number: Int): String {
 when(number) {
   0 -> return "zero"
   1 -> return "one"
   2 -> return "two"
   else -> return "nothing"
 }
}
```

This syntax is is concise and powerful. In fact, there's a lot of [syntactical sugar](https://superkotlin.com/kotlin-when-statement/) I'm not covering.

# General Control Flow

There's a lot of similarity with other languages:

- `if/else/else if` keywords.
- `for` loops
- `while`
- `do while`

# Data Classes

Just as Python has [Dataclasses](https://docs.python.org/3/library/dataclasses.html), Kotlin comes with a similar, more constrained [Data Class](https://kotlinlang.org/docs/reference/data-classes.html):

```kotlin
>>> // Define the data class
>>> data class Baby(val name: String, val age: Int, val ageType: String)
>>> // Instantiate and display the result
>>> val daughter = Baby(name="Uma", age=10, ageType="months")
>>> println(daughter.name)
Uma
```

# MutableMaps as Python/Javascript-Style Key/Value Structures

One thing I dislike about Java is while there are many ways to do key/value structures, none of them fit my brain like Python dictionaries or Javascript objects. Mutable maps are the closest thing to what I prefer, and Kotlin has it as a stdlib function called [mutableMapOf](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/mutable-map-of.html) to support it:

```kotlin
>>> val daughter = mutableMapOf("name" to "Uma", "age" to 10, "ageType" to "months")
>>> println(daughter["name"])
Uma
```

# Summary

What I like about Kotlin is that it follows pretty standard syntactic patterns, there's no wheels being reinvented. Even the [when](#when-instead-of-switch-case) statement is pretty straightforward. While there's quirks such as the use of [single quotes with the Char type](#char-vs-string-single-quotes-vs-double-quotes), nothing makes me want to bang my head against the wall. Instead, I was productive in minutes upon first looking at the language.

[![image](/images/thoughts-on-kotlin.png)](/thoughts-on-kotlin.html)
