import csv

with open("books.csv", encoding='cp1251') as r_file:
    file_reader = csv.DictReader(r_file, delimiter=";")
    mas = []
    for lst in file_reader:
        if lst["Жанр книги"] not in mas:
            mas.append(lst["Жанр книги"])
print(mas)