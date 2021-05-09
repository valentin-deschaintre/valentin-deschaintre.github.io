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
						<td align="center"><a href="https://scholar.google.com/citations?user=UnO0Ap8AAAAJ&hl=en"><img src='img/google-scholar-logo.png' width='32' height='32' alt='Google scholar'/></a> <a href="https://github.com/valentin-deschaintre"><img src='img/GitHub-Mark-32px.png' width='32' height='32' alt='Github'/> </a><a href="https://www.linkedin.com/in/valentin-deschaintre-phd-75226948/?locale=en_US"><img src='img/linkedin-logo.png' width='32' height='32' alt='Linkedin'/></a> <a href="https://twitter.com/vdeschaintre"><img src='img/twitter_logo.png' width='32' height='32' alt='D19'/></a>
						</td>
					</tr>
				</table> 
			</td>
		</tr>
	</table>
	<br/>
	<div class="Introduction">
		I am currently a Research Scientist at Adobe Research in the London lab. I previously was an Associate Researcher in the <a href="http://wp.doc.ic.ac.uk/rgi/">Realistic Graphics and Imaging group</a> of Imperial College London hosted by <a href="https://www.doc.ic.ac.uk/~ghosh/">Abhijeet Ghosh</a>.
		I did my PhD at Inria Sophia-Antipolis in the GraphDeco research group under the supervision of <a href='https://www-sop.inria.fr/members/Adrien.Bousseau/'>Adrien Bousseau</a> and <a href='https://www-sop.inria.fr/reves/George.Drettakis'>George Drettakis</a> in collaboration with Optis, an Ansys affiliate.<br>
		During my PhD, I had the pleasure to spend 2 months in MIT under the supervision of <a href='https://people.csail.mit.edu/fredo/'>Fr&eacute;do Durand</a>, at MIT CSAIL. <br> 
		My research focuses on material and shape (appearance) acquisition, creation, edition and representation, leveraging deep learning methods. <br><br>
		<b>Adobe Research Internship:</b> I will be looking for strong PhD students to collaborate with for the 2022 Adobe internship program. If you are interested in interning at Adobe with me, send me an email (deschain@a***e.com) detailing what your research interests are, and what you would like to work on during the internship. <br><br>

		<!--My PhD was funded by the French government (ANRT and Inria) and Optis, an Ansys affiliate using the <a href='https://www.ifsttar.fr/en/partnerships-innovation/scientific-and-technical-services/cifre-industrial-agreements-for-training-through-research/'>CIFRE</a> system of collaboration.<br><br>
		
		<img src='img/new.gif' alt='new'/> I am happy to share that my  <a href="#thesis">thesis</a> was awarded the <a href = 'https://gdr-igrv.icube.unistra.fr/index.php/Prix_de_th%C3%A8se_du_GdR_IG-RV'>French Computer Graphics and Geometry Thesis award</a>! This award is delivered by the <a href="https://gdr-igrv.icube.unistra.fr/index.php/Accueil">GDR IG-RV</a> in collaboration with AFIG, AFRV and EG French chapter.<br>
		<img src='img/new.gif' alt='new'/> My <a href="#thesis">thesis</a> was also awarded the <a href = 'https://fondation-uca.org/projets/bourses-excellence-academique-theses/'>UCA foundation Academic excellence thesis award 2020</a>! This award is delivered to 6 thesis defended in 2020 (or late 2019) at Université Côte d'Azur (University gathering all labs in the region of Nice) accross all disciplines.<br><br>-->
		
		
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
		<li>Committee member: SIGGRAPH Research Career Development Committee, Siggraph Thesis Fast Forward Steering Committee</li>
		<li>Program commitee member: <a href="https://www.cvcs.no/">CVCS 2020</a>, <a href="https://egsr.eu/2021/">EGSR 2021</a></li>
		<li>Journal Reviewer: <a href="https://dl.acm.org/journal/tog">Transactions On Graphics</a>, <a href="https://www.computer.org/csdl/journal/tg">TVCG</a>, <a href="https://onlinelibrary.wiley.com/journal/14678659">CGF</a>, <a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=34">IEEE TPAMI</a></li>
		<li>Tertiary Reviewer: <a href="https://sa2020.siggraph.org/">Siggraph Asia 2019, 2020</a>, <a href="https://s2021.siggraph.org/">Siggraph 2020, 2021</a>, <a href="https://conferences.eg.org/eg2021/">Eurographics 2020, 2021</a>, <a href="http://iccv2021.thecvf.com/home">ICCV 2021</a></li>
		<li>Website administrator and volunteer <a href="https://egsr2020.london/">EGSR 2020</a></li>
	</ul>

</div>