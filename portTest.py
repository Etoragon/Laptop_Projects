import socket

def is_port_open(port):
    print(port)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex(('localhost',port))
        if result == 0:
            return True
        else:
            return False
    except socket.error:
        print('error!')
        return False
    finally:
        sock.close()

start_port = 1
end_port = 100

open_ports = []
for port in range(start_port, end_port + 1):
    if is_port_open(port):
        open_ports.append(port)

print("Open ports: ")
for port in open_ports:
    print(port)
