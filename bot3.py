import snakeGame
from queue import PriorityQueue
import time

# Initialize the game
game = snakeGame.Game()


# Define the A* pathfinding algorithm
def a_star(start, goal, neighbors_func, heuristic_func):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        _, current = frontier.get()

        if current == goal:
            break

        for next in neighbors_func(current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic_func(goal, next)
                frontier.put((priority, next))
                came_from[next] = current

    if current != goal:
        return []

    path = []
    while current is not None:
        path.append(current)
        current = came_from.get(current, None)
    path.reverse()

    return path


# Define the neighbors function
def neighbors(node):
    x, y = node
    directions = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    return [
        dir for dir in directions if
        0 <= dir[0] < game.getSize() and
        0 <= dir[1] < game.getSize() and
        game.getField(dir[0], dir[1]) in snakeGame.SAFETILES]


# Define the heuristic function
def heuristic(goal, node):
    return abs(goal[0] - node[0]) + abs(goal[1] - node[1])


# Main game loop
while game.getGameOngoing():
    # Get the position of the snake
    snake = game.getSnake()[0]

    apple = min(game.getApples(), key=lambda apple: heuristic(snake, apple))
    path = a_star(snake, apple, neighbors, heuristic)

    # If a path was found, move the snake along the path
    if path:
        next_move = path[1]
        game.move(next_move[0] - snake[0], next_move[1] - snake[1])
    else:
        # If no path was found, make the snake hug a wall
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            next_move = (snake[0] + dx, snake[1] + dy)
            if (0 <= next_move[0] < game.getSize() and
                    0 <= next_move[1] < game.getSize() and
                    game.getField(next_move[0], next_move[1]) not in
                    [snakeGame.SNAKE, snakeGame.WALL]):
                game.move(dx, dy)
                break
        else:
            # If no safe moves are left, make the snake run into itself
            game.move(*directions[0])

    time.sleep(0.1)
