from Class import Game, AiShip, Field, PlayerShip
# Приветствие
Game.hello()

game = Game()
ai_secret_field = Field()
ai_field = Field()
player_field = Field()
ai = AiShip()
player = PlayerShip()

Game.pause()
print("-----------------------------------------")
print('               Старт игры')

# Расстановка кораблей
def input_field():
    print("-----------------------------------------")
    print('ИИ расставляет корабли...')
    print("-----------------------------------------")
    ai_ships = ai.ships()

    for i in ai_ships:
        ai_secret_field.cheakInput(i)

    #print("-----------------------------------------")
    #print("               Поле ИИ")
    #ai_secret_field.test()

    player_ships = player.ships()
    print('Координаты кораблей Игрока:', player_ships)

    for i in player_ships:
        player_field.cheakInput(i)
    print("-----------------------------------------")
    print("        Ввод координат завершен")
    print("-----------------------------------------")
    print("              Поле Игрока")
    player_field.test()
    print("                Поле ИИ")
    ai_field.test()
    print("-----------------------------------------")
    print("          Начинаем стрелять")

# Проверка стрельбы с прошлыми выстрелами
def ai_coorect_shoot(shoot):
    n = ai.getShootHistory().count(shoot)
    if n == 0:
        print('Выстрел разрешен')
        return shoot
    else:
        shoot = game.aiShot()
        return ai_coorect_shoot(shoot)

# Проверка стрельбы с прошлыми выстрелами
def player_coorect_shoot(shoot):
    n = player.getShootHistory().count(shoot)
    if n == 0:
        print('Выстрел разрешен')
        return shoot
    else:
        print(f'{shoot} уже обстрелян!')
        shoot = game.playerShot()
        return player_coorect_shoot(shoot)

# Проверка попадания на пробитие
def second_chance_for_player(cheak):
    if cheak == "Попадание!!!":
        print(f'Ходите еще раз')
        shoot = game.playerShot()
        shoot4 = player_coorect_shoot(shoot)
        player.writeShootHistory(shoot4)
        print("Player's Shoots", player.getShootHistory())
        cheak = ai_secret_field.cheakShootForAIField(shoot4)
        cheak1 = ai_field.cheakFromSecretAIField(*cheak)
        return second_chance_for_player(cheak1)
    else:
        ai_field.test()
        return print("Переход хода")

def second_chance_for_ai(cheak):
    if cheak == "Попадание!!!":
        print(f'AI ходит еще раз')
        shoot = game.aiShot()
        shoot1 = ai_coorect_shoot(shoot)

        ai.writeShootHistory(shoot1)
        print("AI's Shoots", ai.getShootHistory())
        cheak1 = player_field.cheakShoot(shoot1)
        return second_chance_for_ai(cheak1)
    else:
        player_field.test()
        return print("Переход хода")

def cheak_results(ai_result, player_result):
    if ai_result:
        print("-----------------------------------------")
        return ai_result
    if player_result:
        print("-----------------------------------------")
        return player_result


# Основная игра
def main_play():
    result = None
    while not result:
        player_field.test()
        shoot = next(game.changeOfCourse())
        shoot1 = ai_coorect_shoot(shoot)

        ai.writeShootHistory(shoot1)
        print("AI's Shoots", ai.getShootHistory())
        cheak2 = player_field.cheakShoot(shoot1)

        second_chance_for_ai(cheak2)
        ai_result = player_field.cheak_result_player()

        # Ход игрока
        ai_field.test()
        shoot3 = next(game.changeOfCourse())
        shoot4 = player_coorect_shoot(shoot3)

        player.writeShootHistory(shoot4)
        print("Player's Shoots", player.getShootHistory())
        cheak = ai_secret_field.cheakShootForAIField(shoot4)
        cheak1 = ai_field.cheakFromSecretAIField(*cheak)

        second_chance_for_player(cheak1)

        #проверка результата
        player_result = ai_secret_field.cheak_result_player()
        result = cheak_results(ai_result, player_result)
    return result

input_field()

Game.pause()

print(f'Победил {main_play()} !!!!')
print('Конец игры')

Game.pause()
