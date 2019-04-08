---
layout: cvmp-default
title: Previous Years
---


<ul>
    {% for year in site.data.cvmp.previous-years %}
        <li> 
            <a href="{{site.url}}/{{year}}"> {{site.data.cvmp[year].title}} </a> 
        </li>      
    {% endfor %}
</ul>
