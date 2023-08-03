#!/usr/bin/env python3

element_length =  __import__('9-element_length').element_length

print(element_length.__annotations__)
print(element_length(["Jean", "marc", "9", "10", "Michel"]))
print(element_length(([20, 10], "9", "10", "Michel")))
