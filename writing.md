---
layout: writing
title: "My Works"
---

<h2>Welcome to My Writing Collection</h2>
<ul>
  {% for post in site.posts %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date: "%B %d, %Y" }}</li>
  {% endfor %}
</ul>
