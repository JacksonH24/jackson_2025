---
layout: page
title: Snake Game
permalink: /snakegame/
---


<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Realistic Neon Snake Game</title>
    <style>
        body {
            margin: 0;
            background: linear-gradient(135deg, #000428, #004e92);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }
        canvas {
            display: block;
            background: #000;
            border: 5px solid #0ff;
            box-shadow: 0 0 20px #0ff, 0 0 40px #0ff, inset 0 0 50px #000;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas"></canvas>
    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");
        canvas.width = 800;
        canvas.height = 600;

        let snake = [{ x: 200, y: 200 }];
        let direction = { x: 20, y: 0 };
        let apple = randomPosition();
        let score = 0;
        let gameOver = false;

        function randomPosition() {
            return {
                x: Math.floor(Math.random() * (canvas.width / 20)) * 20,
                y: Math.floor(Math.random() * (canvas.height / 20)) * 20,
            };
        }

        function drawSnake() {
            snake.forEach((segment, index) => {
                const gradient = ctx.createRadialGradient(
                    segment.x + 10,
                    segment.y + 10,
                    5,
                    segment.x + 10,
                    segment.y + 10,
                    10
                );
                gradient.addColorStop(0, index === 0 ? "#ff0" : "#0ff"); // Yellow for head, blue for body
                gradient.addColorStop(1, "#00f");
                ctx.fillStyle = gradient;
                ctx.shadowBlur = 15;
                ctx.shadowColor = index === 0 ? "#ff0" : "#0ff";

                // Draw a circular segment
                ctx.beginPath();
                ctx.arc(segment.x + 10, segment.y + 10, 10, 0, Math.PI * 2);
                ctx.fill();
                ctx.closePath();

                // Add details for the head
                if (index === 0) {
                    // Eyes
                    ctx.fillStyle = "#fff";
                    ctx.beginPath();
                    ctx.arc(segment.x + 14, segment.y + 6, 2, 0, Math.PI * 2); // Right eye
                    ctx.fill();
                    ctx.closePath();

                    ctx.beginPath();
                    ctx.arc(segment.x + 6, segment.y + 6, 2, 0, Math.PI * 2); // Left eye
                    ctx.fill();
                    ctx.closePath();

                    // Mouth
                    ctx.strokeStyle = "#fff";
                    ctx.lineWidth = 1;
                    ctx.beginPath();
                    ctx.arc(segment.x + 10, segment.y + 13, 3, Math.PI * 0.2, Math.PI * 0.8); // Curved mouth
                    ctx.stroke();
                }
            });
        }

        function drawApple() {
            ctx.fillStyle = "#f00";
            ctx.shadowBlur = 25;
            ctx.shadowColor = "#f00";
            ctx.beginPath();
            ctx.arc(apple.x + 10, apple.y + 10, 10, 0, Math.PI * 2);
            ctx.fill();
            ctx.closePath();

            // Draw the apple leaf
            ctx.fillStyle = "#0f0";
            ctx.beginPath();
            ctx.arc(apple.x + 10, apple.y, 5, 0, Math.PI * 2);
            ctx.fill();
        }

        function updateSnake() {
            const head = { x: snake[0].x + direction.x, y: snake[0].y + direction.y };
            snake.unshift(head);

            if (head.x === apple.x && head.y === apple.y) {
                apple = randomPosition();
                score += 1;
            } else {
                snake.pop();
            }
        }

        function checkCollision() {
            const head = snake[0];
            if (
                head.x < 0 || head.x >= canvas.width ||
                head.y < 0 || head.y >= canvas.height ||
                snake.slice(1).some((segment) => segment.x === head.x && segment.y === head.y)
            ) {
                gameOver = true;
            }
        }

        function drawScore() {
            ctx.fillStyle = "#fff";
            ctx.shadowBlur = 0;
            ctx.font = "20px Arial";
            ctx.fillText(`Score: ${score}`, 10, 30);
        }

        function gameLoop() {
            if (gameOver) {
                ctx.fillStyle = "#fff";
                ctx.shadowBlur = 0;
                ctx.font = "40px Arial";
                ctx.fillText("Game Over!", canvas.width / 2 - 100, canvas.height / 2);
                ctx.font = "20px Arial";
                ctx.fillText("Press R to Restart", canvas.width / 2 - 80, canvas.height / 2 + 40);
                return;
            }

            ctx.clearRect(0, 0, canvas.width, canvas.height);
            drawApple();
            drawSnake();
            drawScore();
            updateSnake();
            checkCollision();
        }

        function restartGame() {
            snake = [{ x: 200, y: 200 }];
            direction = { x: 20, y: 0 };
            apple = randomPosition();
            score = 0;
            gameOver = false;
        }

        function handleInput(e) {
            if (e.code === "KeyW" && direction.y === 0) direction = { x: 0, y: -20 };
            if (e.code === "KeyS" && direction.y === 0) direction = { x: 0, y: 20 };
            if (e.code === "KeyA" && direction.x === 0) direction = { x: -20, y: 0 };
            if (e.code === "KeyD" && direction.x === 0) direction = { x: 20, y: 0 };
            if (e.code === "KeyR") restartGame();
        }

        window.addEventListener("keydown", (e) => {
            if (["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"].includes(e.code)) {
                e.preventDefault();
            }
        });

        document.addEventListener("keydown", handleInput);
        setInterval(gameLoop, 100);
    </script>
</body>
</html>
