---
layout: egsr-twitter
title: Previous Years
---

<ul>
    {% for year in site.data.egsr.previous-years %}
        <li> 
            <a href="{{site.url}}/{{year}}"> {{site.data.egsr[year].title}} </a> 
        </li>      
    {% endfor %}
</ul>
