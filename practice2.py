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

#以下に続く

score = [40,60,80]
print(sum(score)/len(score))
max_score = max(score)
print(max_score)
table = [['24/3','24/4','24/5'],[300,-400,0]]
print(table[0][1])
print(table[1][2])
print(table[0][0])
print(table[1][2])
color = ('red','green','blue')
print(color[0])
#color.append('black') タプルには要素の追加はできない
print(color)
menu = ('rice',200)
print(menu[1])
menu = {'apple':100,'banana':80,'orange':120}
print(menu['apple'])
menu['grape'] = 150
print(menu)
menu['banana'] = 60
print(menu)
menu['ido',460] = 300  #キーにはタプルも入れることができる
print(menu)
menu = {'apple':100,'banana':80,'orange':120}
del menu['apple'],menu['banana']
print(menu)