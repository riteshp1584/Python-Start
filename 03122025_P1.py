list_1 = [i for i in range(10, 101, 2)]

print(list_1)

def func_1(number):
    if number % 10 == 0:
        return number
    else:
        return "Not ending with zero"

for i in list_1:
    print(func_1(i))

def my_sum(*integers):
    result = 0
    for i in integers:
        result += i
    return result

tuple_1 = (1, 2, 3)
print(my_sum(*tuple_1))

def join_words(**words):
    result = ''
    for word in words.values():
        result += word + ' '
    return result

dict_1 = {'a':'India', 'b':'is', 'c':'a', 'd':'beautiful', 'e':'country'}
print(join_words(**dict_1))



list_5 = [1, 2, 3]
list_6 = [4, 5, 6]
merged_list = [*list_5, *list_6]
print(merged_list)

dict_5 = {'A': 1, "B": 2}
dict_6 = {'C': 3, "D": 4}
merged_dict = {**dict_5, **dict_6}
print(merged_dict)



list_10 = [i for i in range(10, 101, 10)]
print(list_10)

func_2 = lambda x: x + 5

list_11 = []
for i in list_10:
    list_11.append(func_2(i))

print(list_11)



list_12 = [i for i in range(1, 21)]

func_5 = lambda x: x * 10 if x > 10 else (x * 5 if x < 5 else x)

list_14 = []
for i in list_12:
    list_14.append(func_5(i))

print(list_14)

print(func_5(11))
