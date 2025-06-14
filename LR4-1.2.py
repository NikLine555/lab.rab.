from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
import time

years = range(2001, 2025)
genders = ['men', 'women']
events = {
    '60m': '60-metres',
    '100m': '100-metres',
    '200m': '200-metres',
    '400m': '400-metres'
}

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

def parse_top1_result(url):
    try:
        driver.get(url)
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        table = soup.find('table')
        if not table:
            print(f"Таблица не найдена на {url}")
            return None

        first_row = table.find('tbody').find('tr')
        if not first_row:
            print(f"Нет результатов на {url}")
            return None

        cells = first_row.find_all('td')
        athlete = cells[1].text.strip()
        country = cells[2].text.strip()
        time_result = cells[3].text.strip()
        competition_date = cells[4].text.strip()

        return athlete, country, time_result, competition_date
    except Exception as e:
        print(f"Ошибка парсинга {url}: {e}")
        return None

def main():
    results = []
    for gender in genders:
        for event_key, event_slug in events.items():
            for year in years:
                url = f"https://worldathletics.org/records/toplists/sprints/{event_slug}/outdoor/{gender}/senior/{year}"
                print(f"Обрабатываю: {url}")
                data = parse_top1_result(url)
                if data:
                    athlete, country, time_result, competition_date = data
                    results.append([year, gender, event_key, athlete, country, time_result, competition_date])
                time.sleep(1)

    driver.quit()

    with open("top_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Year", "Gender", "Event", "Athlete", "Country", "Time", "Date"])
        writer.writerows(results)

    print("Готово! Данные сохранены в top_results.csv")

if __name__ == "__main__":
    main()
