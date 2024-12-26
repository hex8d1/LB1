import requests
import matplotlib.pyplot as plt
from datetime import datetime

def fetch_rates(valcode, start_date, end_date):
    url = (
        "https://bank.gov.ua/NBU_Exchange/exchange_site"
        f"?start={start_date}"
        f"&end={end_date}"
        f"&valcode={valcode}"
        f"&sort=exchangedate"
        f"&order=asc"
        f"&json"
    )
    r = requests.get(url)
    if r.status_code == 200:
        try:
            return r.json()
        except:
            return []
    return []

def plot_rates(data, valcode):
    if not data:
        return
    ds = [i["exchangedate"] for i in data]
    rs = [i["rate"] for i in data]
    ds = [datetime.strptime(d, "%d.%m.%Y") for d in ds]
    plt.plot(ds, rs, marker='o')
    plt.title(f"{valcode} NBU")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

valcode = "USD"
start_date = "20241218"
end_date   = "20241225"
data = fetch_rates(valcode, start_date, end_date)
plot_rates(data, valcode)
