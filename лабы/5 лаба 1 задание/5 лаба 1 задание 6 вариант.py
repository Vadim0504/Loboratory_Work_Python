from ast import comprehension


n = int(input("введите число \n"))
list = [[i for _ in range(n)] for i in range(n)]
print(*list, sep = '\n')
# Вводится натуральное число N. Необходимо сгенерировать вложеный список с помощью list comprehension,
# размером N x N, где первая строка содержала бы все нули, вторая единицы, третья все двойки 
# и так до N, результат вывести на экран.