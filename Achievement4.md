---
layout: page
title: Achievement 4
permalink: Achievement4
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

# Achievement 4

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Settings Page - Legendary Motorsports</title>
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
        <h1>Enhancing User Control: The Settings Page</h1>
        <p>The Settings Page in <strong>Legendary Motorsports</strong> is a crucial feature that gives users full control over their profiles. With a clean and intuitive UI, users can seamlessly update their profile picture, username, and password, ensuring a personalized experience.</p>

The page was designed to be fully responsive and includes real-time updates, so changes are instantly reflected across the platform.

<h2>Settings Page in Action</h2>
        <p>Scroll down to see how the settings page allows users to manage their profiles effortlessly:</p>

<div class="video-container">
            <video id="scrollVideo" muted playsinline loop>
                <source src="images/Car Social Profile - 2 March 2025 (1).mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>

<h2>Key Features</h2>
        <ul class="feature-list">
            <li><strong>Profile Customization:</strong> Users can update their profile picture and username instantly.</li>
            <li><strong>Password Management:</strong> Securely change passwords with built-in validation.</li>
            <li><strong>Real-Time Updates:</strong> Profile changes are immediately reflected across the platform.</li>
            <li><strong>Responsive Design:</strong> Works perfectly on desktops, tablets, and mobile devices.</li>
            <li><strong>Security Measures:</strong> Users are required to authenticate before making sensitive changes.</li>
        </ul>

<h2>Challenges & Solutions</h2>
        <p>Developing the Settings Page required solving various technical challenges:</p>
        <ul class="feature-list">
            <li><strong>Challenge:</strong> Ensuring profile updates apply instantly without refreshing the page.</li>
            <li><strong>Solution:</strong> Implemented AJAX requests to update user data dynamically.</li>

            <li><strong>Challenge:</strong> Handling profile picture uploads efficiently without slowing down performance.</li>
            <li><strong>Solution:</strong> Used image compression techniques to optimize storage and speed.</li>

            <li><strong>Challenge:</strong> Keeping password changes secure and encrypted.</li>
            <li><strong>Solution:</strong> Integrated hashing algorithms and authentication checks before updates.</li>
        </ul>

        <h2>User Feedback</h2>
        <p>At Night at the Museum, users loved the simplicity and effectiveness of the settings panel. Many appreciated how quickly changes applied and how easy it was to customize their profiles.</p>

        <p>Security features like password validation and authentication were also well received, as they added an extra layer of protection without complicating the experience.</p>

        <h2>Future Enhancements</h2>
        <p>The Settings Page is already a powerful tool, but I plan to introduce additional improvements:</p>
        <ul class="feature-list">
            <li>Adding two-factor authentication (2FA) for enhanced security.</li>
            <li>Providing an option for custom bio descriptions.</li>
            <li>Allowing users to switch between light and dark mode.</li>
        </ul>

<p>The Settings Page is an essential feature of *Legendary Motorsports*, giving users full control over their profiles while ensuring a seamless and secure experience.</p>

 <div class="footer">
            <p>© 2025 Legendary Motorsports. All Rights Reserved.</p>
 </div>


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


