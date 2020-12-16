class User:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def getName(self):
        return self.name

    def getCity(self):
        return self.city


class Customer(User):
    def __init__(self, name, city, purse=None, status="Customer"):
        super().__init__(name, city)
        self.purse = purse
        self.status = status
        self.DB = [f'Начальный баланс: {purse}']

    def dataBase(self):
        return self.DB

    def getStatus(self):
        return self.status

    def getBalance(self):
        return self.purse

    def info(self):
        return f'Клиент "{self.getName()}". Баланс: {self.getBalance()} рублей'

    def changeBalance(self):
        return f'{self.getStatus()} "{self.getName()}" wallet changes: {self.dataBase()}'

    def setReplenishment(self):
        x = int(input("Пополнение баланса: "))
        if x > 0 and isinstance(x, int):
            self.purse += x
            self.dataBase().append(f'+{x} рублей')
            return self.purse
        else: print('Неверный ввод')


    def setDecrease(self):
        x = int(input("Уменьшение баланса: "))
        if x > 0 and isinstance(x, int):
            self.purse -= x
            self.dataBase().append(f'-{x} рублей')
            return self.purse
        else: print('Неверный ввод')



class Volunteer(User):
    def __init__(self, name, city, level, status="Volunteer"):
        super().__init__(name, city)
        self.level = level
        self.status = status

    def getStatus(self):
        return self.status

    def getLevel(self):
        return self.level

    def info(self):
        return f'{self.getName()}, г.{self.getCity()}, статус "{self.getLevel()}"'