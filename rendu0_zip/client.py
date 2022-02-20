from socket import *

mysocket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
message = "J'aime le cours de Réseaux 2"

message_bytes = bytes(message, "utf-8")

sent = mysocket.sendto(message_bytes,("127.0.0.1", 1234))

(resultat_bytes, adresse_serveur) = mysocket.recvfrom(60)

resultat = str(resultat_bytes, "utf-8")
print(resultat)
mysocket.close()


