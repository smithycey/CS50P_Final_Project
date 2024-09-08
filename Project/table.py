from menu import *
from prettytable import PrettyTable
from tabulate import tabulate


######## > For use by the test file only < #######

items_list = [key for key in Food.basket.keys()]

item_list_str = ""

for key in items_list:
    item_list_str += key + "\n"

qty_list = [value for key, value in Food.basket.items() for i, value in enumerate(Food.basket[key]) if i == 0]

qty_total = 0

for qty in qty_list:
    qty_total += qty

prices_list = [value for key, value in Food.basket.items() for i, value in enumerate(Food.basket[key]) if i == 1]


order_amount = 0

for price in prices_list:
    order_amount += price


order_list_headers = ["Product", "Qty", "Price" ]

table = []

for item, qty, price in zip(items_list, qty_list, prices_list):
    table.append([item, qty, f"£{price}"])
table.append(["Total", qty_total, f"£{order_amount}"])

########################################################