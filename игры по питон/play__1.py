import random

print ("Я задумал число от 1 до 20. Угадайте, какое это число, за минимум попыток!")
print("Я буду давать подсказки")
n=random.randint(1,20)
n=random.randint(1, 20)

vib=int(input("Введите число:"))
pop=10

while vib!=n:
    while pop>0:
        if vib>n:
            print("Меньше..")
        else:
            print("Больше...")
        vib=int(input("Ваше предложение:"))
        pop -=1
    print("Ты потратил все попытки")
print("ты угадал")
        
        