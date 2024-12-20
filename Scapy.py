# Programma per l'acquisizione di pacchetti con scapi e salvataggio in un file .pcap

# importo sniff per l'acquisizione e wrcap per il salvataggio
from scapy.all import sniff
from scapy.utils import wrpcap

# Fase di input per la gestione del programma
inter = input("Inserisci l'interfaccia dove vuoi acquisire i pacchetti: ") #eth0
cont_str = input("Inserisci quanti pacchetti vuoi catturare (0 per acquisizione continua): ")
cont = int(cont_str)
filtro = input("Inserisci il tipo di pacchetti che vuoi acquisire (all per acquisire tutti i tipi): ") #tcp, udp, >


if cont == 0:
        if filtro == "all":
                pacchetti = sniff(iface = inter, prn = lambda x: x.summary())
                print("Acquisizione finita")
                nome = input("Inserisci il nome del file: ")
                wrpcap(nome, pacchetti)
        else:
                pacchetti = sniff(iface = inter, filter = filtro, prn = lambda x: x.summary())
                print("Acquisizione finita")
                nome = input("Inserisci il nome del file: ")
                wrpcap(nome, pacchetti)
else:
        if filtro == "all":
                pacchetti = sniff(iface = inter, count = cont, prn = lambda x: x.summary())
                print("Acquisizione finita")
                nome = input("Inserisci il nome del file: ")
                wrpcap(nome, pacchetti)
        else:
                pacchetti = sniff(iface = inter, filter = filtro, count = cont, prn = lambda x: x.summary())
                print("Acquisizione finita")
                nome = input("Inserisci il nome del file: ")
                wrpcap(nome, pacchetti)



# In "nome" puoi inserire anche il path se vuoi salvarlo in una cartella differente altrimenti
# verrà salvato nella cartella corrente

# Per una successiva lettura del file posso eseguire Scapy direttamente da terminale inserendo
# sudo scapy
# pacchetti = rdpcap(NOME_FILE.pcap)
# nella variabile "pacchetti" avrò tutto il contenuto del file