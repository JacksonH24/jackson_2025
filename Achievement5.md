---
layout: page
title: Achievement 5
permalink: Achievement5
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
  </ul>
</nav>

# Achievement 5


<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comment System Integration - Legendary Motorsports</title>
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
        <h1>Integrating the Comments System into Posts</h1>
        <p>One of the most interactive features of Legendary Motorsports is the comment system. While I had already built the backend API and database model, the next major step was to fully integrate it into the frontend, allowing users to create, edit, and delete comments directly on car posts.</p>

        <p>Through seamless frontend-backend communication, the comment system now updates in real time, ensuring that user interactions are smooth and efficient.</p>

        <h2>Frontend-Backend Integration</h2>
        <p>To integrate the backend API and database model into the frontend, I implemented the following steps:</p>
        <ul class="feature-list">
            <li>Fetched comments dynamically from the backend API using JavaScript.</li>
            <li>Implemented AJAX requests to allow users to add, edit, and delete comments instantly.</li>
            <li>Created a real-time UI update so new comments appear without refreshing the page.</li>
            <li>Ensured form validation and error handling to prevent spam and empty comments.</li>
        </ul>

        <h2>CRUD Operations: How It Works</h2>
        <p>The integration is built around four core actions (CRUD operations):</p>

        <h3>1. Creating a Comment (POST)</h3>
        <p>When a user submits a comment, the frontend sends a POST request to the backend API. The response then updates the UI in real time.</p>

        <h3>2. Retrieving Comments (GET)</h3>
        <p>Whenever a post is loaded, a GET request fetches all comments from the database and displays them dynamically.</p>

        <h3>3. Editing a Comment (PUT)</h3>
        <p>Users can edit their own comments. When an edit is made, a PUT request updates the database and refreshes the displayed content instantly.</p>

        <h3>4. Deleting a Comment (DELETE)</h3>
        <p>To maintain a clutter-free experience, users can delete their comments. A DELETE request removes the comment from the database, and the frontend removes it from the UI without needing a page refresh.</p>

        <h2>Challenges & Solutions</h2>
        <p>Integrating the comments system into the frontend required overcoming a few challenges:</p>
        <ul class="feature-list">
            <li><strong>Challenge:</strong> Keeping comments updated without refreshing the page.</li>
            <li><strong>Solution:</strong> Used AJAX requests and JavaScript event listeners for real-time updates.</li>

            <li><strong>Challenge:</strong> Preventing spam and blank comments.</li>
            <li><strong>Solution:</strong> Implemented input validation and error handling before submitting data.</li>

            <li><strong>Challenge:</strong> Ensuring users can only edit or delete their own comments.</li>
            <li><strong>Solution:</strong> Added authentication checks to verify user ownership before modifying data.</li>
        </ul>

        <h2>User Feedback</h2>
        <p>At Night at the Museum, users loved how smooth and interactive the comment system was. The ability to edit and delete comments in real time made the platform feel polished and professional.</p>

        <h2>Future Improvements</h2>
        <p>Now that the comments system is fully integrated, I plan to enhance it even further:</p>
        <ul class="feature-list">
            <li>Adding reply threads for deeper conversations.</li>
            <li>Integrating likes and reactions on comments.</li>
            <li>Using AI-based moderation to automatically detect spam.</li>
        </ul>

        <p>The comment system has transformed Legendary Motorsports into a truly interactive platform, and I’m excited to keep improving it!</p>

        <div class="footer">
            <p>© 2025 Legendary Motorsports. All Rights Reserved.</p>
        </div>
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

</body>

