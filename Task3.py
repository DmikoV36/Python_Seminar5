# Напишите программу, удаляющую из текста все слова, содержащие "абв".

import re

def del_str (n):
    start = 0
    while "абв" in n:
        for i in range(len(n)):
            if n[i] in separators:                
                if i > n.find("абв") and start == 0:
                    n = n[i:]                    
                    break
                elif i > n.find("абв") and n.find("абв") > start:
                    n = n[:start + 1] + n[i:]                    
                    break                
                else:                   
                    start = i                    
            if i == len(n) - 1 and "абв" in n:
                n = n[:start + 1]
    return n

n = str(input("Введите текст: "))
separators = [".", ",", " ", "!", ":", ";", "?"]

if n.count("абв") == 0:
    print("Слова содержащие 'абв' отсутствуют.")
    exit()
else:  
    print(del_str(n))