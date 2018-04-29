---
layout: news
categories: news
title: Post template
excerpt: A post template to help create posts using Jekyll
image:
  feature: sample.jpg
  credit: "Markus Spiske"
  creditlink: "https://unsplash.com/photos/8OyKWQgBsKQ"
  card: 2018/expressiveCard.jpg
sidebar: twitter
---

This website is built using the Jekyll framework, which makes the development of static websites easy and straightforward, even for non-developers. This template post is meant to help anyone unfamiliar with Jekyll to get started and add content to this website.

## Creating a News post

To create a News post, create a text file with a `*.md` extension inside the `_posts/news` folder. The name of this text file is critical for it to be rightfully incorporated by Jekyll into the website. So lets go over the most important points.

* The name begins with the date it should become public, in `YYYY-MM-DD` format
* Followed by a dash and the URL in the website (which should not contain whitespaces)

In the end, your text file will be named something like this inside the `_posts/news` folder: `2017-12-25-merry-christmas.md`. In the website, it will be located at `expressive.graphics/2018/news/merry-christmas`.


## Post template

Jekyll parses markdown language to automatically generate HTML. In fact, we are writing in markdown right now. Markdown uses simple syntax to control the way words are formatted.

For example, we just created a new paragraph `(<p> </p>)` by leaving an empty line between the text. There are many features to the markdown syntax, so we will only introduce the most common ones in this post template.

* A list is started at each line by an asterisk, followed by a whitespace and the content, e.g. `* A list element`. In the case of numbered lists, simply replace the asterisk of the first list element with a number, followed by a point, e.g. `1. First list element`.
* _Italic_ text is marked by wrapping the content with underscores, e.g. `_italize_`.
* **Bold** text is marked by wrapping the content with double asterisks, e.g. `(**bold**)`.
* Headings are marked down with hashtags followed by a whitespace and the heading title. The least hashtags, the more important the header, e.g. `## Markdown cheatsheet` is a `<h2></h2>` because it has two hashtags.
* A link ([Expressive website](expressive.graphics)) is created by wrapping the text in squared brackets and the URL in brackets, e.g. `[Expressive website](expressive.graphics)`.

## Markdown reference

* For a quick reference of additional syntax, make sure to check the [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).
* For the full list of features and syntax reference, visit the official documentation of its creator, John Gruber, [here](https://daringfireball.net/projects/markdown/syntax).

## Adding images

Adding images using markdown is not possible, but we can always revert back to HTML within a markdown post and rely on Bootstrap to set them up in a responsive manner.

Using Bootstrap to format images is straightforward. One can simply specify how many columns (12 in total) they should take along the entire width. These columns can also be set by device, so the images are resized according to different screen sizes. Two examples are seen below.

<figure class="col-xs-12">
    <img class="col-xs-12 col-sm-4" src="/img/2018/CAe.png" alt="CAe">
    <img class="col-xs-12 col-sm-4" src="/img/2018/SBIM.png" alt="SBIM">
    <img class="col-xs-12 col-sm-4" src="/img/2018/NPAR.png" alt="NPAR">
    <figcaption class="col-xs-12">Three images in a row for big screens, one image per row for small screens</figcaption>
</figure>

In the example above, each image has the classes `class="col-xs-12 col-sm-4"`. This means that for extra small devices `xs` (e.g. phones), the images will span the entire width (12 columns). For bigger devices `sm` (small) and above, each image will span 4 columns out of the 12, allowing us to fit 3 images per row.

<figure style="width:60%;">
	<img class="col-xs-12" src="/img/2018/CAe.png" alt="CAe">
  <figcaption>A single image that spans the entire row width</figcaption>
</figure>

In the example above, the single image will span the entire width as only the extra small class has bee specified to take all 12 columns `class="col-xs-12`

## Utility classes

A number of small utility classes have also been added to aid formatting content on this website. These classes can be used in both HTML `<figure class="top3"></figure>` and Markdown `{: .top3}` (in the line following the content that should have the class). Some common classes are the following:

* Adding top margins to the html are also available _top1, top2, top3_.
* Adding bottom margins to the html are also available _bottom1, bottom2, bottom3_.
* Pulling things to either side _pull-right, pull-left_.

That's it, this should cover the basics to start adding content with markdown on the conference website. Have fun!
{: .top3}
