import csv
import json
from prettytable import PrettyTable

# Пищик Іван: створення CSV-файлу та його перетворення в JSON
try:  # Обробка виключної ситуації, якщо файл не вдається відкрити для запису
    with open('Data_1.csv', 'w', newline='') as csvfile:
        fieldnames = ['Sole proprietor', 'EDRPOU Code']  # Заголовки стовпців таблиці
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  # Створення об'єкта для запису даних у файл

        writer.writeheader()  # Запис заголовків у файл
        writer.writerow({'Sole proprietor': 'LLC ATB', 'EDRPOU Code': '30487219'})
        writer.writerow({'Sole proprietor': 'EPICENTR K LLC', 'EDRPOU Code': '32490244'})
        writer.writerow({'Sole proprietor': 'LLC AURORA', 'EDRPOU Code': '24905266'})
except FileNotFoundError:
    print("Файл Data_1.csv не знайдено!")

try:  # Обробка виключної ситуації, якщо файл не вдається відкрити для читання
    with open("Data_1.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")  # Читання даних із CSV-файлу
        table = PrettyTable()  # Створення об'єкта таблиці для гарного відображення даних
        table.field_names = ["ФОП", "Код ЄДРПОУ"]
        print("Українські ФОП:")

        data = {}  # Ініціалізація словника для зберігання даних
        for row in reader:  # Формування таблиці та заповнення словника
            Sole_proprietor = row['Sole proprietor']
            EDRPOU_Code = row['EDRPOU Code']
            table.add_row([Sole_proprietor, EDRPOU_Code])  # Додавання рядка до таблиці
            data[Sole_proprietor] = {"EDRPOU Code": EDRPOU_Code}  # Додавання запису в словник
        print(table)

        with open("Data_1.json", "w") as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)  # Запис даних у JSON-файл
        print("\nДані успішно збережені у форматі JSON у файлі Data_1.json")

except FileNotFoundError:
    print("Файл не знайдено!")

# Рожченко Іван: переписання даних з JSON-файлу у CSV
try:
    # Відкриття Data_1.csv для запису
    with open("Data_1.csv", "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()

        # Відкриття Data_1.json для читання
        with open("Data_1.json", "r") as jsonfile:
            Data_json = json.load(jsonfile)

        # Перенесення даних з Data_1.json у Data_1.csv
        for Sole_proprietor, EDRPOU_Code in Data_json.items():
            writer.writerow({'Sole proprietor': Sole_proprietor, 'EDRPOU Code': EDRPOU_Code['EDRPOU Code']})
        print("\nДані з Data_1.json у Data_1.csv було перенесено успішно.\n\nДодамо нові:")

        # Додавання нових даних
        writer.writerow({'Sole proprietor': 'LLC SILPO-FOOD', 'EDRPOU Code': '40720198'})
        writer.writerow({'Sole proprietor': 'NEW POST LLC', 'EDRPOU Code': '31316718'})

        print("ФОП: LLC SILPO-FOOD | Код ЄДРПОУ: 40720198\n"
            "ФОП: NEW POST LLC | Код ЄДРПОУ: 31316718\n"
            "\nДані було додано успішно\n")

except FileNotFoundError:
    print("Файл Data_1.csv або Data_1.json не знайдено!")
    exit()

# Виведення CSV-файлу у вигляді таблиці
try:
    with open("Data_1.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")

        # Створення таблиці
        table = PrettyTable()
        table.field_names = ["ФОП", "Код ЄДРПОУ"]
        print("Українські ФОП (оновлені):")

        # Додавання рядків до таблиці
        for row in reader:
            Sole_proprietor = row['Sole proprietor']
            EDRPOU_Code = row['EDRPOU Code']
            table.add_row([Sole_proprietor, EDRPOU_Code])

        # Виведення таблиці
        print(table)

except FileNotFoundError:
    print("Файл Data_1.csv не знайдено!")
    exit()
