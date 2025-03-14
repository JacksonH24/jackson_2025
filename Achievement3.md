---
layout: page
title: Achievement 3
permalink: Achievement3
---

<style>
  nav {
    background-color: #333;
    overflow: hidden;
  }
  nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
  }
  nav ul li {
    float: left;
  }
  nav ul li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
  }
  nav ul li a:hover {
    background-color: #111;
  }
  body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 20px;
  }
  h1 {
    color: #333;
  }
</style>

<nav>
  <ul>
    <li><a href="/jackson_2025/Legendary">Review</a></li>
    <li><a href="/jackson_2025/NATM">N@TM</a></li>
    <li><a href="/jackson_2025/Feature">Feature</a></li>
    <li><a href="/jackson_2025/Achievement1">Achievement 1</a></li>
    <li><a href="/jackson_2025/Achievement2">Achievement 2</a></li>
    <li><a href="/jackson_2025/Achievement3">Achievement 3</a></li>
    <li><a href="/jackson_2025/Achievement4">Achievement 4</a></li>
    <li><a href="/jackson_2025/Achievement5">Achievement 5</a></li>
    <li><a href="/jackson_2025/SelfGrade">Self Grade</a></li>
    <li><a href="/jackson_2025/Extra">Extra</a></li>
    <li><a href="/jackson_2025/MCQ">MCQ</a></li>
    <li><a href="/jackson_2025/PPR">PPR</a></li>
  </ul>
</nav>

# Achievement 3


<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile Page - Legendary Motorsports</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f4f4;
            color: #333;
        }
        .container {
            max-width: 1000px;
            margin: auto;
            padding: 20px;
            background-color: white;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            color: #222;
        }
        p {
            line-height: 1.6;
        }
        .feature-list {
            margin-top: 20px;
            padding-left: 20px;
        }
        .feature-list li {
            margin-bottom: 10px;
        }
        .video-container {
            text-align: center;
            margin: 20px 0;
        }
        video {
            max-width: 100%;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        }
        .footer {
            margin-top: 30px;
            font-size: 14px;
            color: #555;
        }
    </style>
</head>
<body>

  <div class="container">
        <h1>Creating the Legendary Motorsports Profile Page</h1>
        <p>The **Profile Page** in <strong>Legendary Motorsports</strong> is one of the most visually polished and functional parts of the website. Inspired by **Instagram**, it showcases a user’s profile picture, username, posts, and followers in a clean and interactive design.</p>

<p>To make the experience even better, I added a **unique ignition key animation** for an engaging transition when navigating to the profile page. Users can also **update their profile picture and username**, with changes reflected in real-time.</p>

<h2>Profile Page in Action</h2>
        <p>Scroll down to see how the profile page works:</p>

<div class="video-container">
            <video id="scrollVideo" muted playsinline loop>
                <source src="images/Car Social Profile - 2 March 2025.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>

<h2>Key Features</h2>
        <ul class="feature-list">
            <li><strong>Instagram-Inspired Layout:</strong> Displays user posts in a grid format.</li>
            <li><strong>Real-Time Profile Updates:</strong> Profile picture and username update instantly when changed in settings.</li>
            <li><strong>Ignition Key Animation:</strong> A **smooth transition effect** when navigating to the profile.</li>
            <li><strong>Follow System:</strong> Users can follow each other, and follower count updates dynamically.</li>
            <li><strong>Responsive Design:</strong> Works flawlessly on all devices, from desktops to mobile.</li>
        </ul>

        <h2>Challenges & Solutions</h2>
        <p>Building the Profile Page came with challenges, but I found effective solutions:</p>
        <ul class="feature-list">
            <li><strong>Challenge:</strong> Keeping profile updates real-time without page reloads.</li>
            <li><strong>Solution:</strong> Used AJAX requests to update data dynamically.</li>

            <li><strong>Challenge:</strong> Ensuring a smooth ignition key animation**.</li>
            <li><strong>Solution:</strong> Optimized the CSS animation to work across all screen sizes.</li>

            <li><strong>Challenge: Making the follow system dynamic.</li>
            <li><strong>Solution:</strong> Implemented a database-driven system to track follows and update UI instantly.</li>


        <h2>User Feedback</h2>
        <p>At Night at the Museum, attendees were highly impressed with the profile page’s design, smooth animations, and responsiveness. Many mentioned that it looked like a real social media platform, and the ignition key animation was a favorite.</p>

<h2>What’s Next?</h2>
<p>The Profile Page is already a standout feature, but I plan to improve it even further:</p>
<ul class="feature-list">
            <li>Adding profile bios so users can share more about themselves.</li>
            <li>Implementing direct messaging** for users to communicate privately.</li>
</ul>

<p>The Profile Page has set a new standard for UI/UX on Legendary Motorsports, and I’m excited to continue refining it!</p>



  <script>
        document.addEventListener("DOMContentLoaded", function() {
            const video = document.getElementById("scrollVideo");

            function checkScroll() {
                const rect = video.getBoundingClientRect();
                const windowHeight = window.innerHeight || document.documentElement.clientHeight;

                if (rect.top >= 0 && rect.bottom <= windowHeight) {
                    video.play();
                } else {
                    video.pause();
                }
            }

            window.addEventListener("scroll", checkScroll);
        });
    </script>
