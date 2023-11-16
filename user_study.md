---
permalink: /userstudy
title: "User Study"
layout: wide
---

<body style="width: 60%; margin: auto;">

<h2 style="font-size: larger; font-weight: bold; padding-top: 10px; padding-bottom: 10px;">
    Please read carefully: 
</h2>

The goal of our project is to generate plausible textures for a given geometry. A plausible texture is consistent from different viewpoints (i.e., has as few seams as possible). We will show you a geometry and a video with two results, please select which result you prefer.
Please read the instructions carefully and in the end, do not forget to click 'submit'. 
The study should not take more than 5 minutes  of your time - thank you for participating!

<br>

{% for id in (0..9) %}

{{id | plus: 1}}/10: Given the geometry in the first image, which texture has the best overall quality?
<center>
<form id="NAvideoForm">

<div class="top-image-container">
    <img src="https://text2mat-bot.s3.us-west-2.amazonaws.com/video_user_study/0000/mesh.png" width=256 id="{{id}}_imgTop">
</div>
    <div class="NAvideo-container">
        <video width="512" height="512" mute loop autoplay controls id="{{id}}_video_src">
        <source src="https://text2mat-bot.s3.us-west-2.amazonaws.com/video_user_study/0000/output_ours_text2tex.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
        <div class="radio-buttons">
            <input type="radio" name="transf{{id}}" value="0"> Left
            <input type="radio" name="transf{{id}}" value="1"> Right
        </div>
    </div>
</form>
</center>

{% endfor %}
<br/><br/>
<center><button type="button" id="submit">Submit</button></center>
<br/><br/>
<script>
const randomMeshes = [];
var randomMethod = ["text2tex", "texture", "text2tex", "texture", "text2tex", "texture", "text2tex", "texture", "text2tex", "texture"];
const shuffle = (array) => { 
  for (let i = array.length - 1; i > 0; i--) { 
    const j = Math.floor(Math.random() * (i + 1)); 
    [array[i], array[j]] = [array[j], array[i]]; 
  } 
  return array; 
}; 
randomMethod = shuffle(randomMethod);

for (let i = 0; i < 10; i++) {
    randomMeshes.push(Math.floor(Math.random() * 411));
}

window.onload = load_videos;
function load_videos() {

    for (let id=0; id < 10; id++)
    {
        const id_str = String(randomMeshes[id]).padStart(4, '0');
        const method = randomMethod[id]
        
        document.getElementById(id + "_imgTop").src = "https://text2mat-bot.s3.us-west-2.amazonaws.com/video_user_study/" + id_str + "/mesh.png";
        document.getElementById(id + "_video_src").src = "https://text2mat-bot.s3.us-west-2.amazonaws.com/video_user_study/" + id_str + "/output_ours_" + method + ".mp4";
    }
};


document.getElementById('submit').addEventListener('click', function() {
    var transfRadio0 = document.querySelector('input[name="transf0"]:checked');
    var transfRadio1 = document.querySelector('input[name="transf1"]:checked');
    var transfRadio2 = document.querySelector('input[name="transf2"]:checked');
    var transfRadio3 = document.querySelector('input[name="transf3"]:checked');
    var transfRadio4 = document.querySelector('input[name="transf4"]:checked');
    var transfRadio5 = document.querySelector('input[name="transf5"]:checked');
    var transfRadio6 = document.querySelector('input[name="transf6"]:checked');
    var transfRadio7 = document.querySelector('input[name="transf7"]:checked');
    var transfRadio8 = document.querySelector('input[name="transf8"]:checked');
    var transfRadio9 = document.querySelector('input[name="transf9"]:checked');

    
    if (!transfRadio0 || !transfRadio1 || !transfRadio2 || !transfRadio3 || !transfRadio4 || !transfRadio5 || !transfRadio6 || !transfRadio7|| !transfRadio8|| !transfRadio9) {
        alert("Please make a selection for ALL items.");
        return;
    }

    var transfV0 = transfRadio0.value;
    var transfV1 = transfRadio1.value;
    var transfV2 = transfRadio2.value;
    var transfV3 = transfRadio3.value;
    var transfV4 = transfRadio4.value;
    var transfV5 = transfRadio5.value;
    var transfV6 = transfRadio6.value;
    var transfV7 = transfRadio7.value;
    var transfV8 = transfRadio8.value;
    var transfV9 = transfRadio9.value;

    var queryString = `transf0=${encodeURIComponent(transfV0)}&` + 
                      `transf1=${encodeURIComponent(transfV1)}&` +
                      `transf2=${encodeURIComponent(transfV2)}&` +
                      `transf3=${encodeURIComponent(transfV3)}&` +
                      `transf4=${encodeURIComponent(transfV4)}&` +
                      `transf5=${encodeURIComponent(transfV5)}&` +
                      `transf6=${encodeURIComponent(transfV6)}&` +
                      `transf7=${encodeURIComponent(transfV7)}&` +
                      `transf8=${encodeURIComponent(transfV8)}&` +
                      `transf9=${encodeURIComponent(transfV9)}&` +
                      `meshid0=${encodeURIComponent(randomMeshes[0])}&` + 
                      `meshid1=${encodeURIComponent(randomMeshes[1])}&` +
                      `meshid2=${encodeURIComponent(randomMeshes[2])}&` +
                      `meshid3=${encodeURIComponent(randomMeshes[3])}&` +
                      `meshid4=${encodeURIComponent(randomMeshes[4])}&` +
                      `meshid5=${encodeURIComponent(randomMeshes[5])}&` +
                      `meshid6=${encodeURIComponent(randomMeshes[6])}&` +
                      `meshid7=${encodeURIComponent(randomMeshes[7])}&` +
                      `meshid8=${encodeURIComponent(randomMeshes[8])}&` +
                      `meshid9=${encodeURIComponent(randomMeshes[9])}&` +
                      `method0=${encodeURIComponent(randomMethod[0])}&` + 
                      `method1=${encodeURIComponent(randomMethod[1])}&` +
                      `method2=${encodeURIComponent(randomMethod[2])}&` +
                      `method3=${encodeURIComponent(randomMethod[3])}&` +
                      `method4=${encodeURIComponent(randomMethod[4])}&` +
                      `method5=${encodeURIComponent(randomMethod[5])}&` +
                      `method6=${encodeURIComponent(randomMethod[6])}&` +
                      `method7=${encodeURIComponent(randomMethod[7])}&` +
                      `method8=${encodeURIComponent(randomMethod[8])}&` +
                      `method9=${encodeURIComponent(randomMethod[9])}`;

    // queryString = `name=${encodeURIComponent(participantName)}&${queryString}`;

    fetch(`https://script.google.com/macros/s/AKfycby5FbuER43cO_G73uV5fGHaOaM8rvFfxg1Avp1JhANJcO_8xj3mmWdJmjTkJ_Xd8InR/exec?${queryString}`)
        .then(response => response.json())
        .then(data => {
            if (data && data.result === "success") {
                // Displaying a thank you message
                alert("Thank you for your submission!");
            } else {
                // Handle other responses or errors
                alert("There was an issue with your submission.");
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert("An error occurred while submitting your response.");
        });
});

</script>

</body>

