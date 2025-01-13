from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# List of trivia questions and answers
questions = [
    {"question": "Who is known as the 'King of Pop'?", "answer": "Michael Jackson"},
    {"question": "Which song holds the record for the most weeks at number one on the Billboard Hot 100?", "answer": "Old Town Road"},
    {"question": "What band is known for the song 'Bohemian Rhapsody'?", "answer": "Queen"},
    {"question": "Who is the female artist behind the song 'Rolling in the Deep'?", "answer": "Adele"},
    {"question": "Which famous musician was known for wearing a 'meat dress'?", "answer": "Lady Gaga"}
]

@app.route('/get_question', methods=['GET'])
def get_question():
    """Provide a random music trivia question."""
    question = random.choice(questions)
    return jsonify({"question": question["question"], "id": questions.index(question)})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    """Check the user's answer."""
    data = request.json
    question_id = data.get("question_id")
    user_answer = data.get("answer").strip().lower()

    correct_answer = questions[question_id]["answer"].lower()

    if user_answer == correct_answer:
        return jsonify({"correct": True, "message": "Correct!"})
    else:
        return jsonify({"correct": False, "message": "Incorrect. Try again!"})

if __name__ == '__main__':
    app.run(debug=True)
