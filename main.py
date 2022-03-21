from bs4 import BeautifulSoup
import requests
from art import tprint
from colorama import init, Fore


product = input("Enter product name:")
def pazaruvaj_search(product):
    count = 0
    product_pazaruvaj = product.replace(" ", "+")
    url_pazaruvaj = f"https://www.pazaruvaj.com/CategorySearch.php?st={product_pazaruvaj}"

    result_pazaruvaj = requests.get(url_pazaruvaj)
    doc_pazaruvaj = BeautifulSoup(result_pazaruvaj.text, "html.parser")
    for a in doc_pazaruvaj.find_all('a', {"class": "price"}, title=True):
        print("Product:", a["title"])
        print(Fore.RED + "Price", a.text)
        print(Fore.RESET + "Found at", a["href"])
        print("________________________________________")
        print("________________________________________")
        count += 1
        if count == 5:
            break

def emag_search(product):
    price = ""
    count = 0
    counter = 0
    product_emag = product.replace(" ", "%20")
    url_emag = f"https://www.emag.bg/search/{product_emag}?ref=effective_search"
    result_emag = requests.get(url_emag)
    doc_emag = BeautifulSoup(result_emag.text, "html.parser")
    for card in doc_emag.find_all('a', {"class": "card-v2-title semibold mrg-btm-xxs js-product-url"}):
        print("Product:", card.text)
        counter += 1
        secondary = 0
        for price in doc_emag.find_all('p', {"class": "product-new-price"}):
            secondary += 1
            if secondary == counter:
                price_printable = price.text
                price_printable = price_printable.replace(".", ',')
                price_printable = price_printable[:-6] + "." + price.text[-6:]
                print(Fore.RED + "Price:", price_printable, "лв.")
                break

        print(Fore.RESET + "Found at ", card["href"])
        print("________________________________________")
        print("________________________________________")
        count += 1
        if count == 5:
            break

def vario_search(product):
    count = 0
    counter = 0
    product_vario = product.replace(" ", "+")
    url_vario = f"https://www.vario.bg/search.php?s={product_vario}"
    result_vario = requests.get(url_vario)
    doc_vario = BeautifulSoup(result_vario.text, "html.parser")
    for card in doc_vario.find_all('a', {"class": "product_permalink"}):
        print("Product:", card.text)
        counter += 1
        secondary = 0
        for price in doc_vario.find_all('strong'):
            letter = price.text[0]
            is_letter = letter[0].isalpha()
            if is_letter != True:
                secondary += 1
                if secondary == counter:
                    price_printable = price.text
                    #price_printable = price_printable.replace('"', ' ')
                    #price_printable = price_printable[:-6] + "." + price.text[-6:]
                    print(Fore.RED + "Price:", price_printable)
                    print(Fore.RESET + "Found at ", card["href"])
                    print("________________________________________")
                    print("________________________________________")
                    break
        count += 1
        if count == 5:
            break

def gplay_search(product):
    count = 0
    counter = 0
    result = ''
    product_gplay = product.replace(" ", "+")
    url_gplay = f"https://gplay.bg/търсене?search_text={product_gplay}"
    result_gplay = requests.get(url_gplay)
    doc_gplay = BeautifulSoup(result_gplay.text, "html.parser")
    for card in doc_gplay.find_all('a', {"class": "product-name"}):
        print("Product:", card["title"])
        counter += 1
        secondary = 0
        for price in doc_gplay.find_all('div', {"class": "normal-price"}):
            secondary += 1
            if secondary == counter:
                price = str(price)
                has_dot =[i for i in price if i == "."]
                price = [i for i in price if i.isdigit()]
                price = ''.join(price)
                if len(has_dot) >= 1:
                    price = price[:-2] + "." + price[-2:]
                print(Fore.RED + "Price:" + price)
                break
        print(Fore.RESET + "Found at ", card["href"])
        print("________________________________________")
        print("________________________________________")
        count += 1
        if count == 5:
            break

def nikem_search(product):
    main_info = ''
    count = 0
    counter = 0
    product_nikem = product.replace(" ", "+")
    url_nikem = f"http://nikem-bg.net/search.php?p={product_nikem}"
    result_nikem = requests.get(url_nikem)
    doc_nikem = BeautifulSoup(result_nikem.text, "html.parser")
    for card in doc_nikem.findAll('div', {"class": "item"}):
        price = card.findAll("strong")
        card = card.findAll("a")
        price = str(price)
        price = price[19:]
        price = price[:-16]
        print("Product:", card[1].text)
        print(Fore.RED + "Price:", price, "лв.")
        print(Fore.RESET + "Found at  http://nikem-bg.net/" + card[0]["href"])
        print("________________________________________")
        print("________________________________________")
        count += 1
        if count == 5:
            break
tprint('PAZARUVAJ')
pazaruvaj_search(product)
tprint('EMAG')
emag_search(product)
tprint("VARIO")
vario_search(product)
tprint("Gplay")
gplay_search(product)
tprint("NIKEM.NET")
nikem_search(product)
while True:
    var = 1
