 #Kommunikations_und_Betriebssysteme #Kommunikations_Systeme #Übertragen #-_Mac_Sublayer- ALOHA
  - Timeout wird genutzt
  - Kollisionen
    - Poisson verteilung
      - T Frame Zufallsvariable
        - Neu eingetroffene Frames
      - Parameter N 
        - Wahrscheinlichkeit im Mittel dass gesendet wird
      - Parameter G
        - >= N
        - Zusätzlich also kollisionen
        - Kanalbeslastung
        - P0=E^-2G
      - Durchsatz S
        - G*p0
- CSMA
  - Carrier sense multiple Access
  - 1 persistent
    - Warten bis kanal fri
      - Erst hören dann senden
  - Nicht persistent
    - Wenn kanal belegt warte zufällige zeit
  - P persistent
    - Falls slot frei sende mit wahrscheinlichkeit p
- CSMA/CD
  - Carrier sense multiple access collision detection
  - Kanal lauschen  bie übertragung
  - Beginen sobald kanal frei
  - Lausche auch während übertragung
  - Wenn kollision brich ab und warte mit wahrscheinlichkeit p
- Bit map
  - Reservierden
  - „Connection slots“
    - Konkurenzphase
  - 
- Binäre countdown
  - Station bekommt id
    - Id => prio
  - Eigene ID als binärzahl senden in konkurenzphase
  - Kanal verknüft oder schritt für schritt 
  - Id die nicht übereinstimmt hört nichtmehr zu
  - Einsatz im canbus 
    - Steuergeräte im auto
  - Mok und Ward
    - Wenn gesendet hat wird prio auf 0 gesetzt
- Ethernet
  - Frame layout
    - Preamble
    - Frame delimiter
    - Destination
    - Source
    - Length of data
    - Padding
      - Zufällg für mindestlänge
    - Checksum crc
    - Freitext
  - Csma/cd
    - Binary exponential backoff
      - Zufallszeit warten nach ersteer kollision
        - Nach 1 kollision jetzt oder im nächsten frame
        - Nach 2 jetzt oder bis zum 4ten
      - Immer verdoppeln nach weiterer kollision
      - Nicht mehr als 10
  - Fast ethernet
    - Mehr datenrate
  - Gigabit ethernet
    - Keine kollisionserkennung 
    - Nur noch switches

   Tags & Topics:
   #Kollisionen
   #Frames
   #Konkurenzphas
   #padding
   #während
   #Station
   #Warten
   #übereinstimmt
   #Durchsatz
   #hör
   #gigabit
   #Kanalbeslastung
   #warten
   #Padding
   #Kollision
   #Kanal
   #Wahrscheinlichkeit
   #hören
   #Reservierde
   #E^-2
   #Gigabit
   #Lausch
   #Zufallszeit
   #Lausche
   #Konkurenzphase
   #Parameter
   #Begin
   #„Connection
   #Carrier
   #Frame
   #Beginen
   #Zufallsvariable
   #übertragung
   #Freitext
   #hört