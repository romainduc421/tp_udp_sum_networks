from socket import *
import sys

#Server socket
mysocket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
mysocket.bind(('', 1234))

(msg, adr_client) = mysocket.recvfrom(60)
print("adresse IP : "+adr_client[0]+"\nport : ", adr_client[1])

msg_str = str(msg, "utf-8")
msg_str=msg_str.upper()
msg_bytes = bytes(msg_str, "utf-8")
mysocket.sendto(msg_bytes, adr_client)

mysocket.close()
