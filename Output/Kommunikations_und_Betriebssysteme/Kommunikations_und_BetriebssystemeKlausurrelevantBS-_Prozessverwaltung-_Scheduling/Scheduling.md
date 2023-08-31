 #KommunikationsundBetriebssysteme #Klausurrelevant #BS #Prozessverwaltung #Scheduling- Prozessorganisiation
  - Dialog
    - Interaktiv
    - Ziel ist interaktives arbeiten
    - bevorzugt io
  - Stack
    - in Batches
    - Ziel ist auslastung
    - Bevorzugt prozesse die Ressourcen brauchen die gerade ungenutzt sind
  - Real time
    - Ziel einhaltung der Zeitgarantie
    - Bevorzugt Prozesse die knappe fristen haben
- Thread vs Prozess
  - Thread ist bestandteil von prozess
    - Thread hat immer einen kontrollfluss
- Timeline
  - Kurzzeit
    - Welcher prozess akut
    - Aufruf in kurzen abständen
  - Langzeit 
    - Swapping
      - Auftrag Sofort zu prozessoren
      - Überlast zustand -> zurückstellung in externen datentrger
    - Autragsverwaltung
      - Auftragswarteschlange
      - Je nach last
      - Überlast -> verdrängung
        - Swapspace auf Festplatte
- Kriterien
  - Zeit
    - Wartezeit
    - Umlaufzeit
    - Echtzeit
    - Antwortzeit
  - Leistung
    - Leistungsfähigkeit
    - Auslastung
    - Durchsatz
- Klassifikation
  - kooperativ
    - Keine gezielte kontrolle
    - Nur durch interrupts
  - Verdrängendes
    - Prozess wird verdrängt
- verfahren
  - First come first serve
    - Der der am längsten im rdy zustand ist ist an der reihe
    - Keine verdrängung
    - Leere anweisung-> NOP Schleife
  - Shortest processing time
    - Der der am schnellsten vorbei ist
    - CPU Burst
    - Shortest job first
    - Duchschnitt der zeit des Prozesses wird genommen
  - Shortest remaining time
    - Verdrängung
    - Wird ein prozess mit kürzerem burst bereit dann wird der aktuelle abgelöst
  - round robin
    - Time Sharing
    - Gleicher anteil alle nach einander
    - Zeitscheibe
      - Klein
        - Kaum fortschritt
      - Groß
        - Nicht responsive
  - Highest priority first
    - Nicht verdrängend
      - Bis selber freigeben
    - Verdrängend
      - Sobald ein höer priorisierter da ist wird der aktuelle abgelöst
    - Statisch
      - Bei erzeugung
      - Geschätzer burst
      - Geschätzer io
      - Geschätzter speicher
    - Dynamisch
      - Kann bei laufzeit geändert werden
      - Aktuellerburst
      - Aktueller io
      - Aktueller speicher
    - Starvaation
      - Aging gegenstrategie
  - Mehrstufen verfahren
    - Kombination aus mehreren
- Die ready warteschlange
  - Process management
    - Dispatcher
      - Intern verfügbar
    - Schnittstellen operationen
      - System calls
      - Interrupt handler
      - Timer Interrupt durch Prozessor selbst
        - Register selbst
  - Implementierung
    - Array mit prozessen
      - Konstruktor aufruf bei start
    - Running
      - Terminate macht inactive
    - Ready
      - Assign macht running
    - Inactive
      - initiate dann wird ready
    - Scheduler
      - Wählt aus
    - Store and load reg
      - Store
        - Werte werden gespeichert
      - load
        - Werde werden geladen
      - Das eigene Stack wird operiert
    - Test and set befehl
      - Atomare operation
      - Spinlock waiting

   Tags & Topics:
   #Ready
   #zurückstellung
   #Klassifikation
   #schleife
   #Sofort
   #Ziel
   #Proze�
   #Geschätzter
   #Kombination
   #verdr�ngung
   #Aufruf
   #Duchschnitt
   #Aktueller
   #leere
   #Starvaation
   #Dispatcher
   #Swapspace
   #Auslastung
   #Auftragswarteschlange
   #Echtzeit
   #Kurzzeit
   #Aktuellerburst
   #Kriterium
   #Groß
   #Zeitgarantie
   #Leere
   #Ressource
   #Schleife
   #Autragsverwaltung
   #Prozessorganisiation
   #Schnittstelle
   #Leistung
   #Abgelöst
   #Array
   #Wartezeit
   #Kann
   #Thread
   #Dialog
   #Burst
   #mehrstufen
   #Ressourcen
   #abgelöst
   #Auftrag
   #Geschätzer
   #Zeit
   #Register
   #Terminate
   #Kriterien
   #verdrängung
   #Langzeit
   #Leistungsfähigkeit
   #ge�ndert
   #Inactiv
   #Prozesses
   #Verdrängung
   #Statisch
   #Stack
   #Prozesse
   #Mehrstufen
   #Implementierung
   #Aging
   #Konstruktor
   #höer
   #Antwortzeit
   #Durchsatz
   #verdrängt