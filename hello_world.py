import math
import os
import sys

import requests

print("hello world")
print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


name = input("Your name ?")
print("Hello ,", name)

r = requests.get("https://google.com")
print(r.status_code)

