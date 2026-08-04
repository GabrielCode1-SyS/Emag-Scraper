#!/usr/bin/venv python3

try:
    import requests
except ImportError:
    sys.exit()
try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit()
try:
    import sys
except ImportError:
    exit()

class Information:

    def __init__(self,inStock,price,stars):
        self.inStock = inStock
        self.price = price
        self.stars = stars

    def sayDetails(self):
        print(f"PRICE: {self.price}\n")
        print(f"STOCK: {self.inStock}\n")
        print(f"STARS: {self.stars}")

def getInformation(url):

    # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36

    headers = {
        'User-Agent':(
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            'AppleWebKit/537.36 '
            '(KHTML, like Gecko) '
            'Chrome/120.0.0.0 Safari/537.36 '
        )
    }

    priceS = []

    reviewS = []

    stockS = []

    try:
        html = requests.get(url, headers=headers).text
    except requests.exceptions.MissingSchema:
        sys.exit()
    bs = BeautifulSoup(html, "html5lib")

    for price in bs.find_all('p', class_="product-new-price"):
        priceS.append(price.get_text(strip=True))

    for review in bs.find_all('span', class_="average-rating fw-semibold"):
        reviewS.append(review.get_text(strip=True))

    for stock in bs.find_all('div', class_="mb-1 fw-semibold fs-12 text-availability-in_stock"):
        stockS.append(stock.get_text(strip=True))

    return Information(stockS,priceS,reviewS)

randomVar = getInformation('https://www.emag.ro/search/calculatoare?ref=effective_search')

randomVar.sayDetails()