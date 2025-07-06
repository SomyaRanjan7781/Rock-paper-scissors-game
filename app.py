from flask import Flask, request, jsonify
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app)  # ✅ Enable CORS to allow frontend requests
@app.route("/play", methods=["POST"])
def play():
    data = request.get_json()
    user_choice = data.get("choice")
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    # Determine result
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You Win!"
    else:
        result = "You Lose!"
    return jsonify({
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result
    })
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)