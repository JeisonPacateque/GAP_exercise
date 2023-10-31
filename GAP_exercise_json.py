#!/usr/bin/env python
# coding: utf-8

import json
from datetime import timedelta, datetime


def read_data(filename: str = "assets/products.json") -> list:
    with open(filename) as products:
        products_data = json.load(products)

    date_format = '%Y-%m-%d'
    for p in products_data:
        p['updated_at'] = datetime.strptime(p['updated_at'], date_format)

    return products_data


def sort_by_price(products_data: list) -> list:
    return sorted(products_data, key=lambda product: product['price'])


def calculate_average(products: list):
    prices = [p['price'] for p in products]

    return sum(prices) / len(prices)


def filter_old_updates(products, months=3):
    today = datetime.today()
    months_ago = today - timedelta(months * 30)
    filtered_products = []

    for p in products:
        if p['updated_at'] > months_ago:
            filtered_products.append(p)

    return filtered_products


def main():
    products = read_data()
    products = filter_old_updates(products)
    #print(products)
    sorted_by_price = sort_by_price(products)
    top_products = sorted_by_price[:10]
    avg = calculate_average(top_products)

    print(avg)


if __name__ == "__main__":
    main()
