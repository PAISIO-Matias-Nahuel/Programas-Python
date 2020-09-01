import bs4
import request

def getAmazonPrice(productURL)
    res = request.get(productURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('csspath')
    return elems.text.strip()

price = getAmazonPrice()
print('the price is ' + price)

