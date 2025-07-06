document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".choice-button");
  const resultDiv = document.getElementById("result");
  const scoreDiv = document.getElementById("score");
  const playerChoiceSpan = document.getElementById("playerChoice");
  const computerChoiceSpan = document.getElementById("computerChoice");
  const playerEmojiDiv = document.getElementById("playerEmoji");
  const computerEmojiDiv = document.getElementById("computerEmoji");

  let playerScore = 0;
  let computerScore = 0;

  // 🌙 Theme toggle (if you have toggleTheme button in HTML)
  const toggleButton = document.getElementById("toggleTheme");
  if (toggleButton) {
    toggleButton.addEventListener("click", () => {
      document.body.classList.toggle("dark-theme");
      document.body.classList.toggle("light-theme");
    });
  }

  function getEmoji(choice) {
    if (choice === 'rock') return '✊';
    if (choice === 'paper') return '✋';
    if (choice === 'scissors') return '✌️';
    return '';
  }

  buttons.forEach(button => {
    button.addEventListener("click", () => {
      const choice = button.getAttribute("data-choice");

      // ✅ Use your Render backend URL below
      fetch("https://rock-paper-scissors-game-yj93.onrender.com", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ choice: choice })
      })
      .then(response => response.json())
      .then(data => {
        playerChoiceSpan.innerText = data.user_choice;
        computerChoiceSpan.innerText = data.computer_choice;
        playerEmojiDiv.innerText = getEmoji(data.user_choice);
        computerEmojiDiv.innerText = getEmoji(data.computer_choice);

        if (data.result.includes('Win')) {
          playerScore++;
          document.getElementById("winSound").play();
        } else if (data.result.includes('Lose')) {
          computerScore++;
          document.getElementById("loseSound").play();
        } else {
          document.getElementById("tieSound").play();
        }

        resultDiv.innerText = data.result;
        scoreDiv.innerText = `Player: ${playerScore} | Computer: ${computerScore}`;
      })
      .catch(error => {
        console.error("Error:", error);
        resultDiv.innerText = "Server error.";
      });
    });
  });
});
