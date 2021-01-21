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

    <li> <a href="http://egsr2019.icube.unistra.fr/"> The 30<sup>th</sup> <b>Eurographics Symposium on Rendering</b> </a> </li>
    <li> <a href="https://cg.ivd.kit.edu/egsr18/"> The 29<sup>th</sup> <b>Eurographics Symposium on Rendering</b> </a> </li>
    <li> <a href="http://egsr2017.aalto.fi/"> The 28<sup>th</sup> <b>Eurographics Symposium on Rendering</b> </a> </li>

</ul>
