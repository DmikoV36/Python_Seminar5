# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

path1 = 'file.txt'
path2 = 'zip.txt'

n = str(input("Введите исходный текст: "))
with open(path1, 'w') as data:
    data.write(n)

    
def metod_RLE(file):
    with open(file, 'r') as data:
        text = data.readline()
    count = 1
    zip = ""
    temp = text[0]
    for i in range(1, len(text)):
        if temp == text[i]:
            count += 1
        else:
            zip = zip + str(count) + temp
            count = 1
            temp = text[i]
        if i == len(text) - 1:
            zip = zip + str(count) + temp
    print("Сжатый текст: " + zip)
    with open(path2, 'w') as data:
        data.write(zip)

def re_zip (file):
    with open(file, 'r') as data:
        text = data.readline()
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    value = ""
    temp = 0
    for i in range(len(text) - 1):
        if text[i] in numbers and text[i + 1] in numbers:
            temp = temp * 10 + int(text[i])
        elif text[i] in numbers and text[i + 1] not in numbers:
            value = value + (temp * 10 + int(text[i]))*text[i + 1]
            temp = 0
    print("Разархивированный текст: " + value)

metod_RLE(path1)
re_zip(path2)
        