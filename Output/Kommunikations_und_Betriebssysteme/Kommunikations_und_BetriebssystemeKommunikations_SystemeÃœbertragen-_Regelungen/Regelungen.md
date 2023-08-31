 #KommunikationsundBetriebssysteme #KommunikationsSysteme #Übertragen #Regelungen- Protokolle
  - Header
  - Trailer
  - Modelle
    - OSI
      - 7 Application Layer
      - 6 Darstellung
      - 5 Session
      - 4 Transport Layer
      - 3 Network Layer
      - 2 Datalink Layer
      - 1 Pysical Layer
    - TCP IP
      - Anwendung
      - Transport
      - Internet
      - Netz
    - Vorlesung
      - 5 Application Layer
      - 4 Transport Layer
      - 3 Network Layer
      - 2 Datalink Layer
      - 1 Pysical Layer
- Flow control
  - Datenstruktur
    - Header
    - payload
    - Trailer
  - Sliding window
    - Empfangsfenser ändert sich laufend
    - Beschädigte frames bleiden stehen bis sie korrigiert wurden
    - Puffer beider seiten 
    - Bestätigt wird immer das höchtse element aus dem gesamten block
  - Schnittstellen
    - Abholen
      - Networklayer
      - Ack ( acknowledge)
    - Weitergeben
      - Physical layer
      - Wait for event
  - Sequenznummern
    - Nummer des pakets
    - Nummer des „trys“
  - nummerierte pakete
    - Nicht angekommene werden erneut angefordert
  - Go back n
  - Selective repeat
- Transportschicht
  - ziel
    - einheitliche dienste für einheitliche vorgänge
    - anwendungen schnittstelle liefern 
      - System calls
  - adressierung
    - TSAP
      - Transport service ACcess Point
      - Kommunikation zwischen 2 prozessen
      - kommunikationsendpunkt = Socket
        - Socket adtesse = ( Ip adresse, port nummer)
    - Unterknoten 2
  - verbindungsorientiere kommunikation
    - CR: Erster Versuch zum verbindungsaufbau
    - DR: Disconnect request
    - Ack: bestätigung
    - Data
    - was bei fehlern:
      - Anforderung geht verloren
        - nochmal senden
      - bestätigung ging verloren
        - weitere verbindung aufbauen ( unnötige last)
      - eins von beidem wird verzögert
        - in timeout laufen und erneut aufbauen
    - Sequenznummern 

   Tags & Topics:
   #socket
   #Vorlesung
   #Transport
   #Nicht
   #verzögert
   #Sequenznummer
   #Empfangsfenser
   #vorgänge
   #Bestätigt
   #Abholen
   #Puffer
   #Abhole
   #Schnittstelle
   #System
   #Unterknot
   #Weitergeben
   #Selective
   #Datenstruktur
   #höchtse
   #Darstellung
   #Nummer
   #session
   #Versuch
   #unnötige
   #Socket
   #Kommunikation
   #Unterknoten
   #Modelle
   #Modell
   #Session
   #Application
   #Internet
   #Anforderung
   #internet
   #Netz
   #Transportschicht