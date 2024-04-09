import snakeGame
import time

# Initialize the game
game = snakeGame.Game()


# Make a cycle that covers the entire game field
cycle = []
if game.getSize() % 2 == 0:
    for x in range(0, game.getSize(), 2):
        for y in range(1, game.getSize()):
            cycle.append((x, y))
        for y in range(game.getSize()-1, 0, -1):
            cycle.append((x+1, y))
    for x in range(game.getSize()-1, -1, -1):
        cycle.append((x, 0))
else:
    print("The game field must have an even size.")


# Print the cycle for debugging
# for i in range(len(cycle)):
#     for y in range(game.getSize()):
#         for x in range(game.getSize()):
#             print('X' if cycle.index((x, y)) <= i else '.', end='')
#         print("")
#     time.sleep(0.1)


# Main game loop
while game.getGameOngoing():
    # Get the position of the snake
    snake = game.getSnake()[0]

    # Get the position of the snake in the cycle
    snake_index = cycle.index(snake)

    # make the snake move to the next point in the cycle
    x, y = cycle[(snake_index + 1) % len(cycle)]
    game.move(x - snake[0], y - snake[1])

    time.sleep(0.1)
