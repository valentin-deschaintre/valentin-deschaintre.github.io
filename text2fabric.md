---
permalink: /text2fabric
title: 'The Visual Language of Fabrics'
layout: paper
---

<div id='content'>
	<center>
	<div id='paper'>
     <div class="row">
            <h1 class="col-md-12 text-center">
              The Visual Language of Fabrics
              <br/><small>Siggraph 2023</small>
            </h1>
        </div>
        <div class="row">
            <div class="col-md-12 text-center">
                <ul class="list-inline">
                    <li>
                        <a href="https://valentin.deschaintre.fr">
                            Valentin Deschaintre*
                        </a>
                        <br/>Adobe Research
                    </li>
                    <li>
                        <a href="http://webdiis.unizar.es/~juliagv/">
                            Julia Guerrero-Viu*
                        </a>
                        <br/>Universidad de Zaragoza - I3A
                    </li>
                    <li>
                        <a href="http://giga.cps.unizar.es/~diegog/">
                            Diego Gutierrez
                        </a>
                        <br/>Universidad de Zaragoza - I3A
                    </li>
                    <li>
                        <a href="https://perso.telecom-paristech.fr/boubek/">
                            Tamy Boubekeur
                        </a>
                        <br/>Adobe Research
                    </li>
                    <li>
                        <a href="http://webdiis.unizar.es/~bmasia/">
                            Belen Masia
                        </a>
                        <br/>Universidad de Zaragoza - I3A
                    </li>
                </ul>
            </div>
            <div class="col-md-12 text-center">
			<small>* Equal contribution </small>
			</div>
        </div>
        <center>
        <div class="row" id="header_img">
            <figure class="col-md-8 col-md-offset-2">
            <image src="img/nlp4mat_teaser.jpeg" class="img-responsive" alt="overview" style="width:100%;"/>
            </figure>
        </div>
        </center>
        <!-- <div class="row"> -->
        <!--     <div class="col&#45;md&#45;8 col&#45;md&#45;offset&#45;2 text&#45;center last"> -->
        <!--         <iframe align="center" width="560" height="315" src="" frameborder="0" allowfullscreen></iframe> -->
        <!--     </div> -->
        <!-- </div> -->
        <div class="row">
            <div class="col-md-8 col-md-offset-2">
                <h3>
                    Abstract
                </h3>
                <p class="text-justify">
We introduce text2fabric, a novel dataset that links free-text descriptions to various fabric materials. 
The dataset comprises 15,000 natural language descriptions associated to 3,000 corresponding images of fabric materials. 
Traditionally, material descriptions come in the form of tags/keywords, which limits their expressivity, induces pre-existing knowledge of the appropriate vocabulary, and ultimately leads to a chopped description system. 
Therefore, we study the use of free-text as a more appropriate way to describe material appearance, taking the use case of fabrics as a common item that non-experts may often deal with. 
Based on the analysis of the dataset, we identify a compact lexicon, set of attributes and key structure that emerge from the descriptions. 
This allows us to accurately understand how people describe fabrics and draw directions for generalization to other types of materials. 
We also show that our dataset enables specializing large vision-language models such as CLIP, creating a meaningful latent space for fabric appearance, and significantly improving applications such as fine-grained material retrieval and automatic captioning.
                </p>
            </div>
        </div>
        <div class="row">
            <div class="col-md-8 col-md-offset-2">
                <h3>
                <!-- <h3 class="text&#45;center"> -->
                    Downloads
                </h3>
                <div class="col-md-8 col-md-offset-2 text-center">
                    <ul class="nav nav-pills nav-justified">
                        <li>
                            <a href="files/Visual_language_fabric_optim.pdf">
                                Paper
                            </a>
                        </li>
                      <li>
                            <a href="files/The_Visual_Language_of_Fabrics_Supplemental_Material.pdf">
                                Supplemental Materials
                            </a>
                        </li> 	
                          <li>
                            <a href="text2fabric_additional_results.html">
                                Additional Results
                            </a>
                        </li> 
                      <li>
                            <a href="text2fabric_browser_v1.html">
                                Data Browser
                            </a>
                        </li>     
                    </ul>
                </div>  <br>
                <div class="col-md-8 col-md-offset-2 text-center">
                    <ul class="nav nav-pills nav-justified">
                        <li>
                            <a href="https://language-fabric-pub.s3.us-west-2.amazonaws.com/descriptions.csv">
                                Data: Descriptions
                            </a>
                        </li>
                        <li>
                            <a href="https://language-fabric-pub.s3.us-west-2.amazonaws.com/renderings.zip">
                                Data: All renderings 512x512
                            </a>
                        </li> 
                        <li>
                            <a href="https://language-fabric-pub.s3.us-west-2.amazonaws.com/renderings_4096_drape.zip">
                                Data: 4K Renderings
                            </a>
                        </li>
                <li>
                            <a href="https://language-fabric-pub.s3.us-west-2.amazonaws.com/file_name_url_correspondance.json">
                                Data: Substance Materials URLs
                            </a>
                        </li>
            <li>
                            <a href="data_fabric_license.md">
                                License
                            </a>
                        </li>           
                    </ul>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-8 col-md-offset-2">
                <h3>
                    BibTeX
                </h3>
                <div class="text-justify">
					<pre style="display: flex; justify-content: center;">
@article{deschaintre23_visual_fabric,
author = {Deschaintre, Valentin and Guerrero-Viu, Julia and Gutierrez, Diego and Boubekeur, Tamy and Masia, Belen},
title = {The Visual Language of Fabrics},
year = {2023},
issue_date = {August 2023},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {42},
number = {4},
issn = {0730-0301},
doi = {10.1145/3592391},
journal = {ACM Trans. Graph.},
month = {jul},
articleno = {50},
numpages = {15},
keywords = {material appearance, descriptions, perception}
}

</pre>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-8 col-md-offset-2">
                <h3>
                    Acknowledgements
                </h3>
                <p class="text-justify">
                  We thank Kushal Kafle for his help in navigating the NLP domain; Yulia Gryaditskaya and Zoya Bylinskii for advice about data collection and user studies; J Eisenmann for his help in data generation; Jorge Gracia del Rio for NLP pointers; and Sergio Izquierdo and the members of the Graphics and Imaging Lab for discussions and help preparing the final figures. We would also like to thank the Substance 3D Assets team for the creation of the materials, all the participants in the user studies, and the anonymous reviewers.
                  This work has received funding from the European Research Council (ERC) within the EU's Horizon 2020 research and innovation programme (project CHAMELEON, Grant No. 682080) and under the Marie Skłodowska-Curie grant agreement No. 956585 (project PRIME), as well as a generous donation from Adobe. Julia Guerrero-Viu was supported by the FPU20/02340 predoctoral grant. We borrow this Template from Michaël Gharbi.
                </p>
            </div>
        </div>
    </div>
</center>
</div>
