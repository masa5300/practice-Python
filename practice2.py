menu = ['salad','soup','steak']
menu.append('cake')
print(menu[-1])
print(menu[1])
menu = ['salad','soup','steak','cake']
print(menu[1])
menu[-1] = 'pudding'
print(menu)
menu = ['salad','soup','steak','cake']
print(menu[1:3])
menu2 = menu[:-1]
print(menu2)
menu = ['salad','soup','steak']
menu.append('cake')
print(menu[-1])
menu.remove('soup')
print(menu[1:])