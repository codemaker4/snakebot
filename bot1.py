import snakeGame
import time

# Initialize the game
game = snakeGame.Game()

# Main game loop
while game.getGameOngoing():
    # Get the position of the snake
    snake_x, snake_y = game.getSnake()[0]

    # Get the position of the first apple
    apple_x, apple_y = game.getApples()[0]

    # Move the snake in the direction of the apple
    if snake_x != apple_x:
        game.move(1 if apple_x > snake_x else -1, 0)
    else:
        game.move(0, 1 if apple_y > snake_y else -1)

    time.sleep(0.1)
