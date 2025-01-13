---
layout: page
title: MCQ Blog
permalink: mcq blog
---

Engaging with the quiz was an insightful experience, providing a clear picture of my strengths and areas needing improvement. Here's a detailed breakdown of what I learned, the topics I need to focus on, and corrections to any mistakes I made.

What I Learned
Strengths:

My performance in topics like Binary Numbers (100%), Boolean Expressions (100%), Beneficial and Harmful Effects (100%), and Safe Computing (100%) demonstrates a solid understanding of fundamental concepts.
I excel in areas requiring logical reasoning, such as Developing Procedures (100%), and technical topics like The Internet (100%) and Fault Tolerance (100%).
Weaknesses:

I struggled significantly with Identifying and Correcting Errors (25%), Lists (0%), Algorithmic Efficiency (0%), and Using Programs with Data (0%). These areas involve debugging, algorithm optimization, and working with data—key skills for effective programming and computational thinking.
Surprising Areas:

My lower scores in Mathematical Expressions (0%), despite its straightforward nature, suggest a need to revisit and refine fundamental mathematical operations in programming contexts.
Data Compression (67%) and Extracting Information from Data (57%) highlight some inconsistencies in understanding data representation and analysis.
Topics I Feel Weak On
Debugging and Error Correction:
With only 25% accuracy in Identifying and Correcting Errors, I need to practice debugging systematically and understanding error patterns.

Data-Related Topics:
My low performance in Using Programs with Data (0%), Lists (0%), and Algorithmic Efficiency (0%) indicates a lack of familiarity with handling data effectively, which is crucial for solving computational problems efficiently.

Complex Program Structures:
Topics like Nested Conditionals and Iteration, with scores around 50%, highlight difficulty with designing and implementing complex logic structures.

Corrections on Mistakes
Here are specific corrections for questions I got wrong:

Identifying and Correcting Errors (25%):
I often missed identifying logical errors in code. Going forward, I will:

Break code into smaller sections for analysis.
Use debugging tools to isolate issues systematically.
Using Programs with Data (0%):
I misunderstood how data is processed within programs. I’ll review examples of data parsing, transformation, and visualization.

Mathematical Expressions (0%):
I struggled with operator precedence and numerical calculations in code. I’ll revisit basic programming math concepts and solve more practice problems.

Algorithmic Efficiency (0%):
I lacked clarity on optimizing algorithms. I'll study time complexity (e.g., Big-O notation) and practice optimizing existing code.

Developing Algorithms (25%):
Errors here came from not planning algorithm logic clearly. I need to focus on breaking down problems into smaller, solvable components.

Steps to Improve
Focus on Weak Areas:
I'll dedicate more time to practicing error correction, data manipulation, and algorithm development.

Practice Through Application:
Solving real-world problems and participating in coding challenges will help reinforce theoretical knowledge.

Use Debugging Tools:
I’ll familiarize myself with debugging software to improve error identification skills.

Revise Basics:
Revisiting foundational topics like Lists, Iteration, and Mathematical Expressions will strengthen my programming fundamentals.


This quiz provided valuable insights into my current skill level. While I have strong foundational knowledge, my performance shows room for improvement in handling errors, working with data, and optimizing algorithms. With a focused plan, I am confident I can turn these weaknesses into strengths.


SPECIFIC CORRECTIONS:

Q14: Comparing loop algorithms: I originally chose answer A. Program A displays values from 1 to 10 because it displays i before incrementing. Program B displays values from 2 to 11 because it increments i first, then displays. Both programs output the same number of values (10), but the values are different, making C the correct answer.

Q21: I originally chose A. The robot needs to move 2 steps forward, turn right once, and then move 3 steps forward to reach the gray square. Option B executes this sequence correctly: MoveXTimes 2, RightXTimes 1, and MoveXTimes 3. Options A, C, and D fail because they don't follow this exact movement pattern. I didn't take enough time with this question.

Q30: I originally chose C. The program calls the Analysis procedure once for "science fiction" (1 hour) and then once for each of the 4 genres in the list ("comedy," "drama," "mystery," "romance"), totaling 5 calls. Since each call takes 1 hour, the program takes 5 hours to execute, making D the correct answer.

Q31: I originally chose B. This question tests your understanding of how the order of operations (incrementing vs. displaying) in a loop affects the program's output. Program A displays i before incrementing, while Program B increments i before displaying, leading to different sequences of values but the same number of outputs. The correct answer is C: Program A and Program B display the same number of values, but the values differ.

Q41: I initially answered this question incorrectly because I misunderstood how the total score is calculated. I thought the higher score alone determined the total, but the correct approach involves adding the higher of the two scores (midterm or final) to the original final exam score. This means the procedure should account for both the replacement rule and the inclusion of the final exam score in the total. The correct answer is B: adjustedTotal ← Max(midtermExam, finalExam) + finalExam.

Q55: I initially answered this question incorrectly because I misunderstood how the logic in the procedure works. The condition in the IF statement checks if the response is both "y" and "yes", which is impossible for a single input. As a result, the procedure always skips the RETURN(true) statement and defaults to RETURN(false) regardless of the input. The correct answer is D: The procedure returns false no matter what the input value is.


Sprint 3 REVIEW:

Song Voting Web App Explanation


I created a Song of the Day Voting app where users can vote for their favorite song, see current vote results, and get an error if they try to vote multiple times.


Frontend (HTML & CSS):

HTML: The page includes a voting section with a song dropdown and a vote button, and a results section to display votes.

CSS: Styles the page with a clean layout, interactive buttons, and readable vote results.



JavaScript (Voting Logic):

Local Storage: Stores votes and user voting history to persist data even after a page reload.

Vote Casting: Users select a song and click "Vote." The script checks if they've already voted. If not, it adds their vote and updates the vote count.

Error Handling: Displays an error if the user tries to vote again for the same song.


How It Works:
When a user votes, the vote is saved in local storage, and the results are displayed dynamically without reloading the page.





