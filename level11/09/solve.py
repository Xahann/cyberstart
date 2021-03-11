#!/usr/bin/env python3
import requests
import sys

session = requests.Session()


response = session.get(
    "http://easy-filebox.com/u/1/account/files",
    cookies={
        "Cyber_Protection_Agency": "0vu34oap0bukiokhl5p4dr1orc",
        "cyber_discovery": "m1ii6l0b84cb7m4vku8dsmuqgf",
        "SQL_SESSuser": "342423961827",
    },
)

print(response.text)