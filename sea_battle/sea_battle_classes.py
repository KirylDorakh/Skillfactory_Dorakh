import random
#Игра
class Game:
    def __init__(self, player=None, n=0, coords=None):
        self.player = player
        self.n = n
        self.coords = coords
        self.player_history = []
        self.player_near_history = []
        self.ai_history = []
        field = [['◌' for j in range(6)] for i in range(6)]
        self.field = field
        self.ship = "■"

    # Приветствие и правила
    @staticmethod
    def hello():
        print("---------------------------")
        print("        Морской бой")
        print("---------------------------")

    # Ввод координат
    def inputCoords(self, num=None):
        x = 0
        y = 0
        print(num, 'num')
        print("---------------------------")
        while True:
            while not (1 <= x <= 6):
                try:
                    x = int(input('Выберете строку от 1 до 6:'))
                    if not (1 <= x <= 6):
                        raise ValueError
                except ValueError:
                    print("Введено неверное значение")
                else:
                    print(f"Вы ввели значение {x}")
            while not (1 <= y <= 6):
                try:
                    y = int(input('Выберете столбец от 1 до 6:'))
                    if not (1 <= y <= 6):
                        raise ValueError
                except ValueError:
                    print("Введено неверное значение")
                else:
                    print(f"Вы ввели значение {y}")
            val = x, y
            if not num:
                coords = list(val)
                return coords
            if num == '2' and val == (6, 6):
                print('Недопустимая координата для двухпалубного корабля')
                return self.inputCoords('2')
            if num == '3' and (val == (6, 6) or val == (5, 6) or val == (5, 5) or val == (6, 5)):
                print('Недопустимая координата для двухпалубного корабля')
                return self.inputCoords('3')
            else:
                coords = list(val)
                return coords

    # Ввод рандомных координат для ИИ
    def inputRandomCoords(self, num=None):
        x = 0
        y = 0
        print(num, 'num')
        print("---------------------------")
        while True:
            while not (1 <= x <= 6):
                try:
                    x = random.randint(0, 6)
                    if not (1 <= x <= 6):
                        raise ValueError
                except ValueError:
                    print("Введено неверное значение")
                else:
                    print(f"Вы ввели значение {x}")
            while not (1 <= y <= 6):
                try:
                    y = random.randint(0, 6)
                    if not (1 <= y <= 6):
                        raise ValueError
                except ValueError:
                    print("Введено неверное значение")
                else:
                    print(f"Вы ввели значение {y}")
            val = x, y
            if not num:
                coords = list(val)
                return coords
            if num == '2' and val == (6, 6):
                print('Недопустимая координата для двухпалубного корабля')
                return self.inputRandomCoords('2')
            if num == '3' and (val == (6, 6) or val == (5, 6) or val == (5, 5) or val == (6, 5)):
                print('Недопустимая координата для двухпалубного корабля')
                return self.inputRandomCoords('3')
            else:
                coords = list(val)
                return coords


    # выбор горизонтального или вертикального расположения
    def chooseView(self):
        print('---------------------------')
        val = 0
        print("Коориданты носа коробля", self.coords)
        while True:
            while not (1 <= val <= 2):
                try:
                    val = int(input('Введите 1 для горизонтального расположения '
                                        'или 2 для вертикального корабля:'))
                    if not (0 <= val <= 1):
                        raise ValueError
                except ValueError:
                    print("Нужно выбрать между 1 и 2")
                else:
                    print(f"Вы ввели значение {val}")
            return val


    def randomChooseView(self):
        print('---------------------------')
        val = 0
        print("Коориданты носа коробля", self.coords)
        while True:
            while not (random.randint(1,2)):
                try:
                    val = int(input('Введите 1 для горизонтального расположения '
                                        'или 2 для вертикального корабля:'))
                    if not (0 <= val <= 1):
                        raise ValueError
                except ValueError:
                    print("Нужно выбрать между 1 и 2")
                else:
                    print(f"Вы ввели значение {val}")
            return val

    # горизонтальное расположение
    def horizontal(self):
        self.secondcoords = [self.coords[0], self.coords[1] + 1]
        print('вторая координата', self.secondcoords)
        return self.secondcoords

    # вертикальное расположение
    def vertical(self):
        self.secondcoords = [self.coords[0] + 1, self.coords[1]]
        print('вторая координата', self.secondcoords)
        return self.secondcoords

    # вертикальное горизонтального или вертикального расположения
    def horizOrVert(self, num=None):
        if self.coords[1] == 6:
            print(f'Только вертикальное расположение корабля доступно для координаты {self.coords}')
            print('---------------------------')
            return self.vertical()

        if self.coords[0] == 6:
            print(f'Только горизонтальное расположение корабля доступно для координаты {self.coords}')
            print('---------------------------')
            return self.horizontal()

        if num == '3' and self.coords[1] == 5:
            print(f'Только вертикальное расположение корабля доступно для координаты {self.coords}')
            print('---------------------------')
            return self.vertical()

        if num == '3' and self.coords[0] == 5:
            print(f'Только горизонтальное расположение корабля доступно для координаты {self.coords}')
            print('---------------------------')
            return self.horizontal()

        val = self.chooseView()
        if val == 1:
            print('Вы выбрал горизонтальное расположение корабля')
            print('---------------------------')
            return self.horizontal()
        if val == 2:
            print('ВЫ выбрал вертикальное расположение корабля')
            print('---------------------------')
            return self.vertical()

    def horizOrVertForThree(self):
        val = self.horizOrVert('3')
        print('val', val)
        if val == self.horizontal():
            self.thirdcoords = [self.coords[0], self.coords[1] + 2]
        if val == self.vertical():
            self.thirdcoords = [self.coords[0] + 2, self.coords[1]]
        return val + self.thirdcoords

    # горизонтального или вертикального расположения
    def randomHorizOrVert(self, num=None):
        if self.coords[1] == 6:
            print(f'Только вертикальное расположение корабля доступно для координаты {self.coords}')
            print('---------------------------')
            return self.vertical()

        if self.coords[0] == 6:
            print(f'Только горизонтальное расположение корабля доступно для координаты {self.coords}')
            print('---------------------------')
            return self.horizontal()

        if num == '3' and self.coords[1] == 5:
            print(f'Только вертикальное расположение корабля доступно для координаты {self.coords}')
            print('---------------------------')
            return self.vertical()

        if num == '3' and self.coords[0] == 5:
            print(f'Только горизонтальное расположение корабля доступно для координаты {self.coords}')
            print('---------------------------')
            return self.horizontal()

        val = self.randomChooseView()
        if val == 1:
            print('Вы выбрал горизонтальное расположение корабля')
            print('---------------------------')
            return self.horizontal()
        if val == 2:
            print('ВЫ выбрал вертикальное расположение корабля')
            print('---------------------------')
            return self.vertical()

    def randomHorizOrVertForThree(self):
        val = self.randomHorizOrVert('3')
        print('val', val)
        if val == self.horizontal():
            thirdcoords = [self.coords[0], self.coords[1] + 2]
        if val == self.vertical():
            thirdcoords = [self.coords[0] + 2, self.coords[1]]
        return val + thirdcoords

    def cageCheak(self, coords, history):
        print("---------------------------")
        n = 0
        n = history.count(coords)
        if n == 0:
            print('Клетка свободна')
            return coords
        else:
            print('Клетка занята!')
            coords1 = self.inputCoords()
            return self.cageCheak(coords1, history.playerHistory())

    def nearCageCheak(self, coords, history):
        print("---------------------------")
        n = 0
        n = history.count(coords)
        if n == 0:
            print('Рядом нет кораблей')
            return coords
        else:
            print('Рядом корабль!')
            coords1 = self.inputCoords()
            self.cageCheak(coords1, history.playerHistory())
            return self.nearCageCheak(coords1, history.playerNearHistory())

    def randomCageCheak(self, coords, history):
        print("---------------------------")
        n = 0
        n = history.count(coords)
        if n == 0:
            print('Клетка свободна')
            return coords
        else:
            print('Клетка занята!')
            coords1 = self.inputRandomCoords()
            return self.randomCageCheak(coords1, history.playerHistory())

    def randomNearCageCheak(self, coords, history):
        print("---------------------------")
        n = 0
        n = history.count(coords)
        if n == 0:
            print('Рядом нет кораблей')
            return coords
        else:
            print('Рядом корабль!')
            coords1 = self.inputRandomCoords()
            self.randomCageCheak(coords1, history.playerHistory())
            return self.randomNearCageCheak(coords1, history.playerNearHistory())


# Игрок
class Player(Game):
    # Проверка координат
    def getCooordinates(self, num=None):
        coords = self.inputCoords(num)
        print('Проверка ', coords)
        cords1 = self.cageCheak(coords, player_history.playerHistory())
        cords2 = self.nearCageCheak(cords1, player_history.playerNearHistory())
        self.coords = cords2
        return self.coords

    # Запрос координат для однопалубного
    def getCooordsForOne(self):
        self.coords = self.getCooordinates()
        print('Координаты ', self.coords)
        player_history.writePlayerHistory(self.coords)
        player_history.writePlayerNearHistory(self.coords)
        player_history.getPlayerHistory()
        return self.coords

    # Запрос координат для двупалубного
    def getCoordsForTwo(self):
        self.coords = self.getCooordinates('2') + self.horizOrVert()
        print('Координаты ', self.coords)
        player_history.writePlayerHistory(self.coords)
        player_history.writePlayerNearHistory(self.coords)
        player_history.getPlayerHistory()
        return self.coords

    # Запрос координат для трехпалубного
    def getCoordsForThree(self):
        self.coords = self.getCooordinates('3') + self.horizOrVertForThree()
        print('координаты', self.coords)
        player_history.writePlayerHistory(self.coords)
        player_history.writePlayerNearHistory(self.coords)
        player_history.getPlayerHistory()
        return self.coords


# ИИ
class AI(Game):
    # Проверка координат
    def randomCooordinates(self, num=None):
        coords = self.inputRandomCoords(num)
        print('Проверка ', coords)
        cords1 = self.randomCageCheak(coords, ai_history.playerHistory())
        cords2 = self.randomNearCageCheak(cords1, ai_history.playerNearHistory())
        self.coords = cords2
        return self.coords

    # Запрос координат для однопалубного
    def randomCooordsForOne(self):
        self.coords = self.randomCooordinates()
        print('Координаты ', self.coords)
        ai_history.writePlayerHistory(self.coords)
        ai_history.writePlayerNearHistory(self.coords)
        ai_history.getAIHistory()
        return self.coords

    # Запрос координат для двупалубного
    def randomCoordsForTwo(self):
        self.coords = self.randomCooordinates('2') + self.randomHorizOrVert()
        print('Координаты ', self.coords)
        ai_history.writePlayerHistory(self.coords)
        ai_history.writePlayerNearHistory(self.coords)
        ai_history.getAIHistory()
        return self.coords

    # Запрос координат для трехпалубного
    def randomCoordsForThree(self):
        self.coords = self.randomCooordinates('3') + self.randomHorizOrVertForThree()
        print('координаты', self.coords)
        ai_history.writePlayerHistory(self.coords)
        ai_history.writePlayerNearHistory(self.coords)
        ai_history.getAIHistory()
        return self.coords


# Хранение данных
class History(Game):
    # Запоминаем использованые клетки
    def playerHistory(self):
        return self.player_history

    def playerNearHistory(self):
        return self.player_near_history

    # Клетки занятые кораблями
    def writePlayerHistory(self, ship):
        self.playerHistory().append(ship)

    # Клетки рядом с кораблями
    def writePlayerNearHistory(self, ship):
        if len(ship) == 2:
            self.playerNearHistory().append([ship[0] - 1, ship[1] - 1])
            self.playerNearHistory().append([ship[0] - 1, ship[1]])
            self.playerNearHistory().append([ship[0] - 1, ship[1] + 1])
            self.playerNearHistory().append([ship[0], ship[1] - 1])
            self.playerNearHistory().append([ship[0], ship[1] + 1])
            self.playerNearHistory().append([ship[0] + 1, ship[1] - 1])
            self.playerNearHistory().append([ship[0] + 1, ship[1]])
            self.playerNearHistory().append([ship[0] + 1, ship[1] + 1])
        if len(ship) == 4:
            self.playerNearHistory().append([ship[0] - 1, ship[1] - 1])
            self.playerNearHistory().append([ship[0] - 1, ship[1]])
            self.playerNearHistory().append([ship[0] - 1, ship[1] + 1])
            self.playerNearHistory().append([ship[0], ship[1] - 1])
            self.playerNearHistory().append([ship[0], ship[1] + 1])
            self.playerNearHistory().append([ship[0] + 1, ship[1] - 1])
            self.playerNearHistory().append([ship[0] + 1, ship[1]])
            self.playerNearHistory().append([ship[0] + 1, ship[1] + 1])

            self.playerNearHistory().append([ship[2] - 1, ship[3] - 1])
            self.playerNearHistory().append([ship[2] - 1, ship[3]])
            self.playerNearHistory().append([ship[2] - 1, ship[3] + 1])
            self.playerNearHistory().append([ship[2], ship[3] - 1])
            self.playerNearHistory().append([ship[2], ship[3] + 1])
            self.playerNearHistory().append([ship[2] + 1, ship[3] - 1])
            self.playerNearHistory().append([ship[2] + 1, ship[3]])
            self.playerNearHistory().append([ship[2] + 1, ship[3] + 1])

        if len(ship) == 6:
            self.playerNearHistory().append([ship[0] - 1, ship[1] - 1])
            self.playerNearHistory().append([ship[0] - 1, ship[1]])
            self.playerNearHistory().append([ship[0] - 1, ship[1] + 1])
            self.playerNearHistory().append([ship[0], ship[1] - 1])
            self.playerNearHistory().append([ship[0], ship[1] + 1])
            self.playerNearHistory().append([ship[0] + 1, ship[1] - 1])
            self.playerNearHistory().append([ship[0] + 1, ship[1]])
            self.playerNearHistory().append([ship[0] + 1, ship[1] + 1])

            self.playerNearHistory().append([ship[2] - 1, ship[3] - 1])
            self.playerNearHistory().append([ship[2] - 1, ship[3]])
            self.playerNearHistory().append([ship[2] - 1, ship[3] + 1])
            self.playerNearHistory().append([ship[2], ship[3] - 1])
            self.playerNearHistory().append([ship[2], ship[3] + 1])
            self.playerNearHistory().append([ship[2] + 1, ship[3] - 1])
            self.playerNearHistory().append([ship[2] + 1, ship[3]])
            self.playerNearHistory().append([ship[2] + 1, ship[3] + 1])

            self.playerNearHistory().append([ship[4] - 1, ship[5] - 1])
            self.playerNearHistory().append([ship[4] - 1, ship[5]])
            self.playerNearHistory().append([ship[4] - 1, ship[5] + 1])
            self.playerNearHistory().append([ship[4], ship[5] - 1])
            self.playerNearHistory().append([ship[4], ship[5] + 1])
            self.playerNearHistory().append([ship[4] + 1, ship[5] - 1])
            self.playerNearHistory().append([ship[4] + 1, ship[5]])
            self.playerNearHistory().append([ship[4] + 1, ship[5] + 1])

    #Вывод инфы из истории
    def getPlayerHistory(self):
        print('Здесь хранятся корабли AI')
        print(self.playerHistory())
        print(f'Здесь хранятся клетки рядом с кораблями  AI:')
        print(self.playerNearHistory())

    def getAIHistory(self):
        print('Здесь хранятся корабли AI:')
        print(self.playerHistory())
        print('Здесь хранятся клетки рядом с кораблями  AI:')
        print(self.playerNearHistory())


# Корабли
class Ship():
    def __init__(self, coords=None):
        self.coords = coords

    def getCoords(self):
        return self.coords


# Поле
class Field():
    def __init__(self):
        field = [['◌' for j in range(6)] for i in range(6)]
        self.field = field
        self.ship = "■"
        self.empty = "⋄"

    def getField(self):
        return self.field

    def getShip(self):
        return self.ship

    def getEmpty(self):
        return self.ship

    # Красивый вывод тестового поля
    def test(self):
        print("---------------------------")
        print('    1    2   3   4    5   6 ')
        for i, row in enumerate(self.getField()):
            row_str = f"{i + 1} | {' | '.join(row)} |"
            print(row_str)
        print('---------------------------')

    # Растановка кораблей на тестовом поле
    def cheakInput(self, coords):
        def repeat_list(coords):
            coords_values = coords.copy()
            while True:
                value = coords_values.pop(0)
                coords_values.append(value)
                print('вызываемое значние', value)
                yield value

        print('список для поля', coords)
        val = repeat_list(coords)
        self.getField()[next(val) - 1][next(val) - 1] = self.getShip()
        self.getField()[next(val) - 1][next(val) - 1] = self.getShip()
        self.getField()[next(val) - 1][next(val) - 1] = self.getShip()


player_history = History()
ai_history = History()
