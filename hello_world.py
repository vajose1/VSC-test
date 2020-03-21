import math
import os

import requests

print("hello world")


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


name = input("Your name ?")
print("Hello ,", name)

r = requests.get("https://google.com")
print(r.status_code)

