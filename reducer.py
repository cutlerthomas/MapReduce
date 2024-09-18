#!/bin/python3

from operator import itemgetter
import sys

max = -99999999999
min = 999999999999
total_price = 0
total = 0
for line in sys.stdin:
    total += 1
    price = line.strip()
    price = int(price)

    if price > max:
        max = price
    if price < min:
        min = price

    total_price += price

average = total_price/total
  
print(f'Min price: {min}')
print(f'Max price: {max}')
print(f'Average price: {average}')
print(f'# of car sales used: {total}')