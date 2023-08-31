 #KommunikationsundBetriebssysteme #KommunikationsSysteme #IP #IProuting- Open Shortest path first
  - Benefits
    - Schnelle konvergenz
    - Loop frei
    - VLSM und CIDR subnetting
  - Characteristics
    - SPF alogrythmus
    - Link state routing
  - Features
    - Gruppenkonzept zum simplifizieren
    - möglichkeit BFD Protokoll zu nutzen
- BGP ( Border Gateway Protocol)
  - Typ
    - Exterior Gateway routing
    - modifiziertes distance vector routing
      - "behebt" count to infinity
  - Eigenschaften
    - sehr große routing tabellen
    - Manuelle Regeln
      - konfiguration von routing "nogos"
  - Netze werden verschaltet
- ICMP ( Internet Control Message Protocol)
  - Internet Control Message Protocol
  - Nutzen
    - Pings
    - Fehler
    - Status
  - Erkennen von ICMP Paketen
    - wenn ein Paket verloren geht wird nocht reagiert
    - der Sender "wartet" bis etwas ankommt
      - mit timeout
- ARP
  - Adress Resolution Protokol
  - Nutzen
    - Aufschlüsseln von MAC und IP im "heim"Netz
  - ARP Request
    - Aufbau
      - Frage
        - Who has "adresse"
        - broadcast
      - Antwort
        - der Besitzer der adresse Antwortet
  - ARP Erkennen
    - Schicht 2 Header ( Mac)
  - ARP Spoofing
    - der falsche antwortet absichtlich dass er die Adresse hat
    - Interner Angriff
- IPv6
  - Aufbau
    - Adressen
      - Hexadezimal ziffern
        - :: -> 00en 1x pro adressse für kürzung
      - 16 Byte gesamt
      - global unicast ( GUA)
      - site local
    - paket
      - Class
        - label
      - header
      - Destination
      - source 
  - Header
    - wurde möglichst klein gehalten 
    - keine TTL
  - Features
    - jumbo pakete ( 4gb)
    - kleinere Routing tabellen
    - mehr sicherheit
    - QoS
    - Anycast
      - an eine Gruppe 
      - geringere Netzlast als Broadcast
      - Nachricht wird vom schnellsten geantwortet
    - Multicast
      - Gruppen kommunikation
    - Stateless Adress autoconfig (slaac)
      - fe80:: MAC:
      - test auf neigbour solicitation  anstelle von ARP
      - Anschließend des generieren einer (global unicast)

   Tags & Topics:
   #Protokoll
   #Netze
   #Manuelle
   #Erkennen
   #Border
   #Aufbau
   #Byte
   #Antwort
   #Ope
   #VLSM
   #Besitzer
   #Destination
   #Gruppenkonzept
   #Anycast
   #Schicht
   #Fehler
   #Paketen
   #Sender
   #Nachricht
   #Frage