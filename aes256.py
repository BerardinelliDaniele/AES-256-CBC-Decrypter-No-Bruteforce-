# Berardinelli Daniele | CC 2023 UNIVPM 
# Tramite questo programma, è possibile decifrare un base64 criptato con AES_256 CBC avendo la chiave e l'IV. 

import base64
from Crypto.Cipher import AES

messaggio_b64 = "" #Inserisci qui il messaggio in base64
chiave = b'' #Inserisci qui la chiave di crittografia
iv = b'' #Inserisci qui l'IV

messaggio = base64.b64decode(messaggio_b64) 

iv_messaggio = messaggio[:16]


cipher = AES.new(chiave, AES.MODE_CBC, iv_messaggio)
messaggio_decriptato = cipher.decrypt(messaggio[16:])


messaggio_unpaddato = messaggio_decriptato[:-messaggio_decriptato[-1]]
messaggio_finale = messaggio_unpaddato.decode('utf-8')

print(messaggio_finale)