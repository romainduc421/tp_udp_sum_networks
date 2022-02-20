#connexion simultanée de 2 clients sur la somme
#un premier client qui remplit la 1ere opérande
#le deuxième client remplit la 1e opérande
#puis le deuxième client remplit la 2e operande
from socket import *
from select import select
import copy
#Server socket

#clients=[]

cpt = 1
add = 0

mysocket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
mysocket.bind(('', 1234))
prev_client=('',1)

	#(clé, valeur) = (adrIP, premiere_operande)
clients = dict()
#clients = {}

# Listen for incoming datagrams
while True:


	data, adr_client = mysocket.recvfrom(60)

	#print("Received from %s message %s" %(data, adr_client))

	#print (clients)

	for adrIP in clients.copy():
		if(adr_client[0] == adrIP):
			add = clients[adr_client[0]] + int.from_bytes(data[0:4], byteorder='big')
	#add += int.from_bytes(data[0:4], byteorder='big')
			#print(add)
			mysocket.sendto(int.to_bytes(add, 8, byteorder='big'), adr_client)
			res = clients.pop(adr_client[0], None)
			#print(res)
			add = 0

	if(adr_client[0] not in clients):
		clients[adr_client[0]] = int.from_bytes(data[0:4], byteorder='big')

mysocket.close()
