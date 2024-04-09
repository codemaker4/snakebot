import snakeGame
import time

# Initialize the game
game = snakeGame.Game()

# Main game loop
while game.getGameOngoing():
    # Get the position of the snake
    snake_x, snake_y = game.getSnake()[0]

    # Get the position of the nearest apple
    apple_x, apple_y = min(game.getApples(),
                           key=lambda apple: abs(apple[0] - snake_x) +
                           abs(apple[1] - snake_y))

    # Possible moves
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Sort moves by their distance to the apple
    moves.sort(key=lambda move: abs((snake_x + move[0]) - apple_x) +
               abs((snake_y + move[1]) - apple_y))

    # Try each move
    for move in moves:
        new_x, new_y = snake_x + move[0], snake_y + move[1]

        # If the field is not safe, try the next move instead
        if game.getField(new_x, new_y) in snakeGame.DANGERTILES:
            continue

        game.move(*move)
        break
    else:
        # If no safe moves are left, make the snake run into itself
        game.move(*moves[0])

    time.sleep(0.1)
