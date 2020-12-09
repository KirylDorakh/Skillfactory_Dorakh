field = [['-' for j in range(3)] for i in range(3)]


# Вывод стартового поля
def start_field():
    for n in field:
        print(*n)
    print('---------------------------')


# Смена игрока
def change_player():
    n = 0
    while True:
        if n:
            n += 1
            player = 'o'
        else:
            n -= 1
            player = 'x'
        yield player


# Ход
def my_input(player):
    print(f"Ход игрока {player}")
    print('---------------------------')
    x = 0
    y = 0
    while True:
        while not (1 <= x <= 3):
            try:
                x = int(input('Выберете строку от 1 до 3:'))
                if not (1 <= x <= 3):
                    raise ValueError
            except ValueError:
                print("Введено неверное значение")
            else:
                print(f"Вы ввели значение {x}")
        while not (1 <= y <= 3):
            try:
                y = int(input('Выберете столбец от 1 до 3:'))
                if not (1 <= x <= 3):
                    raise ValueError
            except ValueError:
                print("Введено неверное значение")
            else:
                print(f"Вы ввели значение {y}")
        yield x, y


# Провекра корректности хода
def check(next_move, player):
    move = field[next_move[0] - 1][next_move[1] - 1]
    if move == '-':
        print('---------------------------')
        print(f'Клетка {next_move} свободна')
        print('Ход разрешен')
        print('---------------------------')
        move = player
        return next_move, move
    elif move != '-':
        print('---------------------------')
        print(f'Клетка {next_move} занята!!!')
        print('Ход запрещен!!!')
        print('Попробуйте еще раз!!!')
        print('---------------------------')
        next_move = next(my_input(player))
        fix = check(next_move, player)
        return fix


# Вывод поля после хода
def output_field(next_move, move):
    field[next_move[0] - 1][next_move[1] - 1] = move
    start_field()


# Проверка результат
def check_result(player):
    i = 0
    j = 0
    n = 0
    if field[i][i] == field[i + 1][i + 1] == field[i + 2][i + 2] == player:
        print('---------------------------')
        print(f'3 "{player}" по диагонали')
        return player

    if field[i + 2][i] == field[i + 1][i + 1] == field[i][i + 2] == player:
        print('---------------------------')
        print(f'3 "{player}" по диагонали')
        return player

    for i in range(3):
        if '-' not in field[i]:
            n += 1
        if field[i][j] == field[i][j + 1] == field[i][j + 2] == player:
            print('---------------------------')
            print(f'3 "{player}" по строке {i + 1}')
            return player
        if field[j][i] == field[j + 1][i] == field[j + 2][i] == player:
            print('---------------------------')
            print(f'3 "{player}" по столбцу {i + 1}')
            return player

    if n == 3:
        print('---------------------------')
        print('Ничья')
        return 'Никто не'

# wrapper
def game(func):
    def wrapper():
        print("Поле")
        start_field()
        print(f'{func()} выйграл!!!')
        print("Игра окончена")
        # для 3t.exe
        input('Нажмите любую клавишу для выхода')

    return wrapper


# Основной цикл
@game
def main_play():
    val = change_player()  # получаем значение для игрока
    result = None
    while not result:
        player = next(val)  # переменная для игрока
        next_move = next(my_input(player))  # вызов хода
        check_next_move = check(next_move, player)
        output_field(*check_next_move)
        result = check_result(player)
    return result


# Игра
main_play()
