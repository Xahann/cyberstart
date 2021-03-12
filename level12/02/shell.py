#!/usr/bin/env python3
import requests
import sys
from tqdm import tqdm

session = requests.Session()


response = session.get(
    "https://game.joincyberstart.com/base-headquarters",
    cookies={"Cyber_Protection_Agency": "0vu34oap0bukiokhl5p4dr1orc"},
)

import re

def run(command):
    challenge_url = f"https://game.joincyberstart.com/challenge?base=1&level=12&challenge=2&csrf={csrf_base}"

    response3 = session.post(
        challenge_url,
        cookies={"Cyber_Protection_Agency": "0vu34oap0bukiokhl5p4dr1orc"},
        data={
"drink-name": f'$({command})',

        },
    )

    remove_changing = re.search(r'input type="submit" value="Order drink" class="btn">\s*<\/div>([\s\S]*?)<\/form>', response3.text)
    print(remove_changing.group(1).replace('<br>','\n'))
        # print(list(diff)[2])

matches = re.search(r'csrf=(.*?)"', response.text)
csrf_base = matches.group(1)

while True:
    command = input(' > ')
    run(command)

# run("cryptonite -n;" + command)
# print(response3.text)
