 #KommunikationsundBetriebssysteme #HardwareGrundlagen #vonNeumann- Bus
  - Datenbus
  - Adressbus
  - Steuerbus
- EA Geräte
  - Oft unabhängig von Prozessor
  - eigene Controller
  - Direct Memory Access
    - Auslesen und eingeben
    - ohne Mithilfe vom Prozessor
- Speicher
  - Hauptspeicher
    - Byte orientiert
    - Wort orientiert
    - Kapazität
      - KiB
        - 2^10
      - KB
        - 1000 Byte
  - Cache
    - Kaskadierend
      - L1
      - L2
      - L3
    - Koherenz
      - Write back
      - Write through
      - Snoopy
  - RAM
- Interruption
  - Ursachen
    - Synchron
      - Programmbezogen
        - Fehler
    - Asynchron
      - Systembezogeb
        - Hardware
  - Wirkung
    - Unterbrechung
    - Welcher code ?
      - interrupt Vektor aus Tabelle
    - Nach abarbeiten weitermachen As Usual
  - zulassen oder unterbinden
    - IRR
      - Anforderung
    - IER
      - Erlaubnis
    - Prioritäten Konzept
- Prozessor
  - Register
    - Mehrzweckhalle
    - Gleitpunkt
    - Steuer
      - Befehlszähler
      - Befehls Register
      - Kellerregister
    - Dopplung der Register
      - virtuelle Prozessorkerne
      - Wechsel zwischen den Registern
  - Rechenwerk
  - Steuerwerk
  - Prozessor Zustand 
    - Maschienenzustand
      - An 
      - Aus
      - Boot
    - Funktionszustand
      - Gültiger registersatz
    - Privilegien
      - Zugriffs schutzkonzept
        - Virtuelle Adressen
      - Usermode
        - Eingeschränkte Befehle
      - Privileged
        - Alle Befehle
- System Calls
  - benutzerprogramme aus Routinen
  - Fork
    - Erzeugen eines Kindprozesses
  - Wait Pid
    - Warten bis kindprozess beendet
  - Exit
    - Rausgehen
  - (Linux Kommandos)

   Tags & Topics:
   #Kellerregister
   #Wechsel
   #Fork
   #Kaskadierend
   #Erzeug
   #Write
   #Wort
   #Welcher
   #Usermode
   #Privilegien
   #Steuer
   #Kindprozess
   #Ursachen
   #Vektor
   #Ursache
   #Prozessorkerne
   #Programmbezog
   #Auslesen
   #Wirkung
   #Steuerbus
   #Funktionszustand
   #Warten
   #Writ
   #Controller
   #Mehrzweckhalle
   #Gleitpunkt
   #Erzeugen
   #Register
   #Privileged
   #warten
   #auslesen
   #Steuerwerk
   #Maschienenzustand
   #Fehler
   #Speicher
   #Unterbrechung
   #Programmbezogen
   #Hauptspeicher
   #Dopplung
   #Anforderung
   #Privileg
   #Systembezogeb
   #Zugriff
   #Adressbus
   #Koherenz
   #Befehl
   #Zugriffs
   #Interruption
   #Erlaubnis
   #Rausgehen