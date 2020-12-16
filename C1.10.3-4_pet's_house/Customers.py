from house_for_pets import Customer

ivan_petrov = Customer('Иван Петров', 'Минск', 50)

print(ivan_petrov.info())
ivan_petrov.setReplenishment()
print(ivan_petrov.info())
ivan_petrov.setDecrease()
print(ivan_petrov.info())
print(ivan_petrov.changeBalance())

print("\n")

julia_petrova = Customer('Юлия Петрова', 'Москва', 1000)
print(julia_petrova.info())
julia_petrova.setReplenishment()
print(julia_petrova.info())
julia_petrova.setDecrease()
print(julia_petrova.info())
print(julia_petrova.changeBalance())

print(ivan_petrov.changeBalance())
