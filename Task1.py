# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# З.Ы. Бот может ошибиться с вероятностью 20% :)

from random import randint
print("Игра с конфетами!")
print("На столе лежит 2021 конфета. За один ход можно забрать не более чем 28 конфет.")
try:
    variant = int(input("Выберите вариан игры: 1 - игра с другим человеком; 2 - игра против робота: "))
except:
    print("Нужно выбрать один из предложенных вариантов!")
    exit()
candies = 2021

def lot_motion(name1, name2, variant):
    print("Очередность хода определяется случайным образом.")
    if randint(1, 2) == 1:
        print(f"{name1} ходит первый.")
        while candies > 0:
            player_motion(name1, name2)
            if variant == 2:
                bot_motion()
            else:
                player_motion(name2, name1)
    else:
        print(f"{name2} ходит первый.")
        while candies > 0:
            if variant == 2:
                bot_motion()
            else:
                player_motion(name2, name1)
            player_motion(name1, name2)

def player_motion(name1, name2):
    global candies
    try:
        player = int(input(f"{name1}. Возьмите несколько конфет со стола, но не более 28: "))
    except:
        print("Нужно вводить число конфет, которое хотите убрать со стола!")
    if player < 1 or player > 28:
        try:
            player = int(input(f"{name1}. Соберитесь! Вы можете проиграть! Возьмите несколько конфет со стола, но не более 28: "))
        except:
            print(f"{name2} победил! Поздравляем!!!")
            exit()
        if player < 1 or player > 28:
            print(f"{name2} победил! Поздравляем!!!")
            exit()
    candies = candies - player
    if candies == 0:
        print(f"{name1} победил! Поздравляем!!!")
        exit()
    elif candies < 0:
        print(f"Конфет было меньше) Но все-равно {name1} победил! Поздравляем!!!")
        exit()
    else:
        print(f"На столе осталось {candies} конфет.")

def variant1(variant):
    name1 = str(input("Игрок 1 введите ваше имя: "))
    name2 = str(input("Игрок 2 введите ваше имя: "))
    lot_motion(name1, name2, variant)
    
def bot_motion ():
    global candies
    if randint(1, 5) == 1:
        if candies > 28:
            n = randint(1, 28)
        else:
            n = randint(1, candies)
    else:
        n = candies % 29
    if n != 0:
        print(f"Робот взял {n} конфет.")
    else:
        n = randint(1, 28)
        print(f"Робот взял {n} конфет.")
    candies = candies - n
    if candies == 0:
        print("Робот победил. Не расстраивайтесь. Попробуйте еще раз.")
        exit()
    else:
        print(f"На столе осталось {candies} конфет.")

def variant2(variant):
    name1 = str(input("Введите ваше имя: "))
    name2 = "Робот"
    lot_motion(name1, name2, variant)
    
  
if variant == 1:
    variant1(variant)
elif variant == 2:
    variant2(variant)
else:
    print("Вы ошиблись, попробуйте еще раз.")