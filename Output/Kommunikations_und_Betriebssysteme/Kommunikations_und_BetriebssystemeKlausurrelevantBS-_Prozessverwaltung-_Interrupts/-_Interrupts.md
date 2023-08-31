 #Kommunikations_und_Betriebssysteme #Klausurrelevant #BS #-_Prozessverwaltung #-_Interrupts- E/A  Operationen
  - Rahmen bedingungen:
    - Geschwindigkeitsunterschiede
    - Parallelarbeit von CPU und E/A
  - Synchrone schnittstelle
    - Eigener System call
    - E/A Gerät  arbeitet für sich parallel
    - Gerät erzeugt interrupt
    - E/A interrupt handler
    - Timer interrupt handler
      - Resign
      - Assign
    - Eigene Blockiert warteschlange pro gerät
    - Recap: Prozess bleibt nicht im kontrollfluss
  - Asynchrone E/A Schnittstelle
    - System calls
      - Iostart
        - Anstoßen der E/A
      - Io wait
        - Warten bis daten vorliegen
    - Gerät schickt interrupts
    - E/A interrupt handler
      - Notieren 
        - Wenn io wiat noch nicht war
      - Blockieren
        - Wenn io wait läuft
    - Wenn noch nicht abgearbeitet
      - Timer innterrupt handler
    - Recap: Prozess der wartet bleibt im kontrollfluss
    - nebenläufige Abläufe

   Tags & Topics:
   #Warten
   #Iostart
   #Blockieren
   #Synchrone
   #Geschwindigkeitsunterschiede
   #Notieren
   #warten
   #Schnittstelle
   #Abläufe
   #Notier
   #Timer
   #recap
   #Operation
   #Operationen
   #Assign
   #Parallelarbeit
   #Recap
   #Rahmen
   #blockieren