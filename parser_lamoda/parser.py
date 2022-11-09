import asyncio
import aiohttp
import uuid
import bs4

from mg_db.config.mongo_db import database


async def get_page_data(page):
    async with aiohttp.ClientSession() as session:
        response = await session.get(
            url=f'https://www.lamoda.by/c/477/clothes-muzhskaya-odezhda/?sitelink=topmenuM&l=2&page={page}')
        soup = bs4.BeautifulSoup(await response.text(), "lxml")
        cards = soup.find_all("div", class_="x-product-card__card")
        for clothe in cards:
            url_clothe = "https://www.lamoda.by" + clothe.find("a").get("href")
            brand_name = clothe.find("div", class_="x-product-card-description__brand-name")
            product_name = clothe.find("div", class_="x-product-card-description__product-name")
            prise = clothe.find("span", class_="x-product-card-description__price-single "
                                               "x-product-card-description__price-WEB8507_price_no_bold")
            new_prise = clothe.find("span", class_="x-product-card-description__price-new "
                                                   "x-product-card-description__price-WEB8507_price_no_bold")
            id_card = str(uuid.uuid4())
            res = {
                "_id": id_card,
                "url_clothe": url_clothe,
                "brand_name": brand_name.text,
                "product_name": product_name.text,
                "prise": new_prise.text if new_prise else prise.text,
            }
            await database.get_collection("clothe").insert_one(res)
        print(f"Page:{page}")


async def gather_data():
    tasks = []

    for page in range(1, 20):
        task = asyncio.create_task(get_page_data(page))
        tasks.append(task)
    await asyncio.gather(*tasks)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(gather_data())
