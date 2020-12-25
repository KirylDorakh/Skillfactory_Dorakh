import random

# Игра
class Game:
    def __init__(self, player=None, n=0, coords=None):
        self.player = player
        self.n = n
        self.coords = coords
        self.player_history = []
        self.player_near_history = []
        self.shoot_history = []
        self.ai_history = []
        field = [['◌' for j in range(6)] for i in range(6)]
        self.field = field
        self.ship = "■"

    @staticmethod
    def hello():
        print("""-----------------------------------------
                Морской бой
-----------------------------------------
Правила игры:
Первым заполяет поле ИИ (не торопите его).
После ИИ заполните свое поле кораблями.
У вас есть 1 - трехпалубный, 2 - двухпалубных
и 4 - однопалубных корабля.
Введите по очереди координаты по строке
и столбуцу для заполнения поля. 
Игрок и ИИ по очереди делает выстрелы.
ИИ начинает первым.
Введите по очереди координаты по строке
и столбуцу для выстрела.
Кто первым уничтожил корабли противника
              тот выйграл!
-----------------------------------------""")

    @staticmethod
    def pause():
        x = 0
        input('Нажмите Enter...')
        print("-----------------------------------------")


    # Смена хода
    def changeOfCourse(self):
        while True:
            if self.n:
                self.n += 1
                player = self.playerShot()
            else:
                self.n -= 1
                player = self.aiShot()
            yield player

    def getShootHistory(self):
        return self.shoot_history

    def writeShootHistory(self, shoot):
        self.getShootHistory().append(shoot)

    # Выстрел игрока
    def playerShot(self):
        x = 0
        y = 0
        print("-----------------------------------------")
        print("            Выстрел Игрока")
        print("-----------------------------------------")

        while True:
            while not (1 <= x <= 6):
                try:
                    x = int(input('Выберете строку от 1 до 6 для выстрела:'))
                    if not (1 <= x <= 6):
                        raise ValueError
                except ValueError:
                    print("Введено неверное значение")
                else:
                    print(f"Вы ввели значение {x}")
            while not (1 <= y <= 6):
                try:
                    y = int(input('Выберете столбец от 1 до 6 для выстрела:'))
                    if not (1 <= y <= 6):
                        raise ValueError
                except ValueError:
                    print("Введено неверное значение")
                else:
                    print(f"Вы ввели значение {y}")
            shoot = x, y
            print("-----------------------------------------")
            print(f"Выстрел игрока {shoot}")
            return shoot
    # Выстрел ИИ
    def aiShot(self):
        print("-----------------------------------------")
        print("              Выстрел ИИ")
        print("-----------------------------------------")
        x = 0
        y = 0
        while True:
            while not (1 <= x <= 6):
                try:
                    x = random.randint(0, 6)
                    if not (1 <= x <= 6):
                        raise ValueError
                except ValueError:
                    print(" ")
                else:
                    print('ИИ выбирает куда стрелять...')
            while not (1 <= y <= 6):
                try:
                    y = random.randint(0, 6)
                    if not (1 <= y <= 6):
                        raise ValueError
                except ValueError:
                    print("Все еще думает...")
                else:
                    print('ИИ выбирает куда стрелять...')
            shoot = x, y
            print("-----------------------------------------")
            print(f"Выстрел ИИ {shoot}")
            return shoot



    # Запоминаем использованые клетки
    def playerHistory(self):
        return self.player_history

    def playerNearHistory(self):
        return self.player_near_history

    def getSetNearHistory(self):
        _list = []
        for i in self.playerNearHistory():
            _list.append(tuple(i))
        print(_list)
        val = list(set(_list))
        print(val)
        return val

    def getSetHistory(self):
        _list = []
        for i in self.playerHistory():
            _list.append(tuple(i))
        val1 = list(set(_list))
        return val1

    def getSetAllHistory(self):
        a = self.getSetHistory() + self.getSetNearHistory()
        return a

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

    # Вывод инфы из истории
    def getPlayerHistory(self):
        print('Здесь хранятся корабли Игрока')
        print(self.playerHistory())
        print(f'Здесь хранятся клетки рядом с кораблями  Игрока:')
        print(self.playerNearHistory())

    def getAIHistory(self):
        print('Здесь хранятся корабли AI:')
        print(self.playerHistory())
        print('Здесь хранятся клетки рядом с кораблями  AI:')
        print(self.playerNearHistory())


    # Ввод рандомных координат для ИИ
    def inputRandomCoords(self, num=None):
        x = 0
        y = 0
        while True:
            while not (1 <= x <= 6):
                try:
                    x = random.randint(0, 6)
                    if not (1 <= x <= 6):
                        raise ValueError
                except ValueError:
                    error = 1
                else:
                    error = 0
            while not (1 <= y <= 6):
                try:
                    y = random.randint(0, 6)
                    if not (1 <= y <= 6):
                        raise ValueError
                except ValueError:
                    error = 1
                else:
                    y = y
            val = x, y
            if not num:
                coords = list(val)
                return coords
            if num == '2':
                if val == (6, 6):
                    return self.inputRandomCoords('2')
                n = 0
                val = list(val)
                val1 = [val[0], val[1] + 1]
                val2 = [val[0] + 1, val[1]]
                n1 = self.playerNearHistory().count(val1)
                n2 = self.playerNearHistory().count(val2)
                if n1 != 0 and n2 != 0:
                    return self.inputRandomCoords('2')
                if n1 != 0:
                    if val2[0] > 6:
                        return self.inputRandomCoords('2')
                    coords = list(val)
                    return coords
                if n2 != 0:
                    if val1[1] > 6:
                        return self.inputRandomCoords('2')
                    coords = list(val)
                    return coords
            if num == '3' and (val == (6, 6) or val == (5, 6) or val == (5, 5) or val == (6, 5)):
                return self.inputRandomCoords('3')
            else:
                coords = list(val)
                return coords

    # Ввод координат Игрока
    def inputCoords(self, num=None):
        x = 0
        y = 0
        print("-----------------------------------------")
        print(f'Корабль на {num}')
        print("-----------------------------------------")
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
            if num == '1':
                coords = list(val)
                return coords
            if num == '2':
                if val == (6, 6):
                    print("-----------------------------------------")
                    print('Недопустимые координаты для двухпалубного корабля')
                    print("-----------------------------------------")
                    return self.inputCoords('2')
                n = 0
                val = list(val)
                val1 = [val[0], val[1] + 1]
                val2 = [val[0] + 1, val[1]]
                n1 = self.playerNearHistory().count(val1)
                n2 = self.playerNearHistory().count(val2)
                if n1 != 0 and n2 != 0:
                    print("-----------------------------------------")
                    print('Недопустимые координаты для двухпалубного корабля')
                    print('Недопустимые клетки справа и снизу')
                    print("-----------------------------------------")
                    return self.inputCoords('2')
                if n1 != 0:
                    print("-----------------------------------------")
                    print('Cправа недопустимая клетка')
                    print('Выбор горизонтального расположения корабля запрещен')
                    print("-----------------------------------------")
                    if val2[0] > 6:
                        print('Недопустимые координаты для двухпалубного корабля')
                        print('Снизу граница поля')
                        print("-----------------------------------------")
                        return self.inputCoords('2')
                    coords = list(val)
                    return coords
                if n2 != 0:
                    print("-----------------------------------------")
                    print('Снизу недопустимая клетка')
                    print('Выбор вертикального расположения корабля запрещен')
                    print("-----------------------------------------")
                    if val1[1] > 6:
                        print('Недопустимые координаты для двухпалубного корабля')
                        print('Справа граница поля')
                        print("-----------------------------------------")
                        return self.inputCoords('2')
                    coords = list(val)
                    return coords
            if num == '3' and (val == (6, 6) or val == (5, 6) or val == (5, 5) or val == (6, 5)):
                print("-----------------------------------------")
                print('Недопустимые координаты для трехпалубного корабля')
                print("-----------------------------------------")
                return self.inputCoords('3')
            else:
                coords = list(val)
                return coords

    # Горизонтальноe или вертикальноe расположениe
    def randomChooseView(self):
        val = 0
        while True:
            while not (1 <= val <= 2):
                try:
                    val = random.randint(1, 2)
                    if not (1 <= val <= 2):
                        raise ValueError
                except ValueError:
                    error = 1
                else:
                    val = val
            return val

    def chooseView(self):
        print("-----------------------------------------")
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

    # горизонтальное расположение
    def horizontal(self):
        self.secondcoords = [self.coords[0], self.coords[1] + 1]
        return self.secondcoords

    # вертикальное расположение
    def vertical(self):
        self.secondcoords = [self.coords[0] + 1, self.coords[1]]
        return self.secondcoords

    # Выбор горизонтальноeго или вертикального расположения для игрока
    def horizOrVert(self, num=None):
        val = self.coords
        val1 = [val[0], val[1] + 1]
        val2 = [val[0] + 1, val[1]]
        n1 = self.playerNearHistory().count(val1)
        n2 = self.playerNearHistory().count(val2)
        if self.coords[1] == 6:
            print('Только вертикальное расположение корабля')
            print(f'доступно для координаты {self.coords}')
            print("-----------------------------------------")
            return self.vertical()

        if self.coords[0] == 6:
            print(f'Только горизонтальное расположение корабля')
            print(f'доступно для координаты {self.coords}')
            print("-----------------------------------------")
            return self.horizontal()

        if num == '2' and n1 != 0:
            print('Cправа клетка рядом с другим кораблем')
            print('выбор горизонтального расположения запрещен')
            print("-----------------------------------------")
            return self.vertical()

        if num == '2' and n2 != 0:
            print('Снизу клетка рядом с другим кораблем')
            print('выбор вертикального расположения корабля запрещен')
            print("-----------------------------------------")
            return self.horizontal()

        if num == '3' and self.coords[1] == 5:
            print('Только вертикальное расположение корабля')
            print(f'доступно для координаты {self.coords}')
            print("-----------------------------------------")
            return self.vertical()

        if num == '3' and self.coords[0] == 5:
            print('Только горизонтальное расположение корабля')
            print(f'доступно для координаты {self.coords}')
            print("-----------------------------------------")
            return self.horizontal()

        val1 = self.chooseView()
        print('val1', val1)
        if val1 == 1:
            print('Вы выбрали горизонтальное расположение корабля')
            print("-----------------------------------------")
            return self.horizontal()
        if val1 == 2:
            print('ВЫ выбрали вертикальное расположение корабля')
            print("-----------------------------------------")
            return self.vertical()

    def horizOrVertForThree(self):
        val = self.horizOrVert('3')
        if val == self.horizontal():
            self.thirdcoords = [self.coords[0], self.coords[1] + 2]
            return val + self.thirdcoords
        if val == self.vertical():
            self.thirdcoords = [self.coords[0] + 2, self.coords[1]]
            return val + self.thirdcoords

    # Рандом для горизонтального или вертикального расположения
    def randomHorizOrVert(self, num=None):
        val = self.coords
        val1 = [val[0], val[1] + 1]
        val2 = [val[0] + 1, val[1]]
        n1 = self.playerNearHistory().count(val1)
        n2 = self.playerNearHistory().count(val2)
        if self.coords[1] == 6:
            return self.vertical()

        if self.coords[0] == 6:
            return self.horizontal()

        if num == '2' and n1 != 0:
            return self.vertical()

        if num == '2' and n2 != 0:
            return self.horizontal()

        if num == '3' and self.coords[1] == 5:
            return self.vertical()

        if num == '3' and self.coords[0] == 5:
            return self.horizontal()

        val1 = self.randomChooseView()
        if val1 == 1:
            return self.horizontal()
        if val1 == 2:
            return self.vertical()

    def randomHorizOrVertForThree(self):
        val = self.randomHorizOrVert('3')
        if val == self.horizontal():
            thirdcoords = [self.coords[0], self.coords[1] + 2]
            return val + thirdcoords
        if val == self.vertical():
            thirdcoords = [self.coords[0] + 2, self.coords[1]]
            return val + thirdcoords

    # Проверка клеток
    def cageCheak(self, coords, num=None):
        print("-----------------------------------------")
        n = 0
        n = self.playerHistory().count(coords)
        if n == 0:
            #print('Клетка свободна')
            return coords
        else:
            print('Клетка занята!')
            coords1 = self.inputCoords()
            return self.cageCheak(coords1, num)

    def randomCageCheak(self, coords, num=None):
        n = 0
        n = self.playerHistory().count(coords)
        if n == 0:
            return coords
        else:
            coords1 = self.inputRandomCoords(num)
            return self.randomCageCheak(coords1, num)

    def nearCageCheak(self, coords, num):
        print("-----------------------------------------")
        n = 0
        n = self.playerNearHistory().count(coords)
        if n == 0:
            print('Рядом нет кораблей')
            return coords
        else:
            print('Рядом корабль!')
            coords_ = self.inputCoords(num)
            coords9 = self.cageCheak(coords_, num)
            return self.nearCageCheak(coords9, num)

    def randomNearCageCheak(self, coords, num):
        n = 0
        n = self.playerNearHistory().count(coords)
        if n == 0:
            return coords
        else:
            coords_ = self.inputRandomCoords(num)
            coords9 = self.randomCageCheak(coords_, num)
            return self.randomNearCageCheak(coords9, num)


# Поле
class Field():
    def __init__(self):
        field = [['◌' for j in range(6)] for i in range(6)]
        self.field = field
        self.ship = "■"
        self.shoot = "X"
        self.miss = "T"

    @property
    def getField(self):
        return self.field

    @property
    def getShip(self):
        return self.ship

    @property
    def getShoot(self):
        return self.shoot

    @property
    def getMiss(self):
        return self.miss

    # Красивый вывод тестового поля
    def test(self):
        print("-----------------------------------------")
        print('    1   2   3   4   5   6 ')
        for i, row in enumerate(self.getField):
            row_str = f"{i + 1} | {' | '.join(row)} |"
            print(row_str)
        print("-----------------------------------------")

    # Растановка кораблей на тестовом поле
    def cheakInput(self, coords):
        coords = list(coords)

        def repeat_list(coords):
            coords_values = coords.copy()
            while True:
                value = coords_values.pop(0)
                coords_values.append(value)
                yield value

        val = repeat_list(coords)
        self.getField[next(val) - 1][next(val) - 1] = self.getShip
        self.getField[next(val) - 1][next(val) - 1] = self.getShip
        self.getField[next(val) - 1][next(val) - 1] = self.getShip

    #Отображение стрельбы
    def cheakShoot(self, coords):
        val = self.getField[coords[0] - 1][coords[1] - 1]
        if val == '■':
            print('Попадание!!!')
            self.getField[coords[0] - 1][coords[1] - 1] = self.getShoot
            return "Попадание!!!"
        else:
            print("Мимо =(((")
            self.getField[coords[0] - 1][coords[1] - 1] = self.getMiss
            return "Мимо =((("

    def cheakShootForAIField(self, coords):
        val = self.getField[coords[0] - 1][coords[1] - 1]
        if val == '■':
            print('Попадание!!!')
            self.getField[coords[0] - 1][coords[1] - 1] = self.getShoot
            return coords, "Попадание!!!"
        else:
            print("Мимо =(((")
            self.getField[coords[0] - 1][coords[1] - 1] = self.getMiss
            return coords, "Мимо =((("

    def cheakFromSecretAIField(self, coords, cheak):
        if cheak == 'Попадание!!!':
            self.getField[coords[0] - 1][coords[1] - 1] = self.getShoot
            return "Попадание!!!"
        if cheak == "Мимо =(((":
            self.getField[coords[0] - 1][coords[1] - 1] = self.getMiss

    def cheak_result_ai(self):
        val = 0
        n = self.getField.count(self.getShip)
        for i in self.getField:
            n = i.count('■')
            val += n
        if n == 0:
            return 'ИИ'

    def cheak_result_player(self):
        val = 0
        for i in self.getField:
            n = i.count('■')
            val += n
        if val == 0:
            return 'Игрок'


# ИИ
class AiShip(Game):
    # Проверка координат
    def randomCooordinates(self, num=None):
        coords = self.inputRandomCoords(num)
        cords1 = self.randomCageCheak(coords, num)
        cords2 = self.randomNearCageCheak(cords1, num)
        self.coords = cords2
        return self.coords

    # Запрос координат для однопалубного
    def randomCooordsForOne(self):
        self.coords = self.randomCooordinates()
        self.writePlayerHistory(self.coords)
        self.writePlayerNearHistory(self.coords)
        # self.getAIHistory()
        return self.coords

    # Запрос координат для двупалубного
    def randomCoordsForTwo(self):
        self.coords = self.randomCooordinates(num='2') + self.randomHorizOrVert(num='2')
        self.writePlayerHistory(self.coords)
        self.writePlayerNearHistory(self.coords)
        # self.getAIHistory()
        return self.coords

    # Запрос координат для трехпалубного
    def randomCoordsForThree(self):
        self.coords = self.randomCooordinates('3') + self.randomHorizOrVertForThree()
        self.writePlayerHistory(self.coords)
        self.writePlayerNearHistory(self.coords)
        # self.getAIHistory()
        return self.coords

    def randomShipforField(self):
        print("ИИ все еще пытается расставить корабли...")
        print("-----------------------------------------")
        try:
            # Ввод первого трехпалубного
            self.randomCoordsForThree()

            # Ввод первого двухпалубного
            self.randomCoordsForTwo()

            # Ввод второго двухпалубного
            self.randomCoordsForTwo()

            # Ввод первого однопалубного
            self.randomCooordsForOne()

            # Ввод второго однопалубного
            self.randomCooordsForOne()

            # Ввод третьего однопалубного
            self.randomCooordsForOne()

            # Ввод четвертого однопалубного
            self.randomCooordsForOne()

        except RecursionError:
            print("ИИ не справился с задачей =(")
            print("-----------------------------------------")
            self.player_history = []
            self.player_near_history = []
            return self.chanceForAi()
        else:
            print('ИИ справился с задачей =)')
            print("-----------------------------------------")
            return self.playerHistory()

    def ships(self):
        return self.randomShipforField()

    def chanceForAi(self):
        print('ИИ пробует еще раз')
        print("---------------------------")
        return self.randomShipforField()

# Игрок
class PlayerShip(Game):
    # Проверка координат
    def getCooordinates(self, num=None):
        coords = self.inputCoords(num)
        print("-----------------------------------------")
        print('Проверка ', coords)
        cords1 = self.cageCheak(coords, num)
        cords2 = self.nearCageCheak(cords1, num)
        self.coords = cords2
        return self.coords

    # Запрос координат для однопалубного
    def getCooordsForOne(self):
        self.coords = self.getCooordinates('1')
        print('Координаты ', self.coords)
        self.writePlayerHistory(self.coords)
        self.writePlayerNearHistory(self.coords)
        print("-----------------------------------------")
        return self.coords

    # Запрос координат для двупалубного
    def getCoordsForTwo(self):
        self.coords = self.getCooordinates(num='2') + self.horizOrVert(num='2')
        print('Координаты ', self.coords)
        self.writePlayerHistory(self.coords)
        self.writePlayerNearHistory(self.coords)
        print("-----------------------------------------")
        return self.coords

    # Запрос координат для трехпалубного
    def getCoordsForThree(self):
        self.coords = self.getCooordinates('3') + self.horizOrVertForThree()
        print('координаты', self.coords)
        self.writePlayerHistory(self.coords)
        self.writePlayerNearHistory(self.coords)
        print("-----------------------------------------")
        return self.coords

    def getShipforField(self):
        test_field = Field()
        global player_count
        try:
            # Ввод первого трехпалубного
            coords7 = self.getCoordsForThree()
            test_field.cheakInput(coords7)
            print("              Поле игрока")
            test_field.test()

            # Ввод первого двухпалубного
            coords6 = self.getCoordsForTwo()
            test_field.cheakInput(coords6)
            print("               Поле игрока")
            test_field.test()

            # Ввод второго двухпалубного
            coords5 = self.getCoordsForTwo()
            test_field.cheakInput(coords5)
            print("               Поле игрока")
            test_field.test()

            # Ввод первого однопалубного
            coords4 = self.getCooordsForOne()
            test_field.cheakInput(coords4)
            print("               Поле игрока")
            test_field.test()

            # Ввод второго однопалубного
            coords3 = self.getCooordsForOne()
            test_field.cheakInput(coords3)
            print("               Поле игрока")
            test_field.test()

            # Ввод третьего однопалубного
            coords2 = self.getCooordsForOne()
            test_field.cheakInput(coords2)
            print("               Поле игрока")
            test_field.test()

            # Ввод четвертого однопалубного
            coords1 = self.getCooordsForOne()
            test_field.cheakInput(coords1)
            print("               Поле игрока")
            test_field.test()

        except RecursionError:
            print('Ошибка ввода')
            print('Попробуйте заполнить поле заново')
            print("-----------------------------------------")
            self.player_history = []
            self.player_near_history = []
        else:
            print('         Корабли расставлены')
            print("-----------------------------------------")
            return self.playerHistory()

    def ships(self):
        print("-----------------------------------------")
        print("          Расставьте корабли")
        print("-----------------------------------------")
        return self.getShipforField()
