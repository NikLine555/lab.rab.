import pickle

# Пример данных: страны и количество медалей за 6 последних летних Олимпиад
medals = {
    "USA":      [46, 45, 46, 44, 46, 39],
    "China":    [32, 51, 38, 38, 26, 38],
    "Russia":   [28, 27, 23, 24, 32, 19],
    "Germany":  [41, 44, 49, 44, 42, 42],
    "UK":       [19, 29, 27, 29, 27, 22],
    "France":   [33, 30, 32, 34, 42, 33],
    "Australia":[16, 17, 24, 46, 35, 29]
}

# 1) Вывести список всех стран и суммарное количество медалей за 6 Олимпиад
print("Список стран и суммарное количество медалей:")
for country, results in medals.items():
    total = sum(results)
    print(f"{country}: {total}")

# 2) Найти страны с максимальным и минимальным средним числом медалей
averages = {c: sum(m) / len(m) for c, m in medals.items()}
max_country = max(averages, key=averages.get)
min_country = min(averages, key=averages.get)

print(f"\nСтрана с максимальным средним числом медалей: {max_country} ({averages[max_country]:.2f})")
print(f"Страна с минимальным средним числом медалей: {min_country} ({averages[min_country]:.2f})")

# 3) Для каждой страны определить год с наибольшим количеством медалей
print("\nГоды с наибольшим числом медалей для каждой страны (номер олимпиады 1-6):")
for country, results in medals.items():
    max_medals = max(results)
    year = results.index(max_medals) + 1
    print(f"{country}: Олимпиада {year} — {max_medals} медалей")

# 4) Выделить страны с ростом более 20% от первого года
print("\nСтраны с ростом более 20% от первого года:")
for country, results in medals.items():
    first = results[0]
    last = results[-1]
    if last > 1.2 * first:
        print(f"{country}: рост с {first} до {last} медалей")

# Сохранение словаря в бинарный файл
with open("data.pickle", "wb") as f:
    pickle.dump(medals, f)

print("\nДанные сохранены в файл data.pickle")

# Чтение данных из бинарного файла (пример)
with open("data.pickle", "rb") as f:
    loaded_medals = pickle.load(f)

print("\nДанные загружены из файла:")
print(loaded_medals)
