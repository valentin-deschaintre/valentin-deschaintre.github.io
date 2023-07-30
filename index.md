---
permalink: /
title: 'Valentin Deschaintre'
layout: main
---

<script>
window.onload = choosePic;

var myPix = new Array("img/profilePic1.jpg","img/profilePic2.png","img/profilePic3.jpg");

function choosePic() {
     var randomNum = Math.floor(Math.random() * myPix.length);
     document.getElementById("myPic").src = myPix[randomNum];
};
</script>

<div id='content'>
	<table width="100%">
		<tr>
			<!-- The picture -->
			<td style="text-align: left; " valign="bottom">
				<img src="img/placeholder.jpg" id="myPic" width='250' alt="My picture">
			</td>

			<!-- Name and contact -->
			<td valign="top">
				<table>
					<tr>
						<td align="center"><h1>Valentin Deschaintre</h1></td>
					</tr>
					<tr>
						<td align="center">Research Scientist - Adobe Research</td>
					</tr>
					<tr>
						<td align="center"><div class="email" cellpadding="10">e-mail: <a href="mailto:deschain@adobe.com">deschain[at]a***e.com</a></div>
						</td>
					</tr>
					<tr>
						<td align="center"><a href="https://scholar.google.com/citations?user=UnO0Ap8AAAAJ&hl=en"><img src='img/google-scholar-logo.png' width='32' height='32' alt='Google scholar'/></a> <a href="https://github.com/valentin-deschaintre"><img src='img/github-mark.svg' width='32' height='32' alt='Github'/> </a><a href="https://www.linkedin.com/in/valentin-deschaintre-phd-75226948/?locale=en_US"><img src='img/linkedin-logo.png' width='32' height='32' alt='Linkedin'/></a> <a href="https://twitter.com/vdeschaintre"><img src='img/twitter_logo.png' width='32' height='32' alt='D19'/></a> <a rel="me" href="https://mastodon.gamedev.place/@vdeschaintre"><img src='img/mastodon-black-icon.svg' width='32' height='32' alt='Mastodon'/></a>
						</td>
					</tr>
				</table> 
			</td>
		</tr>
	</table>
	<br/>
	<div class="Introduction">
		I am currently a Research Scientist at Adobe Research in the London lab. I previously was an Associate Researcher in the <a href="http://wp.doc.ic.ac.uk/rgi/">Realistic Graphics and Imaging group</a> of Imperial College London hosted by <a href="https://www.doc.ic.ac.uk/~ghosh/">Abhijeet Ghosh</a>.
		I received my PhD at Inria Sophia-Antipolis from the GraphDeco research group under the supervision of <a href='https://www-sop.inria.fr/members/Adrien.Bousseau/'>Adrien Bousseau</a> and <a href='https://www-sop.inria.fr/reves/George.Drettakis'>George Drettakis</a> in collaboration with Optis, an Ansys affiliate. My Thesis received the French Computer Graphics Thesis Award 2020 and UCA Academic Excellence Thesis Award 2020<br>
		During my PhD, I spent 2 great months in MIT under the supervision of <a href='https://people.csail.mit.edu/fredo/'>Fr&eacute;do Durand</a>, at MIT CSAIL. <br> 
		<b>My research focuses on inverse rendering, with a special focus on appearance acquisition, creation, editing and representation for virtual environments.</b> <br><br>

		
		
	</div>
	<h3>Internships</h3>
	<div class="Introduction">
		<b>Adobe Research Internship:</b> I will be looking for strong PhD students to collaborate with for the 204 Adobe internship program. If you are interested in interning at Adobe with me (see my research interests above), don't hesitate to reach out (deschain@a***e.com) detailing what your research interests are, and what you would like to work on during the internship. <br><br>	
	</div>
	<h3>Past Interns</h3>

	<div class="Introduction">
		In recent years, I was happy to collaborate with great students in the context of Adobe's PhD Internship program!
		<ul>
			<li><a href='http://webdiis.unizar.es/~juliagv/'>Julia Guerrero-Viu (Universidad de Zaragoza): 2023</a></li>
			<li><a href='https://rubenwiersma.nl//'>Ruben Wiersma (Delft University): 2023</a></li>
			<li><a href='https://prafullsharma.net/'>Prafull Sharma (MIT): 2022</a></li>
			<li><a href='https://yiweihu.netlify.app/'>Yiwei Hu (Yale University): 2021, 2022</a> (Now at Adobe)</li>
		</ul>
	</div>
	<h3>Publications</h3>
	<div class="Publications list">
		{% for paper in site.data.publications.papers %}
			<div class='thumb image'>
			<div style='padding-top:0px'><a href='{{paper.website_link}}'>
				<img src='{{paper.square_teaser}}' width='100' height='90'/></a>
			</div>
		</div>
		<div class='ref'>
			<div class='title'>
				<a href="{{paper.website_link}}">
					{{paper.title}}
				</a> &nbsp; 
				{% if paper.paper_link %}
				<a href="{{paper.paper_link}}"><img class='doc' src='img/pdf.png' width='19' height='19' alt='Paper'/></a>
				{% endif %}
				{% if paper.poster_link %}
				<a href="{{paper.poster_link}}"><img class='doc' src='img/pdf.png' width='19' height='19' alt='Poster'/></a>
				{% endif %}
				{% if paper.presentation_link %}
				<a href="{{paper.presentation_link}}"><img class='doc' src='img/ppt.png' width='19' height='19' alt='Presentation'/></a>
				{% endif %}
				{% if paper.youtube_link %}
				<a href="{{paper.youtube_link}}"><img class='doc' src='img/yt.jpg' width='20' height='19' alt='Youtube presentation' /></a>
				{% endif %}

			</div>
			<div class='authors'>
				{% for author in paper.authors %}
				{% assign authorDet = site.data.people[author] %}
				{% if authorDet and author != paper.authors.last %}
					<a href='{{authorDet.website}}'>{{authorDet.name}},</a>
				{% elsif authorDet and author == paper.authors.last %}
					<a href='{{authorDet.website}}'>{{authorDet.name}}</a>
				{% else %}
					{{author}}
				{% endif %}
				{% endfor %}
			</div>
			{% if paper.miscs %}
			<div>
			<ul>
				{% for misc in paper.miscs %}
				<li>{{misc}}</li>
				{% endfor %}

			</ul>
			</div>
			{% endif %}

			<div class='conf'>
				{{paper.citation}}
			</div>
		</div>
		{% if paper != site.data.publications.papers.last %}
		<hr />
		{% endif %}
			
			
		{% endfor %}

	</div>
	
	<h3>Presentations</h3>
	<div class="Publications list">
		
		<div class='thumb image'>
			<div style='padding-top:13px'><a href='http://egsr2019.icube.unistra.fr/program.html'>
				<img src='img/teaserTalkMam.PNG' width='67' height='60' alt='D19'/></a>
			</div>
		</div>
		
		<div class='ref'>
			<div class='title'>
				Discussion: Research and questions in neural methods for material acquisition
				<a href="files/mamTalk/MAM_19_NeuralNetDiscussion.pptx"><img class='doc' src='img/ppt.png' width='19' height='19' alt='MAM_19_NeuralNetDiscussion.pptx' /></a>
			</div>
			<div class='authors'>
				<a href='https://valentin.deschaintre.fr'>Valentin Deschaintre</a>,
			</div>
			<div class='conf'>
				Workshop on Material Appearance Modeling, jul 2019
			</div>
		</div>
		<div class="interYear">&nbsp;</div>
	</div>
	
	<h3>Community activities</h3>
	<ul>
		<li>Committee member: <a href="https://research.siggraph.org/">SIGGRAPH Research Career Development Committee, Siggraph Thesis Fast Forward Steering Committee</a>, <a href="https://www.cvmp-conference.org/2022/">Industry Chair CVMP 2022</a> </li>
		<li>Program commitee member: <a href="https://www.cvcs.no/">CVCS 2020</a>, <a href="https://egsr.eu/2021/">EGSR 2021</a>, <a href="https://egsr.eu/2022/">EGSR 2022</a>, <a href="https://conferences.eg.org/egsr2023/">EGSR 2023</a>, <a href="https://eg2023.saarland-informatics-campus.de/">Eurographics 2023</a>, <a href='https://asia.siggraph.org/2023/submissions/technical-papers/'>Siggraph Asia 2023</a></li>
		<li>Journal Reviewer: <a href="https://dl.acm.org/journal/tog">Transactions On Graphics</a>, <a href="https://www.computer.org/csdl/journal/tg">TVCG</a>, <a href="https://onlinelibrary.wiley.com/journal/14678659">CGF</a>, <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=34">IEEE TPAMI</a>, <a href="https://www.journals.elsevier.com/graphics-and-visual-computing">Graphics and Visual Computing</a></li>
		<li>Tertiary Reviewer: <a href="https://sa2020.siggraph.org/">Siggraph Asia 2019, 2020, 2021, 2022</a>, <a href="https://s2022.siggraph.org/">Siggraph 2020, 2021, 2022, 2023</a>, <a href="https://conferences.eg.org/eg2021/">Eurographics 2020, 2021, 2022</a>, <a href="http://iccv2021.thecvf.com/home">ICCV 2021</a>, <a href="https://cvpr2022.thecvf.com/">CVPR 2022</a></li>
		<li>Website administrator and volunteer <a href="https://egsr2020.london/">EGSR 2020</a></li>
	</ul>

</div>
