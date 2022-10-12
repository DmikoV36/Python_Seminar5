# Дан список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.

import re
try:
    n = str(input("Введите последовательность чисел: "))
    numbers = []
    def split_str (n):
        str_numbers = re.split(",| |;", n)
        if str_numbers.count("") != 0:
            for i in range(str_numbers.count("")):
                str_numbers.remove("")
        for i in range(len(str_numbers)):
            numbers.append(int(str_numbers[i]))
        return numbers

    def sequence (list):        
        min_eq = min(list)        
        max_eq = max(list)
        gap = []
        for i in range(min(list), max(list) + 1):
            if i in list and (i - 1) not in list:
                min_eq = i                
            elif i - min_eq > 1 and i not in list and i - 1 in list:
                gap.append(min_eq)
                gap.append(i - 1)
                min_eq = i + 1                
            elif i - min_eq > 0 and i == max_eq and (i - 1) in list:
                gap.append(min_eq)
                gap.append(i)
        if len(gap) == 0:
            print("Возрастающей последовательности нет.")
        elif len(gap) == 2:
            print(f"Список описывающий максимальную возрастающую последовательность!: [{gap[0]}, {gap[1]}]")
        else:
            min_eq = gap[0]
            max_eq = gap[1]
            for i in range(0, len(gap) - 3, 2):
                if gap[i + 3] - gap [i + 2] > gap[i + 1] - gap[i]:
                    min_eq = gap[i + 2]
                    max_eq = gap[i + 3]
            print(f"Список описывающий максимальную возрастающую последовательность: [{min_eq}, {max_eq}]")

    sequence(split_str (n))

except:
    print("Нужно вводить последовательность целых чисел!")
    exit()