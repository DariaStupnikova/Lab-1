import csv

with open("books.csv", encoding='cp1251') as r_file:
    file_reader = csv.DictReader(r_file, delimiter=";")
    autor = input() #Ввод ФИО автора
    for lst in file_reader: #Пробегаемся по массиву, ищем совпадения между запросом и файлом
        if autor==lst["Автор (ФИО)"]:
            print(lst["Название"])
    
