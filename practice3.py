print(1 == 1)
print(1 < 0)
is_rain = False
if is_rain:
    print('傘を持つ')
else:
    print('新しい靴を履く')
print(1 == 1)
print(1 < 0)
age = 40
if age < 20:
    print('NO Drink')
else:
    print('Enjoy')
print(True and False)
print(True or False)
print(not True)
print(not False)
BMI = 20
if BMI >= 18 and BMI < 25:
    print('nomal weight')
BMI = 18.00

if BMI >= 25:
    print('overweight')
elif BMI >= 18 and BMI < 25:
    print('nomal weight')
else:
    print('underweight')
for i in range(0,5):
    print('Python文法',i)

menu = ['salad','soup','steak','cake']
for food in menu:
    print(food)

menu = ['salad','soup','steak','cake']
for i,food in enumerate(menu):
    print(i,food)