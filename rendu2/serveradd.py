from socket import *
import sys

#Server socket
mysocket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
mysocket.bind(('', 1234))

(res, adr_client) = mysocket.recvfrom(60)

sum=int.from_bytes(res[0:4], byteorder="big")+int.from_bytes(res[4:8], byteorder="big")


mysocket.sendto(int.to_bytes(sum, 8, byteorder="big"), adr_client)

mysocket.close()
