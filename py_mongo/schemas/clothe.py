def clothe_entity(item) -> dict:
    return {
        "id": str(item["id"]),
        "url_clothe": item["url_clothe"],
        "brand_name": item["brand_name"],
        "product_name": item["product_name"],
        "prise": item["prise"]
    }


def clothes_entity(entity) -> list:
    return [clothe_entity(item)for item in entity]
