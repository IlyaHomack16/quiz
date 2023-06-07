import random, math

quest_list = {"Сколько лет Илье?": "12", "Сколько лет Илья занимается питоном?": "2", "Кто преподаватель Ильи по питону?": "Алина", "Как зовут маму Ильи?": "Иванова Вероника Александровна", "Тян гей?": "да"}
s = 4
res = 0

for i in range(3):
    m = list(quest_list.keys())[random.randint(0, s)]
    print(m)
    j = input()
    if j == quest_list[m]:
        print("Ответ верный!")
        res += 1
    else:
        print(f"Правильный ответ: {quest_list[m]}.")
    quest_list.pop(m)
    s -= 1
print(f"Вы справились на {math.floor((res / 3) * 100)}%!")