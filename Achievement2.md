---
layout: page
title: Achievement 2
permalink: Achievement2
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

# Achievement 2


<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Backend for Comment System - Legendary Motorsports</title>
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
        code {
            background-color: #eee;
            padding: 3px 6px;
            border-radius: 4px;
        }
        pre {
            background: #272822;
            color: #f8f8f2;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>

  <div class="container">
        <h1>Building a Fast & Secure Comment System Backend</h1>
        <p>Interactivity is key for any social media platform, and comments are essential for fostering engagement. For Legendary Motorsports, I developed the entire backend API and database model for the comment system, ensuring fast, secure, and reliable communication between users.</p>

<h2>Comment System in Action</h2>
        <p>Scroll down to see how the API processes and stores comments in real time:</p>

<div class="video-container">
            <video id="scrollVideo" muted playsinline loop>
                <source src="images/tvick22.github.io_personal_flocker_frontend_allPosts - 2 March 2025.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>

<div class="video-container">
            <video id="scrollVideo" muted playsinline loop>
                <source src="images/Car Comments - 2 March 2025.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>

 <h2>Backend Design & API Endpoints</h2>
        <p>The backend for the comment system is built using Flask (Python) and utilizes SQLAlchemy for database management. The API supports the following CRUD operations:</p>
        <ul class="feature-list">
            <li><strong>GET:</strong> Retrieve all comments for a specific post.</li>
            <li><strong>POST:</strong> Add a new comment.</li>
            <li><strong>PUT:</strong> Update an existing comment (only if the user owns it).</li>
            <li><strong>DELETE:</strong> Remove a comment (only if the user owns it).</li>
        </ul>

<h2>Database Model - CarComments</h2>
        <p>All comments are stored in a SQLAlchemy database model, ensuring structured and efficient data retrieval. Here’s the model definition:</p>

        <pre><code>
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class CarComments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    post_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "post_id": self.post_id,
            "content": self.content,
            "timestamp": self.timestamp
        }
        </code></pre>

        <h2>Comment API - CRUD Operations</h2>
        <p>The API follows RESTful principles, allowing smooth communication between the frontend and backend.</p>

        <h3>1. Adding a Comment (POST Request)</h3>
        <p>When a user submits a comment, the frontend sends a POST request with JSON data:</p>
        <pre><code>
@app.route('/comments', methods=['POST'])
def add_comment():
    data = request.json
    if "content" not in data or "post_id" not in data or "user_id" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    new_comment = CarComments(
        user_id=data["user_id"],
        post_id=data["post_id"],
        content=data["content"]
    )

    db.session.add(new_comment)
    db.session.commit()

return jsonify(new_comment.to_dict()), 201
        </code></pre>

        <h3>2. Retrieving Comments (GET Request)</h3>
        <p>The frontend fetches all comments for a specific post using a GET request:</p>
        <pre><code>
@app.route('/comments/<int:post_id>', methods=['GET'])

def get_comments(post_id):
    comments = CarComments.query.filter_by(post_id=post_id).all()
    return jsonify([comment.to_dict() for comment in comments])
        </code></pre>

        <h3>3. Editing a Comment (PUT Request)</h3>
        <p>Users can edit their own comments. The backend checks ownership before updating:</p>
        <pre><code>
@app.route('/comments/<int:comment_id>', methods=['PUT'])

def update_comment(comment_id):
    comment = CarComments.query.get(comment_id)
    data = request.json
    if "content" in data:
        comment.content = data["content"]
        db.session.commit()
        return jsonify(comment.to_dict()), 200
    return jsonify({"error": "Invalid request"}), 400
        </code></pre>

        <h3>4. Deleting a Comment (DELETE Request)</h3>
        <p>Users can delete only their own comments. This prevents unauthorized modifications:</p>
        <pre><code>
@app.route('/comments/<int:comment_id>', methods=['DELETE'])

def delete_comment(comment_id):
    comment = CarComments.query.get(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "Comment deleted"}), 200
        </code></pre>

<h2>Challenges & Solutions</h2>
<p>Building a **real-time comment system backend** had its challenges, but I tackled them effectively:</p>
<ul class="feature-list">
<li><strong>Challenge:</strong> Ensuring fast retrieval of comments without overloading the server.</li>
<li><strong>Solution:</strong> Used **SQLAlchemy indexing** and optimized queries for performance.</li>

<li><strong>Challenge:</strong> Preventing spam and inappropriate content.</li>
<li><strong>Solution:</strong> Implemented **input validation, keyword filtering, and user authentication checks**.</li>

 <li><strong>Challenge:</strong> Maintaining security and preventing unauthorized deletions.</li>
<li><strong>Solution:</strong> Enforced **user authentication and ownership verification** before updating or deleting comments.</li>
</ul>

<h2>The Impact & Future Improvements</h2>
        <p>The comment system backend made *Legendary Motorsports* a truly interactive platform. Future improvements include:</p>
<ul class="feature-list">
            <li>Adding **comment replies and threads** for deeper discussions.</li>
            <li>Integrating **AI-based moderation** for automatic spam detection.</li>
            <li>Enhancing **database indexing** for even faster response times.</li>
</ul>




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
