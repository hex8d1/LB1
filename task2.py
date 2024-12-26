import requests
from datetime import datetime, timedelta

def get_nbu_currency_rates_previous_week(valcode='USD'):
   

    today = datetime.now()

    start_date_dt = today - timedelta(days=7)

    end_date_dt = today - timedelta(days=1)

    start_date_str = start_date_dt.strftime('%Y%m%d')
    end_date_str   = end_date_dt.strftime('%Y%m%d')

    url = (
        "https://bank.gov.ua/NBU_Exchange/exchange_site"
        f"?start={start_date_str}"
        f"&end={end_date_str}"
        f"&valcode={valcode}"
        f"&sort=exchangedate"
        f"&order=desc"
        f"&json"
    )

    print(f"Запрос к API НБУ:\n{url}\n")

    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            return data
        except ValueError:
            print("Ошибка при парсинге ответа JSON")
            return []
    else:
        print(f"Ошибка при запросе. Код ответа: {response.status_code}")
        return []

if __name__ == "__main__":

    rates = get_nbu_currency_rates_previous_week()


    for item in rates:
        exchangedate = item.get('exchangedate')
        cc = item.get('cc')
        r030 = item.get('r030')
        rate = item.get('rate')
        print(f"Дата: {exchangedate}, Валюта: {cc}, Код: {r030}, Курс: {rate}")
