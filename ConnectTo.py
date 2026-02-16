import socket

HOST = ''

PORT = ''

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.timeout(5.0)



conn.close()