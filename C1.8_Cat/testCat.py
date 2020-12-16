from cat import Cat

cat1 = Cat('Baron', 'M', '2')
cat2 = Cat('Sam', 'M', '2')

print(f"Имя первого кота: {cat1.getName()}")
print(f"Возраст первого кота: {cat1.getAge()}")
print(f"Пол первого кота: {cat1.getSex()}")

print(f"Имя второго кота: {cat2.getName()}")
print(f"Возраст второго кота: {cat2.getAge()}")
print(f"Пол второго кота: {cat2.getSex()}")
