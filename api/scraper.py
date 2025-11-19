import requests
from bs4 import BeautifulSoup

def fetch_olx(query):
    url = f"https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    cars = []

    for item in soup.select("li.sc-1fcmfeb-2"):
        title = item.select_one("h2")
        price = item.select_one("span")

        if title and price:
            cars.append({
                "title": title.get_text(strip=True),
                "price": price.get_text(strip=True)
            })

    return cars
