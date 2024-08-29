---
date: '2010-05-11T12:14:00.003-07:00'
description: ''
published: true
slug: 2010-05-using-modernizr-to-help-with-canvas
tags:
- canvas
- javascript
- HTML5
- legacy-blogger
time_to_read: 5
title: Using modernizr to help with canvas
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2010/05/using-modernizr-to-help-with-canvas.html)*.

On my current project I've been using a little bit of the [HTML5](https://en.wikipedia.org/wiki/HTML5)&nbsp;[Canvas element](https://en.wikipedia.org/wiki/Canvas_element) to provide a little bell/whistle. However, the problem with Canvas is that not all browsers support it. Out of the box though Canvas gives you a quick and handy way of dealing with that problem:

<pre class="prettyprint lang-html">&lt;div id="content"&gt;
    &lt;div id="demo-space-wrapper"&gt;
        &lt;canvas height="100" id="demo-space" width="100"&gt;
            This text is displayed if the client browser does not support HTML5 Canvas.
        &lt;/canvas&gt;
    &lt;/div&gt;
&lt;/div&gt;
</pre>
The problem with this approach is that if your layout expects to have an object there and your client's use of Internet Explorer doesn't include the Canvas extension then this could damage the overall feel of your layout.

And that is where [Modernizr](https://www.modernizr.com/) comes in to play. It is a trivial to use JavaScript library that makes it possible to detect if a browser can use Canvas or any other HTML control. So what I did was take the [Modernizr Canvas detection documentation](https://www.modernizr.com/docs/#canvas) and apply it to my JavaScript. With that in hand I wrote this:

<pre class="prettyprint lang-js">// check for canvas
if (Modernizr.canvas) {
    // We have canvas so add a rectangle
    var demospace = document.getElementById('demo-space');
    var context = demospace.getContext('2d');
    context.fillStyle = "rgb(255,0,0)";
    context.fillRect(10, 10, 10, 10)            
} else {
    // No canvas. Remove the layout space to preserve the layout.
    var ul = document.getElementById('content');
    var li = document.getElementById('demo-space-wrapper');
    ul.removeChild(li);
};
</pre>