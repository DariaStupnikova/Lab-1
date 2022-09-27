import csv
import random

rand = []
cnt = 0
for i in range(20):
    num = random.randint(1, 9410)
    rand.append(num)
rand.sort()
with open("books.csv", encoding='cp1251') as r_file:
    f = open('bibly.txt', 'w')
    file_reader = csv.DictReader(r_file, delimiter=";")
    count = 1
    for lst in file_reader:
        count += 1
        if count in rand:
            cnt += 1
            f.write(f'{cnt}. {lst["Автор (ФИО)"]}. {lst["Название"]} - {lst["Дата поступления"][6:10]} \n')
    f.close()