# Maak je snake bot!
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

Je eigen bot moet rond het niveau van bot3 zitten. Dus langer in de toekomst denken dan alleen een tegel. `bot3.py` is trouwens ook niet perfect, dus als je het leuk vindt kan je proberen om een nog betere bot te maken.

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



