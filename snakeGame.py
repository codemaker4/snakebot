import random
import copy

WALL = '#'
EMPTY = ' '
APPLE = 'A'
SNAKE = '+'
HEAD = 'O'
SAFETILES = [EMPTY, APPLE]
DANGERTILES = [WALL, SNAKE, HEAD]
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DIRECTIONNAMES = {(-1, 0): "left",
                  (1, 0): "right",
                  (0, -1): "up",
                  (0, 1): "down"}
DIRECTIONICONS = {(-1, 0): "<",
                  (1, 0): ">",
                  (0, -1): "^",
                  (0, 1): "v"}


class Game:
    def __init__(self, size=10, apples=1, walls=0):
        """
        Initialize the SnakeGame object.

        Args:
            size (int): The size of the game field.
            apples (int): The number of apples in the game.
            walls (int): The number of walls in the game.

        Raises:
            ValueError: If the size is less than 5.

        """
        if size < 5:
            raise ValueError("Field too small.")
        self._size = size

        self._field = []
        for i in range(size):
            self._field.append([EMPTY] * size)

        self._snake = [(int(size/2), 1)]
        self._setField(*self._snake[0], HEAD)
        self._snakeGoalLenth = 3

        self._gameOngoing = True
        self._statusString = "Playing"
        self._moves = 0

        for i in range(walls):
            x, y = self._getRandomEmptyCoords()
            self._setField(x, y, WALL)

        self._apples = []
        for i in range(apples):
            x, y = self._getRandomEmptyCoords()
            self._setField(x, y, APPLE)
            self._apples.append((x, y))

    def __repr__(self) -> str:
        """
        This method returns a string representation of the game state. This is
        used for debugging purposes.
        It represents the game board with the snake, walls, and apple.

        Returns:
            str: A string representation of the game state.
        """
        LEFTPAD = len(str(self._size)) + 1

        coords = [i for i in range(0, self._size)
                  if i == 0 or i == self._size - 1
                  or (i % 5 == 0 and i < self._size - 3)]
        string = 'SNAKE GAME:\n'
        string += f'Status: {self._statusString}\n'
        string += f'Moves: {self._moves}\n'
        string += f'Snake length: {self._snakeGoalLenth}\n'

        string += ' ' * LEFTPAD
        lastCoord = -1
        for coord in coords:
            string += ' ' * (coord - lastCoord)
            string += str(coord)
            lastCoord = coord + len(str(coord))
        string += '\n'

        for y in range(-1, self._size + 1):
            string += (f'{(y):>{LEFTPAD - 1}} '
                       if (y) in coords else ' ' * LEFTPAD)
            for x in range(-1, self._size + 1):
                string += self.getField(x, y)
            string += '\n'

        return string

    def getGameOngoing(self) -> bool:
        """
        This method returns the current state of the game.

        Returns:
            bool: True if the game is ongoing, False otherwise.
        """
        return self._gameOngoing

    def getSize(self) -> int:
        """
        This method returns the size of the game field.

        Returns:
            int: The size of the game field.
        """
        return self._size

    def getMoves(self) -> int:
        """
        This method returns the number of moves made in the game.

        Returns:
            int: The number of moves made in the game.
        """
        return self._moves

    def getField(self, x: int, y: int) -> str:
        """
        Returns the content of the field at the given coordinates.
        If the coordinates are out of bounds, it returns a wall. Otherwise, it
        returns the content of the field.

        Parameters:
            x (int): The x-coordinate of the field.
            y (int): The y-coordinate of the field.

        Returns:
            str: The content of the field at the given coordinates.
        """
        if (x < 0 or x >= self._size):
            return WALL
        if (y < 0 or y >= self._size):
            return WALL
        return self._field[x][y]

    def _setField(self, x: int, y: int, thing: str):
        """
        Sets the content of the field at the given coordinates to the given
        thing.
        If the coordinates are out of bounds, it raises an IndexError.

        Parameters:
            x (int): The x-coordinate of the field.
            y (int): The y-coordinate of the field.
            thing (str): The thing to set at the given coordinates.

        Raises:
            IndexError: If the coordinates are out of bounds.
        """
        if (x < 0 or x >= self._size):
            raise IndexError("Tried to set value out of the field.")
        if (y < 0 or y >= self._size):
            raise IndexError("Tried to set value out of the field.")
        self._field[x][y] = thing

    def _getRandomCoords(self) -> tuple[int, int]:
        """
        Generates and returns a tuple of random coordinates within the game
        field.

        Returns:
            tuple[int, int]: A tuple of two integers representing the x and y
            coordinates.
        """
        return (random.randint(0, self._size - 1),
                random.randint(0, self._size - 1))

    def _getRandomEmptyCoords(self) -> tuple[int, int]:
        """
        Generates and returns a tuple of random coordinates for an empty field
        within the game. If no empty field is found, it raises a RuntimeError.

        Returns:
            tuple[int, int]: A tuple of two integers representing the x and y
            coordinates of an empty field.

        Raises:
            RuntimeError: If no empty field is found.
        """
        for i in range(10):
            x, y = self._getRandomCoords()
            if self.getField(x, y) == EMPTY:
                return (x, y)

        # The field is almost full, so let's make a list of all empty tiles.
        options = []
        for x in range(self._size):
            for y in range(self._size):
                if self.getField(x, y) == EMPTY:
                    options.append((x, y))

        if len(options) == 0:
            raise RuntimeError("Could not add empty, field is full.")
        return random.choice(options)

    def _moveSnake(self, dx: int, dy: int):
        """
        Moves the snake in the specified direction by updating its position on
        the game field.

        Args:
            dx (int): The change in x-coordinate for the snake's movement.
            dy (int): The change in y-coordinate for the snake's movement.
        """
        x, y = self._snake[0]
        x += dx
        y += dy
        self._setField(x, y, HEAD)
        self._setField(*self._snake[0], SNAKE)
        self._snake.insert(0, (x, y))
        if len(self._snake) > self._snakeGoalLenth:
            self._setField(*self._snake[-1], EMPTY)
            self._snake.pop()

    def getSnake(self) -> list[tuple[int, int]]:
        """
        Get a list of all parts of the snake on the board.

        It is a list of tuples, so `x, y = getSnake()[0]` can be used to get
        the coordinates of the part of the snake, which is the head.

        Returns:
            list[tuple[int, int]]: A list of tuples representing the
            coordinates of each part of the snake.
        """
        return copy.deepcopy(self._snake)

    def getApples(self) -> list[tuple[int, int]]:
        """
        Get a list of all apples on the board.

        It is a list of tuples, so `x, y = getApples()[0]` can be used to get
        the coordinates of an apple.

        Returns:
            list[tuple[int, int]]: A list of tuples representing the
            coordinates of each apple on the board.
        """
        return copy.deepcopy(self._apples)

    def move(self, dx: int, dy: int, verbose=3) -> bool:
        """
        Play the game with this function!

        With dx and dy, you give the direction to move.
        One of them is 0, and the other is eiher 1 or -1.

        The optional verbose option is used to specify wether or not to print
        out the game all of the time.

        0 = print nothing.
        1 = only print errors and game endings.
        2 = also print when an apple was eaten.
        3 (default) = print everything always.

        This returns True if the game continues, or False on game over.
        """
        if not self._gameOngoing:
            return False
        if (dx, dy) not in DIRECTIONS:
            raise ValueError("""Invalid movement. (dx, dy) must be a cardinal
                             movement of 1.""")
        x, y = self._snake[0]
        x += dx
        y += dy
        newHeadTile = self.getField(x, y)

        if newHeadTile == WALL or newHeadTile == SNAKE:
            self._gameOngoing = False
            if newHeadTile == WALL:
                self._statusString = "Game Over: You slithered into a wall " +\
                    f"while moving {DIRECTIONNAMES[(dx, dy)]}"
            elif newHeadTile == SNAKE:
                self._statusString = "Game Over: You slithered into " +\
                    f"yourself while moving {DIRECTIONNAMES[(dx, dy)]}"
            self._setField(*self._snake[0], DIRECTIONICONS[(dx, dy)])
            if verbose >= 1:
                print(self)
            return False

        if newHeadTile == APPLE:
            self._snakeGoalLenth += 1
            self._apples.remove((x, y))
            if verbose >= 2:
                print("##### Yum! You ate an apple!")

        if newHeadTile == APPLE or newHeadTile == EMPTY:
            self._moveSnake(dx, dy)

        if newHeadTile == APPLE:
            try:
                newApple = self._getRandomEmptyCoords()
                self._apples.append(newApple)
                self._setField(*newApple, APPLE)
            except ():
                if len(self._apples) == 0:
                    if verbose >= 1:
                        print("##### Field is full, you won!")
                    self._statusString = "Field is full, you won!"
                    return False

        if verbose >= 3:
            print(self)

        self._moves += 1
        return True


if __name__ == "__main__":
    game = Game()

    while game.getGameOngoing():
        print(game)

        direction = input("Enter direction (WASD): ")
        direction_map = {"w": (0, -1), "a": (-1, 0), "s": (0, 1), "d": (1, 0)}
        dx, dy = direction_map.get(direction.lower(), (0, 0))

        if (dx, dy) == (0, 0):
            print("Invalid direction.")
            continue

        game.move(dx, dy)

    print(game)
    print("Game over!")
