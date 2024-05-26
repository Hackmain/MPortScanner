import socket

target = "192.168.0.1"
common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995, 3389, 8080]

for p in common_ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    r = s.connect_ex((target, p))
    
    if r == 0:
        service = socket.getservbyport(p)
        print("[{} is open --> {}]".format(p, service))
    s.close()
