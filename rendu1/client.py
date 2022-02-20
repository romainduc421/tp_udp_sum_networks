import sys
import re
from socket import *

ip_regexp = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
port_regexp = "^((6553[0-5])|(655[0-2][0-9])|(65[0-4][0-9]{2})|(6[0-4][0-9]{3})|([1-5][0-9]{4})|([0-5]{0,5})|([0-9]{1,4}))$"
#A port is a 16-bit unsigned integer ranging from 0 to 65535
#taken from https://ihateregex.io/expr/port/
if len(sys.argv)!=3:
    print("Nb d'arguments incorrect", file=sys.stderr)
    print("usage : \n\tpython3 client.py <IP_adress> <n° port>", file=sys.stdout)
    sys.exit(-1)
else:
    try:
        adr_ip, port = sys.argv[1], sys.argv[2]
        res = (adr_ip, port)

        if re.search(ip_regexp, adr_ip)==False:
            print("erreur formatage IP", file=sys.stderr)
            sys.exit(1)

        if re.search(port_regexp, port)==False :
            print("erreur formatage no port", file=sys.stderr)
            sys.exit(2)
    except TypeError as e:
        print(e, file=sys.stderr)


mysocket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
message = "J'aime le cours de Réseaux 2"

message_bytes = bytes(message, "utf-8")
sent = mysocket.sendto(message_bytes,(adr_ip, int(port)))

(resultat_bytes, adresse_serveur) = mysocket.recvfrom(60)

resultat = str(resultat_bytes, "utf-8")
print(resultat)
mysocket.close()
