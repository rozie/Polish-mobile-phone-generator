# /usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from itertools import product

prefix_file = "prefiksy.txt"

with open(prefix_file, "r") as f:
    prefixes = set(f.read().splitlines())


def generate_N_letter_numbers(prefix, max_length):
    
    digits = '0123456789'
    results = []
    remaining_length = max_length - len(prefix)
    if remaining_length > 0:
        for suffix in product(digits, repeat=remaining_length):
            results.append(prefix + ''.join(suffix))    
    return results


for prefix in prefixes:
    numbers = generate_N_letter_numbers(prefix=prefix, max_length=9)
    for number in numbers:
        print(number)