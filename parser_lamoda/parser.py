import requests
import bs4


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
        print(
            f'URL:{url_clothe},\nBrand_name:{brand_name.text},\n'
            f'Product_name:{product_name.text}\n'
            f'Prise:{new_prise.text if new_prise else prise.text}\n'
            f'==========================================================='
        )


def main():
    get_data('https://www.lamoda.by/c/959/clothes-sports-myzskaia-odezda')


if __name__ == "__main__":
    main()
