# Questo programma riceve in input # Questo programma riceve in input un indirizzo IP e un range di porte
# scansionerà le porte nel range di quell'indirizzo IP e chiederà i verbi HTTP ammessi
# stampa in uscita la lista delle porte e le risposte ai verbi HTTP

import socket
import requests
import http.client

# Funzione che fa lo scan delle porte nel range
# e ritorna una lista con lo stato di ogni porta
def scan(target, start, end):
        stato_porte = []
        inizio = int(start)
        fine = int(end)
        for port in range(inizio,fine+1):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                risultato = sock.connect_ex((target,port))
                if risultato == 0:
                        print("La porta", port, "è aperta")
                else:
                        print("La porta", port, "è chiusa")
                sock.close()

# Funzione che restituisce i verbi HTTP abilitati
def verbi_HTTP(target, port, path):
        try:
                connection = http.client.HTTPConnection(target,port)
                connection.request('OPTIONS','/' + path)
                r = connection.getresponse()
                methods = r.getheader("Allow")
                if methods:
                        methods_list = methods.split(",")
                        print("I verbi HTTP sono:")
                        for method in methods_list:
                                print(f"-{method.strip()}")
                else:
                        print("Impossibile determinare i verbi")

                connection.close()
        except ConnectionRefusedError:
                print("Connessione fallita")
        return r.getheader("Allow")

# Funzione che utilizza i verbi abilitati e stampa il risultato della risposta di ognuno
def utilizzo_verbi(verbi, target, port, path):
        connection = http.client.HTTPConnection(target, port)
        methods_list = verbi.split(",")
        for method in methods_list:
                connection.request("{method.strip()}",'/' + path)
		r = connection.getresponse()
                print("\nCon il verbo " + method.strip() +  " otteniamo come risposta: ",r)
                print(f"Codice di stato: {r.status}")
                body = r.read().decode("utf-8")
                print(f"Contenuto della risposta: {body}")
                print("FINE")
                print("-------------------------------------------------------------------------------------------------------------")
        connection.close()

# Provo i verbi trovati singolarmente
def prova_verbi(target, port, path, verbi):
        ciclo = "ok"
        while ciclo == "ok":
                print("I verbi ammessi sono: " + verbi)
                verbo = input("Inserisci il verbo da provare: ")
                connection = http.client.HTTPConnection(target, port)
                connection.request(verbo,'/' + path) 
                r = connection.getresponse()
                print("\nCon il verbo " + verbo +  " otteniamo come risposta: ",r)
                print(f"Codice di stato: {r.status}")
                body = r.read().decode("utf-8")
                print(f"Contenuto della risposta: {body}")
                connection.close()
                print("FINE")
                print("-------------------------------------------------------------------------------------------------------------")
                ciclo = input("Vuoi continuare? ")



# Acquisisco IP e range delle porte
target_IP = input("Inserisci l'indirizzo IP da testare: ")
start_port = input("Inserisci la porta iniziale: ")
end_port = input("Inserisci la porta finale: ")
#Faccio lo scan e stampo
scan(target_IP, start_port, end_port)

# Ottengo i verbi HTTP abilitati in una porta e stampo quali sono
porta = input("\nInserisci la porta di input: ")
percorso = input("Inserisci il path di destinazione: ") #Il percorso è del tipo Server:localhost
verbi_ammessi = verbi_HTTP(target_IP, porta, percorso)
# Parte per il test dei verbi
print("\n------------------Test dei verbi HTTP-----------------")
selettore = input("Vuoi testare i verbi singolarmente <S> o tutti insieme <P>? ")
if selettore == "S":
        # Se voglio testare i verbi singolarmente
        new_percorso = input("Inserisci il percorso in cui utlizzare i verbi: ") #Il percorso è del tipo phpMyAdmin/index.php?db=metasploit&token=51235f782f7f1c4614cdce17c9692068
        prova_verbi(target_IP, porta, new_percorso, verbi_ammessi)
elif  selettore == "P":
	# Se voglio testare tutti i verbi contemporaneamente
        new_percorso = input("Inserisci il percorso in cui utlizzare i verbi: ") #Il percorso è del tipo phpMyAdmin/index.php?db=metasploit&token=51235f782f7f1c4614cdce17c9692068
        utilizzo_verbi(verbi_ammessi, target_IP, porta, new_percorso)
else:
        print("Verbi HTTP non testasti")
