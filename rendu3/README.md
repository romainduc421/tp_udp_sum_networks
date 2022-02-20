##Experience realisee
Si on alterne l'envoi des messages entre les 2 clients nous sommes censés avoir des mauvais résultats
Plusieurs clients envoient des requêtes pour faire une somme avec des adresses IP identiques ou différentes :

e.g. l'un des clients fournit la premiere operande puis le deuxieme client sa premiere operande
( le serveur ne peut pas faire la différence et effectue la somme des deux, i.e. la 1ere operande du 1er client et la 1ere operande du 2e client et retourne la somme au premier client )
enfin, le deuxième client fournit sa deuxième opérande, puis le premier fournit sa deuxieme operande
( somme des deux deuxièmes opérandes des deux clients renvoyée au 2e client )

exemple arbitraire (pour le deuxième envoi de nombre au serveur, on envoie l'entier du 2eme client d'abord):
$ python3 serveradd2.py &

$ python3 clientadd2.py 127.0.0.1 1234
donnez le premier entier :
1
donnez le deuxième entier :

puis dans un autre terminal :
$ python3 clientadd2.py 10.11.117.169 1234
donnez le premier entier :
1
donnez le deuxième entier :
2
La somme vaut :  2



il faut donc enregistrer le couple (adrIP, port) du client précédent afin de ne pas effectuer la somme si l'adresse IP est distincte.
par exemple dans un dict()
