---
permalink: /live/
layout: egsr-default
title: Live
year: 2020
---
<title>EGSR2020 Live Stream (redirect)</title>


<script type='text/javascript'>
function redirect(){
	var currentTime = new Date();

	{% assign sessions = site.session | sort: 'start' %}
	{% for mySession in sessions %}
		var sessionStart = new Date("{{mySession.start}}");

		sessionStart.setMinutes(sessionStart.getMinutes() - 5);
		var sessionEnd = new Date("{{mySession.end}}");

		if (currentTime >= sessionStart && currentTime < sessionEnd)
		{
			window.location.replace("{{mySession.youtube_url}}");
			return;
		}
	{% endfor %}
		window.location.replace("https://www.youtube.com/channel/UCinRAYhpuuQ1K3UVlSToOMA");
}
redirect();
</script>
