print ("ИГРА БАШЕ")
print ("На столе лежат 16 камней. Мы по очереди берем от 1 до 3 камней")
print ("Проиграет тот, кому будет нечего брать.")
print ("Ваш ход - первый")
s=16
while s>0:
    print()
    i=int(input("Сколько берете камней? "))
    s=s-i    
    print("Осталось камней:", s, "Теперь мой ход.")
    if s>0:
        k=s%4
        s=s-k
        print("Я возьму камней:", k, "Осталось камней:", s)
        if s==0:
            print("Я выиграл! Слава электронному разуму!")
print()
print("Игра окончена!")
