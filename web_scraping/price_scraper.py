import bs4
import requests as r

def getPrice(productUrl):
    res = r.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#variant_info46644 > div.price > span')
    return elems[0].text.strip()

price = getPrice('https://www.douglas.lt/katalogas/rich-pure-luxury-color-safe-shampoo/')
print('Price is: ' + price)

    
