import gradio as gr
import random

# 🌟 Initialize scores globally
player_score = 0
computer_score = 0

def play(user_choice):
    global player_score, computer_score

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    # Determine result
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You Win!"
        player_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    return (f"✊ You chose: {user_choice}\n"
            f"💻 Computer chose: {computer_choice}\n"
            f"🎯 Result: {result}\n\n"
            f"📊 Scores => Player: {player_score} | Computer: {computer_score}")

with gr.Blocks(css="""
body {
  background: url('https://img.freepik.com/free-vector/children-playing-rock-paper-scissors_1308-33220.jpg') no-repeat center center fixed;
  background-size: cover;
}
.gradio-container {
  background-color: rgba(255, 255, 255, 0.85);
  border-radius: 15px;
  padding: 20px;
  max-width: 400px;
  margin: auto;
  margin-top: 50px;
}
h1, h2, h3 {
  color: black; /* 🖤 heading color changed to black */
  text-align: center;
}
""") as demo:
    gr.Markdown("## ✊ ✋ ✌️ Rock Paper Scissors Game")
    with gr.Row():
        with gr.Column():
            user_choice = gr.Radio(["rock", "paper", "scissors"], label="Choose Rock, Paper, or Scissors")
            play_button = gr.Button("Submit")
        output = gr.Textbox(label="output", lines=6)
    play_button.click(fn=play, inputs=user_choice, outputs=output)
demo.launch()