import csv

with open("books.csv", encoding='cp1251') as r_file:
    # Создаем объект reader, указываем символ-разделитель ";"
    file_reader = csv.DictReader(r_file, delimiter=";")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 1
    # Для пункта задания 3
    cnt = 0
    # Считывание данных из CSV файла
    for lst in file_reader:
        count += 1
        if len(lst["Название"]) > 30:
            cnt += 1
    
    print(f'Всего в файле {count} строк.')
    print(f'Имеющих длинное назвоне {cnt} строк.')
