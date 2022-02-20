from socket import *
import sys

#Server socket

mysocket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
mysocket.bind(('', 1234))

num1, num2, add = 0, 0, 0

while True:

    num1, adr_client = mysocket.recvfrom(60)
    print('first number received : ', num1)

    num2, adr_client = mysocket.recvfrom(60)
    print('second number received : ', num2)

    add=int.from_bytes(num1[0:4], byteorder="big")+int.from_bytes(num2[0:4], byteorder="big")

    mysocket.sendto(int.to_bytes(add, 8, byteorder="big"), adr_client)
    add=0

mysocket.close()
