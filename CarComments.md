---
layout: page
title: CarComments
permalink: CarComments
---

# **CPT BLOG - Comments of Car Posts**

## **Introduction**
Programming is a **collaborative and creative** process that brings ideas to life through software development. For my AP Computer Science Principles project, my team and I created a **Car Social Media Website**, where users can share and interact with posts about their favorite cars.

This blog follows the **AP Computer Science Principles (CSP) Create Performance Task (CPT)** requirements by documenting my **individual feature** in our group's program. This project **demonstrates the development process**, including **algorithmic implementation, data handling, and error management**. I will also explain how my feature meets the **College Board requirements** for **problem-solving, innovation, and collaboration**.

---

## **Purpose of the Feature**
### **Purpose of the Car Social Media Website**
The purpose of our **Car Social Media Website** is to create a platform where car enthusiasts can connect and share their passion. Users can post pictures of their favorite cars, comment on others’ posts, and engage in discussions.

### **Purpose of My Individual Feature: Comments System**
The **comments feature** enhances user interaction by allowing users to:
- **Post comments** on car posts.
- **View comments** to engage in discussions.
- **Edit their comments** to refine their input.
- **Delete comments** when necessary.

This feature fosters **community engagement and personal expression**, enabling users to interact with each other’s posts.

---

## **Input and Output**
### **How the Feature Works**
The comments system involves **two key processes**: **input** and **output**.

#### **Input:**
1. Users **enter a comment** in a text box on the frontend.
2. The **frontend sends this input** as a JSON payload (e.g., `content` and `post_id`) to the backend API via a `POST` request.

#### **Output:**
1. The **API processes the request** and stores the comment in the database.
2. The **API returns JSON responses** containing comment data (e.g., `content`, `user ID`, `post ID`, and `date posted`).
3. The **frontend dynamically displays** the comment using this response.

<img src="images/Screenshot 2025-01-27 at 11.23.03 PM.png" alt="POST API Endpoint Screenshot">

---

## **Full Stack Demonstration**
The frontend, built with HTML, CSS, and JavaScript, provides a clean interface for users to interact with the comments system. Users can submit comments, view all comments, and edit or delete their own comments. When a user writes a comment and clicks "Submit Comment," the frontend sends a `POST` request to the backend API.

<img src="images/Screenshot 2025-01-27 at 11.25.29 PM.png" alt="POST API Endpoint Screenshot">

To handle comment submissions, the JavaScript function looks like this:

<img src="images/Screenshot 2025-01-27 at 11.33.39 PM.png" alt="POST API Endpoint Screenshot">

The backend, built using Flask, supports CRUD operations for comments:
- **GET:** Retrieve all comments.  
- **POST:** Add a new comment.  
- **PUT:** Update an existing comment.  
- **DELETE:** Remove a comment.  

The `POST` endpoint processes new comments like this:

<img src="images/Screenshot 2025-01-27 at 11.37.18 PM.png" alt="POST API Endpoint Screenshot">

Error handling is managed with conditional checks for required fields:

<img src="images/Screenshot 2025-01-27 at 11.37.55 PM.png" alt="POST API Endpoint Screenshot">

The `CarComments` database model, defined using SQLAlchemy, manages the comment data structure. It includes methods to create, read, update, and delete comments.

<img src="images/Screenshot 2025-01-27 at 11.39.03 PM.png" alt="POST API Endpoint Screenshot">

---

## **Database Management & Data Handling**
### **Using `db_init`, `db_restore`, `db_backup` for Data Recovery**
To maintain database integrity, I tested database commands:
- **`db_init`**: Initializes the database.
- **`db_restore`**: Restores previous database states.
- **`db_backup`**: Backs up current data for recovery.

<img src="images/Screenshot 2025-01-31 at 9.10.47 AM.png" alt="POST API Endpoint Screenshot">
<img src="images/Screenshot 2025-01-30 at 10.23.59 PM.png" alt="POST API Endpoint Screenshot">

### **Use of Lists, Dictionaries & Database**
- **List Usage:** The backend retrieves **all comments** as a list of objects.
- **Dictionaries Usage:** Each comment is stored and returned as a **dictionary** (JSON object).

<img src="images/Screenshot 2025-01-30 at 10.25.17 PM.png" alt="POST API Endpoint Screenshot">

---

## **Formatting API Responses & Database Queries**
The API returns **structured JSON responses**, which are dynamically **rendered** into HTML using JavaScript.

<img src="images/Screenshot 2025-01-30 at 10.25.55 PM.png" alt="POST API Endpoint Screenshot">
<img src="images/Screenshot 2025-01-30 at 11.04.44 PM.png" alt="POST API Endpoint Screenshot">

---

## **Algorithmic Code Implementation**
This feature includes:
- **Sequencing:** Requests follow a structured sequence from input validation to database interaction and API response.
- **Selection:** Conditional statements handle missing data, errors, and access control.
- **Iteration:** Loops process multiple comments at once.

<img src="images/Screenshot 2025-01-30 at 10.28.09 PM.png" alt="POST API Endpoint Screenshot">

---

## **API Requests & Methods**
The API uses the following methods:
- **GET** - Retrieve all comments.
- **POST** - Add a new comment.
- **PUT** - Edit an existing comment.
- **DELETE** - Remove a comment.

<img src="images/Screenshot 2025-01-30 at 10.29.43 PM.png" alt="POST API Endpoint Screenshot">

---

## **Error Handling & Edge Cases**
- The API **checks for missing required fields** (`content`, `post_id`).
- Users can only **edit/delete their own comments**.
- The frontend **prevents blank comments from being submitted**.

<img src="images/Screenshot 2025-01-30 at 10.30.31 PM.png" alt="POST API Endpoint Screenshot">

---

## **Call to Algorithm: Fetching API Data**
- The frontend **calls the API** using JavaScript’s `fetch()`.
- The response is **processed and displayed dynamically**.

<img src="images/Screenshot 2025-01-30 at 10.38.01 PM.png" alt="POST API Endpoint Screenshot">

```js
[
    {
        "id": Number,
        "content": String,
        "uid": Number,
        "postid": Number,
        "date_posted": Datetime
    }
]
```

---

## **Handling Normal & Error Conditions**

<img src="images/Screenshot 2025-01-30 at 10.38.45 PM.png" alt="POST API Endpoint Screenshot">

### **Normal Condition**
- A comment is successfully posted, edited, or deleted.

### **Error Condition**
- API **rejects** request if `"content"` is missing.
- API **returns error code** if user tries to edit/delete another user’s comment.

<img src="images/Screenshot 2025-01-30 at 10.42.00 PM.png" alt="POST API Endpoint Screenshot">

---

## **Conclusion**
The **comments feature** enhances the **Car Social Media Website** by enabling users to share opinions, engage with others, and manage their content. Through the integration of **frontend, backend, and database components**, the feature demonstrates the **collaborative and creative nature of programming**.

By **following College Board CPT standards**, I ensured my feature:
✅ **Solves a problem & enables innovation**  
✅ **Includes structured input & output processing**  
✅ **Uses sequencing, selection, and iteration**  
✅ **Implements a well-documented API**  

<img src="images/Screenshot 2025-01-30 at 10.54.59 PM.png" alt="POST API Endpoint Screenshot">
