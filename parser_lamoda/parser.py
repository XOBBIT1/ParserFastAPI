import requests
import bs4
from mg_db.commands.command import ClotheRepo


def get_data(url):
    r = requests.get(url=url)
    soup = bs4.BeautifulSoup(r.text, "lxml")

    cards = soup.find_all("div", class_="x-product-card__card")
    for clothe in cards:
        url_clothe = "https://www.lamoda.by" + clothe.find("a").get("href")
        brand_name = clothe.find("div", class_="x-product-card-description__brand-name")
        product_name = clothe.find("div", class_="x-product-card-description__product-name")
        prise = clothe.find("span", class_="x-product-card-description__price-single "
                                           "x-product-card-description__price-WEB8507_price_no_bold")
        new_prise = clothe.find("span", class_="x-product-card-description__price-new "
                                               "x-product-card-description__price-WEB8507_price_no_bold")
        res = {
            "url_clothe": url_clothe,
            "brand_name": brand_name.text,
            "product_name": product_name.text,
            "prise": new_prise.text if new_prise else prise.text,
        }
        clothe_list = ClotheRepo.insert(res)
        print(clothe_list)
    return res


def main():
    get_data('https://www.lamoda.by/c/959/clothes-sports-myzskaia-odezda')


if __name__ == "__main__":
    main()
