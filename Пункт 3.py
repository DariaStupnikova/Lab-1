import csv

with open("books.csv", encoding='cp1251') as r_file:
    file_reader = csv.DictReader(r_file, delimiter=";")
    autor = input()
    for lst in file_reader:
        if autor==lst["Автор (ФИО)"]:
            print(lst["Название"])
    