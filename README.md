# Create your snake bot!
(Nederlandse vertaling onderaan)
Here you can create your own bot for the snake game. The snake game is a game where you control a snake that needs to eat apples. When the snake eats an apple, the snake gets longer. If the snake hits the wall or itself, the game is over.

## How does it work?
The snakeGame.py file contains the code for the snake game. The code is already complete, so you don't need to change anything. All you have to do is create a bot that controls the snake.
- Create a new python file in the same directory as snakeGame.py
- Import the snakeGame module in your new python file with
`import snakeGame`
- Start a game with `game = snakeGame.Game()`
- Use `game.move(dx, dy)` to move the snake. dx and dy are the changes in x and y direction. dx and dy can be -1, 0 or 1. For example, `game.move(1, 0)` moves the snake to the right and `game.move(0, -1)` moves the snake up.
- You can print the current game board with `print(game)`
- `game.gameOngoing()` is a boolean that indicates whether the game is still ongoing. If the game is over, `game.gameOngoing()` is False. You can use this for a while loop.

## HOLD ON, STOP!
You can read the full and detailed explanation below, but it's much more fun to just play around with this interface. Try to move the snake in a straight line with a simple while loop.

One rule: **Do not edit the code in snakeGame.py** and **do not use functions with an underscore (_) in the name** such as `game._setField()` and `game._moveSnake()`. If you do, you're cheating. You can only use `game.move()` and the other functions without an underscore.

Oh and pro tip: I've already made some example bots:
- `bot1.py` just moves the snake to an apple. A good starting point for your own bot.
- `bot2.py` first checks if the next tile is safe, which is a good explanation of how you can use `game.getField()`.
- `bot3.py` uses an advanced algorithm to find a completely safe route to the apple. Reading the code of this is not very useful, but you can use it to see how good your own bot is.
- `bot4.py` cycles through the field, without calculating the shortest path to an apple. This bot can always reach the maximum length with which it fills the entire field, but is not very efficient at picking up apples.

Look around and experiment. If you get stuck, you can always read the full explanation below.

## The rest of the explanation

- With `game.getField(x, y)` you can request a character from the playing field.
    - `snakeGame.WALL` is the character for a wall ("#")
    - `snakeGame.SNAKE` is the snake ("+")
    - `snakeGame.APPLE` is an apple ("A")
    - `snakeGame.EMPTY` is an empty field (" ")
    - `snakeGame.HEAD` is the head of the snake ("O")

    example:
    ```python
    if game.getField(3, 5) == snakeGame.WALL:
        print("There is a wall at position 3, 5")
    ```
    - There are also `snakeGame.SAFETILES` and `snakeGame.DANGERTILES`. These are lists with respectively safe and dangerous characters.

    example:
    ```python
    if game.getField(3, 5) in snakeGame.SAFETILES:
        print("It is safe to move to position 3, 5")
    ```

- With `game.getSnake()` you can request the position of the snake. This gives a list of tuples with the x and y position of the snake. The first tuple is the head of the snake and the last tuple is the tail of the snake.

    example:
    ```python
    snake = game.getSnake()
    print("The snake is at position", snake[0])
    ```

- `game.getApples()` works the same as `game.getSnake()`, but for the apples. (It's a list because this game supports more than 1 apple. Look at the documentation of `snakeGame.Game()` if you want to try this. It's not necessary for this assignment, so you can just use `game.getApples()[0]`.)


# Maak je snake bot! (NL)
Hier kan je een iegen bot maken voor de snake game. De snake game is een spel waarbij je een slang bestuurt die appels moet eten. Als de slang een appel eet, wordt de slang langer. Als de slang tegen de muur of tegen zichzelf aan botst, is het spel afgelopen.

## Hoe werkt het?
Het snakeGame.py bestand bevat de code voor de snake game. De code is al helemaal af, dus je hoeft hier niets aan te veranderen. Het enige wat je hoeft te doen is een bot maken die de snake bestuurt.
- Maak een nieuwe python file aan in dezelfde map als snakeGame.py
- Importeer de snakeGame module in je nieuwe python file met
`import snakeGame`
- Start een spel met `game = snakeGame.Game()`
- gebruik `game.move(dx, dy)` om de snake te bewegen. dx en dy zijn de veranderingen in x en y richting. dx en dy kunnen -1, 0 of 1 zijn. Bijvoorbeeld `game.move(1, 0)` beweegt de snake naar rechts en `game.move(0, -1)` beweegt de snake omhoog.
- Je kan het huidige spelbord uitprinten met `print(game)`
- `game.gameOngoing()` is een boolean die aangeeft of het spel nog bezig is. Als het spel afgelopen is, is `game.gameOngoing()` False. Dit kan je voor een while loop gebruiken.

## HO, STOP!
Je kan de volledige en gedetailleerde uitleg hieronder lezen, maar het is veel leuker om gewoon meteen een beetje rond te spelen met deze interface. Probeer de snake eens in een rechte lijn te laten bewegen met een simpele while loop.

Een regel: **Bewerk de code in snakeGame.py niet** en **gebruik geen functies met een underscore (_) in de naam** zoals `game._setField()` en `game._moveSnake()`. Als je dit wel doet, speel je vals. Je mag alleen `game.move()` gebruiken en de andere functies zonder underscore.

Oh en protip: ik heb al wat voorbeeld bots gemaakt:
- `bot1.py` beweegt de slang gewoon naar een apppel. Een goed startpunt voor je eigen bot.
- `bot2.py` kijkt eerst of de volgende tegel wel vleilig is, wat een goede uitleg is van hoe je `game.getField()` kan gebruiken.
- `bot3.py` gebruikt een geavanceerd algoritme om een volledige veilige route naar de appel te vinden. Het lezen van de code hiervan is niet erg nuttig, maar je kan het wel gebruiken om te zoen hoe goed je eigen bot is.
- `bot4.py` gaag in een cyclus door het veld, zonder het kortste pad naar een appel te berekenen. Deze bot kan altijd de maximale lengte berijken waarmee hij het hele veld vult, maar is niet erg efficiënt met het oppakken van appels.

Kijk een beetje rond en experimenteer. Als je vast zit, kan je altijd nog de volledige uitleg hieronder lezen.

## De rest van de uitleg

- met `game.getField(x, y)` kan je een karakter van het speelveld opvragen.
    - `snakeGame.WALL` is het karakter voor een muur ("#")
    - `snakeGame.SNAKE` is de slang ("+")
    - `snakeGame.APPLE` is een appel ("A")
    - `snakeGame.EMPTY` is een leeg veld (" ")
    - `snakeGame.HEAD` is de kop van de slang ("O")

    voorbeeld:
    ```python
    if game.getField(3, 5) == snakeGame.WALL:
        print("Er is een muur op positie 3, 5")
    ```
    - Er zijn ook `snakeGame.SAFETILES` en `snakeGame.DANGERTILES`. Dit zijn lijsten met respectievelijk veilige en gevaarlijke karakters.

    voorbeeld:
    ```python
    if game.getField(3, 5) in snakeGame.SAFETILES:
        print("Het is veilig om naar positie 3, 5 te bewegen")
    ```

- met `game.getSnake()` kan je de positie van de slang opvragen. Dit geeft een lijst van tuples met de x en y positie van de slang. De eerste tuple is de kop van de slang en de laatste tuple is de staart van de slang.

    voorbeeld:
    ```python
    snake = game.getSnake()
    print("De slang is op positie", snake[0])
    ```

- `game.getApples()` werkt hetzelfde als `game.getSnake()`, maar dan voor de appels. (Het is een lijst omdat dit spel meer dan 1 appels support. Kijk naar de documenatie van `snakeGame.Game()` als je dit wilt proberen. Het is niet nodig voor deze opdracht, dus je kan gewoon `game.getApples()[0]` gebruiken.)



