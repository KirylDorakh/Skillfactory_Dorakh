from sea_battle_classes import Game, Ship, Player, AI, Field, History

Game.hello()
new_game = Game()
test_field = Field()
player = Player()
ai = AI()
player_history = History()
ai_history = History()

# Ввод координат для трехпалубного
coords7 = player.getCoordsForThree()
three1 = Ship(coords7)
test_field.cheakInput(coords7)
print("Поле для расстановки")
test_field.test()
print("---------------------------")

# Ввод первого двухпалубного
coords5 = player.getCoordsForTwo()
two1 = Ship(coords5)
test_field.cheakInput(coords5)
print("Поле для расстановки")
test_field.test()
print("---------------------------")

# Ввод второго двухпалубного
coords6 = player.getCoordsForTwo()
two2 = Ship(coords6)
test_field.cheakInput(coords6)
print("Поле для расстановки")
test_field.test()
print("---------------------------")

# Ввод первого однопалубного
coords1 = player.getCooordsForOne()
one1 = Ship(coords1)
test_field.cheakInput(coords1)
print("Поле для расстановки")
test_field.test()
print("---------------------------")

# Ввод второго однопалубного
coords2 = player.getCooordsForOne()
one2 = Ship(coords2)
test_field.cheakInput(coords2)
print("Поле для расстановки")
test_field.test()
print("---------------------------")
# Ввод третьего однопалубного
coords3 = player.getCooordsForOne()
one3 = Ship(coords3)
test_field.cheakInput(coords3)
print("Поле для расстановки")
test_field.test()
print("---------------------------")

# Ввод четвертого однопалубного
coords4 = player.getCooordsForOne()
one4 = Ship(coords4)
test_field.cheakInput(coords4)
print("Поле для расстановки")
test_field.test()
print("---------------------------")


