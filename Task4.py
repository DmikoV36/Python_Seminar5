# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

#З.Ы. Программа реализована для многочленов не выше 9 степени. Коэффициенты могут быть любыми.

from random import randint
a = randint(0, 9)
b = randint(0, 9)

def fill_list(n):
    random_list = [randint(-10, 10) for i in range(n+1)]
    if random_list[0] == 0:
        while random_list[0] == 0:
            random_list[0] = randint(-10, 10)
    return random_list

def write_file (list, path, k):
    data = open(path, 'w')
    for i in range(k+1):
        if list[i] != 0:
            if k - i > 1:
                if list[i + 1] > 0:
                    data.writelines(f"{list[i]}*x^{k - i}+")
                else:
                    data.writelines(f"{list[i]}*x^{k - i}")
            elif k - i == 1:
                if list[i + 1] > 0:
                    data.writelines(f"{list[i]}*x+")
                else:
                    data.writelines(f"{list[i]}*x")
            elif k == i:
                data.writelines(str(list[i]))
    data.writelines(" = 0")
    data.close()

write_file(fill_list(a), "polynomial1.txt", a)
write_file(fill_list(b), "polynomial2.txt", b)

with open("polynomial1.txt", "r") as file:
    polynom1 = file.read()
with open("polynomial2.txt", "r") as file:
    polynom2 = file.read()

p1 = {}
p2 = {}

def fill_dict (polynom, dict):
    polynom = polynom.replace(" ", "")
    while polynom.find("^") != -1:
        value_p = int(polynom[:polynom.find("*")])    
        key_p = int(polynom[polynom.find("^")+1])    
        dict[key_p] = value_p    
        polynom = polynom[polynom.find("^")+2:]
    if polynom.find("*") != -1:
        value_p = int(polynom[:polynom.find("*")])
        key_p = 1
        dict[key_p] = value_p
        polynom = polynom[polynom.find("x")+1:]
    if len(polynom) > 2:
        value_p = int(polynom[:polynom.find("=")])
        key_p = 0
        dict[key_p] = value_p
    return dict

fill_dict(polynom1, p1)
fill_dict(polynom2, p2)

list_sum = [p1.get(i, 0) + p2.get(i, 0) for i in range(9, -1, -1)]

write_file(list_sum, "polynomial_sum.txt", 9)