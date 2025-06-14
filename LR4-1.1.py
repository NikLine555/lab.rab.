import requests
import json
import os

def get_asian_countries():
    url = "https://restcountries.com/v3.1/region/asia"
    response = requests.get(url)
    response.raise_for_status()
    countries = response.json()
    filtered = []

    for c in countries:
        population = c.get('population', 0)
        if population > 30_000_000:
            name = c.get('name', {}).get('common', 'Unknown')
            capital = c.get('capital', ['Unknown'])[0]
            area = c.get('area', 0)
            flag_url = c.get('flags', {}).get('png', '')
            filtered.append({
                "name": name,
                "capital": capital,
                "area": area,
                "population": population,
                "flag_url": flag_url
            })
    return filtered

def save_results(data, filename="results.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def download_flags(countries, folder="flags"):
    os.makedirs(folder, exist_ok=True)
    for country in countries:
        url = country.get("flag_url")
        if not url:
            continue
        try:
            r = requests.get(url)
            if r.status_code == 200:
                path = os.path.join(folder, f"{country['name'].replace(' ', '_')}.png")
                with open(path, "wb") as f:
                    f.write(r.content)
                print(f"Флаг {country['name']} сохранён: {path}")
            else:
                print(f"Не удалось скачать флаг {country['name']}")
        except Exception as e:
            print(f"Ошибка при скачивании флага {country['name']}: {e}")

def main_api_part():
    countries = get_asian_countries()
    # Добавляем плотность населения
    for c in countries:
        c['density'] = c['population'] / c['area'] if c['area'] > 0 else 0
    # Сохраняем в JSON
    save_results(countries)
    # Сортируем по плотности и берём топ-5
    top5 = sorted(countries, key=lambda x: x['density'], reverse=True)[:5]

    print("Топ-5 азиатских стран по плотности населения:")
    for c in top5:
        print(f"{c['name']} — {c['density']:.2f} чел/км²")

    # Скачиваем флаги топ-5
    download_flags(top5)

if __name__ == "__main__":
    main_api_part()
