list_1 = [i for i in range(1, 21)]

func_1 = lambda x: x % 2 == 0

list_2 = list(filter(func_1, list_1))

print(list_2)



list_3 = [2, 8, 4, 36, 21, 15, 32, 26, 19, 6]

func_2 = lambda x: x > 10

print(sorted(list(filter(func_2, list_3))))


def square(x):
    return x ** 2

list_4 = [1, 2, 3, 4, 5]

list_5 = list(map(square,list_4))

print(list_5)


footballer_goals =  {'Eusebio' : 120, 'Cruyff' : 104, 'Pele' : 150, 'Ronaldo' : 132, 'Messi' : 125}

sorted_list = sorted(footballer_goals.items(), key= lambda x: x[1])

print(sorted_list)

print(dict(sorted_list))

i = 0
while i < 20:
    i += 4
    print(i)
