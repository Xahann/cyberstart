import socket
from timeit import default_timer

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("services.cyberprotection.agency", 9999))
t = default_timer()
data = s.recv(17)
l = data.split(b"\n")
solution = int(int(l[0]) * int(l[1]) / int(l[2]))
s.sendall(bytes(solution) + b"\n")
t2 = default_timer() - t
print("Too slow by ", round(t2 - 0.1, 4), "seconds")
secret_message = s.recv(128)
print(secret_message)
