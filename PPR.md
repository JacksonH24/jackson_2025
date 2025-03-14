---
layout: page
title: PPR BLOG
permalink: PPR
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


<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PPR Blog - AP CSP Component C</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            padding: 20px;
            background-color: #f4f4f4;
            line-height: 1.6;
        }
        h1, h2, h3 {
            color: #333;
            text-align: center;
        }
        .container {
            max-width: 900px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .code-container {
            background: #222;
            color: #f8f8f2;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            font-family: monospace;
            overflow-x: auto;
            margin-bottom: 20px;
        }
        .section {
            margin-bottom: 30px;
            padding: 20px;
            border-left: 5px solid #007BFF;
            background: #f9f9f9;
            border-radius: 5px;
        }
        ul {
            padding-left: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }
        table, th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background: #007BFF;
            color: white;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>🚀 AP CSP Component C: Personalized Project Reference</h1>
        <p><strong>Date:</strong> March 12, 2025</p>

        <div class="section">
            <h2>🔍 Overview</h2>
            <p>This submission includes four required code segments demonstrating key programming concepts:</p>
            <ul>
                <li><strong>Student-Developed Procedure</strong>: A function implementing **sequencing, selection, and iteration**.</li>
                <li><strong>Function Call</strong>: Shows where the student-developed procedure is used in the program.</li>
                <li><strong>List Implementation</strong>: A **list (or collection type)** used to store and manage data efficiently.</li>
                <li><strong>List Processing</strong>: Using data from the list to fulfill program functionality.</li>
            </ul>
        </div>

        <div class="section">
            <h2>1️⃣ Student-Developed Procedure</h2>
            <h3>📌 Code Segment: Comment Creation Function</h3>
            <div class="code-container">
                <pre>
@token_required()
def add_comment(user_id, post_id, content):
    if not content.strip():
        return jsonify({"message": "Comment cannot be empty"}), 400

    comment = CarComments(user_id=user_id, post_id=post_id, content=content)
    comment.create()
    
    return jsonify(comment.read())
                </pre>
            </div>

            <h3>📌 Explanation</h3>
            <ul>
                <li><strong>Sequencing:</strong> The function follows a structured order: validating input, creating a comment, saving it, and returning a response.</li>
                <li><strong>Selection:</strong> An `if` condition ensures that an empty comment is not submitted.</li>
                <li><strong>Iteration:</strong> The `get` function later iterates over all comments for retrieval.</li>
            </ul>
        </div>

        <div class="section">
            <h2>2️⃣ Function Call</h2>
            <h3>📌 Code Segment: Calling the Procedure</h3>
            <div class="code-container">
                <pre>
@app.route("/api/add_comment", methods=["POST"])
@token_required()
def post_comment():
    data = request.get_json()
    return add_comment(g.current_user.id, data["post_id"], data["content"])
                </pre>
            </div>

            <h3>📌 Explanation</h3>
            <ul>
                <li>This function calls `add_comment()`, passing the current user’s ID, post ID, and comment content.</li>
                <li>It ensures secure authentication with `@token_required()`.</li>
                <li>The API processes user input and interacts with the database.</li>
            </ul>
        </div>

        <div class="section">
            <h2>3️⃣ List Implementation</h2>
            <h3>📌 Code Segment: Storing Data in a List</h3>
            <div class="code-container">
                <pre>
def get_comments_for_post(post_id):
    comments = CarComments.query.filter_by(post_id=post_id).all()
    return [comment.read() for comment in comments]
                </pre>
            </div>

            <h3>📌 Explanation</h3>
            <ul>
                <li>This function retrieves all comments related to a specific post.</li>
                <li>A list comprehension processes multiple comments efficiently.</li>
            </ul>
        </div>

        <div class="section">
            <h2>4️⃣ List Processing</h2>
            <h3>📌 Code Segment: Processing the List</h3>
            <div class="code-container">
                <pre>
def format_comments(comments):
    formatted = []
    
    for comment in comments:
        formatted.append(f"{comment['user_id']} said: {comment['content']}")

    return formatted
                </pre>
            </div>

            <h3>📌 Explanation</h3>
            <ul>
                <li>A for loop iterates over the comments list.</li>
                <li>Each comment is formatted into a structured text output.</li>
                <li>The function creates a processed list for display.</li>
            </ul>
        </div>

        <div class="section">
            <h2>📌 Summary of PPR Components</h2>
            <table>
                <tr>
                    <th>Component</th>
                    <th>Purpose</th>
                </tr>
                <tr>
                    <td><strong>Student-Developed Procedure</strong></td>
                    <td>Validates, creates, and stores user-submitted comments.</td>
                </tr>
                <tr>
                    <td><strong>Function Call</strong></td>
                    <td>Securely calls the procedure through an API endpoint.</td>
                </tr>
                <tr>
                    <td><strong>List Implementation</strong></td>
                    <td>Retrieves and stores multiple comments efficiently.</td>
                </tr>
                <tr>
                    <td><strong>List Processing</strong></td>
                    <td>Uses iteration (for loop) to process and format comment data.</td>
                </tr>
            </table>
        </div>

        <div class="section">
            <h2>🏆 Final Thoughts</h2>
            <p>This submission highlights my ability to design, implement, and process structured data in a web-based comment system.</p>
            <p>By using sequencing, selection, iteration, lists, and function calls, I successfully created a functional, interactive, and well-structured program for my AP CSP Create Performance Task.</p>
        </div>
    </div>

</body>
</html>
