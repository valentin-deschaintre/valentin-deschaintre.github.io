---
layout: egsr-default
title: Program
year: 2022
---

{% if page.year != null %}
	{% assign year = page.year %}
{% else %}
	{% assign year = site.data.egsr.current-year %}
{% endif %}

<style>
	.entry-content p {
	    margin: 0 0 10px 20px;
	}
	h2, .h2 {
	    margin-top: 50px;
	}
</style>

<a name="day1" />

## Day 1 (July 4th 2022)
Jump to <a href="#day2">Day 2</a> <a href="#day3">Day 3</a>

### Opening statement (9 am to 9:20 am)

### Lighting (9:30 am to 10:15 am)

**Spectral Upsampling Approaches for RGB Illumination**  
*Giuseppe Claudio Guarnera, Yuliya Gitlina, Valentin Deschaintre, Abhijeet Ghosh*
 
**SkyGAN: Towards realistic cloud imagery for image based lighting**  
*Martin Mirbauer, Tobias Rittig, Tomáš Iser, Jaroslav Křivánek, Elena Sikudova*

**Break** 15 min

### Global Illumination (10:30 am to 12 noon)

**Dynamic Diffuse Global Illumination Resampling (CGF paper presentation)**  
*Zander Majercik, Thomas Müller, Alexander Keller, Derek Nowrouzezahrai, Morgan McGuire*

**Path Guiding with Vertex Triplet Distributions**  
*Vincent Schüßler, Johannes Hanika, Alisa Jung, Carsten Dachsbacher*

**Once-more scattered next event estimation for volume rendering**  
*Johannes Hanika, Andrea Weidlich, Marc Droske*

**Temporally sliced photon primitives for time-of-flight rendering**  
*Yang Liu, Shaojie Jiao, Wojciech Jarosz*

**Lunch break** 90 min

### Sampling (1:30 pm to 3 pm)

**Planetary Shadow-Aware Distance Sampling**  
*Carl Breyer, Tobias Zirr*

**Single-pass stratified importance resampling**  
*Ege Ciklabakkal, Adrien Gruson, Iliyan Georgiev, Derek Nowrouzezahrai, Toshiya Hachisuka*

**A bidirectional formulation for Walk on Spheres**  
*Yang Qi, Dario Seyb, Benedikt Bitterli, Wojciech Jarosz*

**Gaussian Process for Radiance Functions on the S2 Sphere** (CGF paper presentation)   
*R. Marques, C. Bouville, K. Bouatouch*

**Break** 30 min

### Volume Rendering (3:30 pm to 4:30 pm)

**Automatic Feature Selection for Denoising Volumetric Renderings**  
*Xianyao Zhang,  Melvin Ott, Marco Manzi, Markus Gross, Marios Papas*

**Stenciled Volumetric Ambient Occlusion**  
*Felix Brüll, René Kern, Thorsten Grosch*

**Fast Neural Representations for Direct Volume Rendering** (CGF paper presentation)  
*Sebastian Weiss, Philipp Hermüller, Rüdiger Westermann*

**Break** 30 min

### Keynote by Katie Bouman (5 pm to 6 pm) 

**Break** to change venue

### Get together with wine and cheese (7pm)

<a name="day2" />

## Day 2 (July 5th 2022)
Jump to <a href="#day1">Day 1</a> <a href="#day3">Day 3</a>

### Industry track (9 am to 10 am)

**Multi-Fragment Rendering for Glossy Bounces on the GPU**  
*Atsushi Yoshimura, Yusuke Tokuyoshi, Takahiro Harada*

**Generalized Decoupled and Object Space Shading System**  
*Mark Jarzynski, Dan Baker*

**GAN-based Defect Image Generation for Imbalanced Defect Classification of OLED panels**  
*Yongmoon Jeon, Haneol Kim, Hyeona Lee, Seonghoon Jo, Jaewon Kim*

**Break** 30 min

### BXDFs (10:30 am to noon)

**A Microfacet-based Hair Scattering Model**  
*Weizhen Huang, Matthias Hullin, Johannes Hanika*

**A Position-Free Path Integral for Homogeneous Slabs and Multiple Scattering on Smith Microfacets**  
*Benedikt Bitterli, Eugene d'Eon*

**Microsurface Transformations**  
*Asen Atanasov, Vladimir Koylazov, Rossen Dimov, Alexander Wilkie*

**Neural BRDF Representation and Importance Sampling (CGF paper presentation)**  
*Alejandro Sztrajman, Gilles Rainer, Tobias Ritschel, Tim Weyrich*

**Lunch** 90 min

### Material Modeling and Measurement (1:30pm to 3 pm)

**Controlling Material Appearance by Examples**  
*Yiwei Hu, Milos Hasan, Paul Guerrero, Holly Rushmeier, Valentin Deschaintre*

**Physics-Based Inverse Rendering using Combined Implicit and Explicit Geometries**  
*Guangyan Cai, Kai Yan, Zhao Dong, Ioannis Gkioulekas, Shuang Zhao*

**Polarization-imaging Surface Reflectometry using Near-field Display**  
*Emilie Nogue, Yiming Lin, Abhijeet Ghosh*

**SVBRDF Recovery From a Single Image With Highlights using a Pretrained Generative Adversarial Network** (CGF paper presentation)  
*Tao Wen, Beibei Wang, Lei Zhang, Jie Guo, Nicolas Holzschuch*

**Break** 30 min

### Townhall (3:30 pm to 4:30 pm)

**Break** 30 min

### Keynote  by Jules Urbach (5 pm to 6 pm)

**Break to change venue**  

### Reception in Strahov Monastery Brewery (7:30 pm)

<a name="day3" />

## Day 3 (July 6th 2022)
Jump to <a href="#day1">Day 1</a> <a href="#day2">Day 2</a>

### Neural Rendering (9 am to 10 am)

**A Learned Radiance-Field Representation for Complex Luminaires**  
*Jorge Condor, Adrián Jarabo*

**Deep Flow Rendering: View Synthesis via Layer-aware Reflection Flow**  
*Pinxuan Dai, Xie Ning*

**NeuLF: Efficient Novel View Synthesis with Neural 4D Light Field**  
*Zhong Li, Liangchen Song, Celong Liu, Junsong Yuan, Yi Xu*

**Break** 30 min

### High Performance Rendering (10:30 am to noon)

**A Real-Time Adaptive Ray Marching Method for Particle-Based Fluid Surface Reconstruction**  
*Tong Wu, ZhiQiang Zhou, Anlan Wang, Yuning Gong, Yanci Zhang*

**Precomputed Discrete Visibility Fields for Real-Time Ray-Traced Environmental Lighting**  
*Yang Xu, Yuanfa Jiang, Chenhao Wang, Kang Li, Pengbo Zhou, Guohua GENG*

**Efficient Rendering of Ocular Wavefront Aberrations using Tiled Point-Spread Function Splatting** (CGF paper presentation)  
*István Csoba, Roland Kunkli*

**Lunch** 90 min

### Stylized Rendering (1:30 pm to 3 pm)

**GPU-Driven Real-Time Mesh Contour Vectorization**  
*Wangziwei Jiang, Guiqing Li, Yongwei Nie, Chuhua Xian*

**Recolorable Posterization of Volumetric Radiance Fields via Visibility-weighted Palette Extraction**  
*Kenji Tojo, Nobuyuki Umetani*

**pOp: Parameter Optimization of Differentiable Vector Patterns**  
*Marzia Riso, Davide Sforza, Fabio Pellacini*

**HedcutDrawings: Rendering hedcut style portraits**  
*Karelia Pena-Pena, Gonzalo Arce*

**Break** 30 min

### Patterns and Noises (3:30 pm to 4:15 pm)

**Point-Pattern Synthesis using Gabor and Random Filters**  
*Xingchang Huang, Pooran Memari,  Hans-Peter Seidel, Gurprit Singh*

**Spatiotemporal Blue Noise Masks**  
*Alan Wolfe, Nathan Morrical, Tomas Akenine-Möller, Ravi Ramamoorthi*

**Break** 15 min

### Keynote by Gordon Wetzstein (4:30 pm to 5:30 pm)

### Closing remarks (5:30 pm to 5:45 pm)


