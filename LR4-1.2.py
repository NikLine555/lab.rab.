import requests
from bs4 import BeautifulSoup
import csv
import time

# Настройки
base_url = "https://worldathletics.org/records/toplists"
years = range(2001, 2025)
genders = ['men', 'women']
events = {
    '60m': '60-metres',
    '100m': '100-metres',
    '200m': '200-metres',
    '400m': '400-metres'
}

def parse_top1_result(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            print(f"Ошибка загрузки: {url}")
            return None
        soup = BeautifulSoup(r.text, 'html.parser')

        # На сайте таблица результатов может иметь класс 'records-table' или похожий
        table = soup.find('table')
        if not table:
            print(f"Таблица не найдена на {url}")
            return None

        first_row = table.find('tbody').find('tr')
        if not first_row:
            print(f"Нет результатов на {url}")
            return None

        cells = first_row.find_all('td')
        # Проверим количество ячеек, на сайте  обычно:
        # 0 - место, 1 - спортсмен, 2 - страна, 3 - результат, 4 - дата
        athlete = cells[1].text.strip()
        country = cells[2].text.strip()
        time_result = cells[3].text.strip()
        competition_date = cells[4].text.strip()

        return athlete, country, time_result, competition_date
    except Exception as e:
        print(f"Ошибка парсинга {url}: {e}")
        return None

def main_scraping_part():
    results = []
    for gender in genders:
        for event_key, event_url_part in events.items():
            for year in years:
                # Формируем URL (пример):
                # https://worldathletics.org/records/toplists/sprint/outdoor/100-metres/men/year=2024
                url = f"https://worldathletics.org/records/toplists/sprint/outdoor/{event_url_part}/{gender}/year={year}"
                print(f"Обрабатываю: {url}")
                data = parse_top1_result(url)
                if data:
                    athlete, country, time_result, competition_date = data
                    results.append([year, gender, event_key, athlete, country, time_result, competition_date])
                time.sleep(0.5)  # не нагружаем сервер

    # Сохраняем в CSV
    with open("top_results.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Year', 'Gender', 'Event', 'Athlete', 'Country', 'Time', 'Date'])
        writer.writerows(results)

    print("Данные сохранены в top_results.csv")

if __name__ == "__main__":
    main_scraping_part()
