 #Kommunikations_und_Betriebssysteme #Klausurrelevant #BS #-_Semaphore #-_Semaphor_Konzept- Definition
  - Up and down
    - Atomar durch mutex
  - Zähler 
    - Wie viele betriebsmittel sind da
    - Buchführung 
    - Positiv
      - Anzahhl der Verfügbaren
    - Negativ
      - Wie lang ist die warteschlange
  - Prozesswarteschlange
- Implementierung
  - Konstruktor 
    - FIFO warteschlange
    - Counter = übergabewert
  - P = down
    - Mutex
      - Counter —
      - Counter< 0
        - Block prozess
        - Assign
  - V=up
    - Mutex
      - Counter++
      - Counter <=0
        - Deblock
- Gegenseitiger ausschluss
  - Mutex
    - Mutex.p
    - Mutex.v
    - kritischer abschnitt
      - Enter mutex
      - Prozess
      - Exit mutex

   Tags & Topics:
   #Enter
   #Mutex
   #Counter
   #Assign
   #Verfügbaren
   #Buchführung
   #Prozess
   #Gegenseitiger
   #übergabewert
   #Mutex.p
   #Zähler
   #Definition
   #Implementierung
   #Konstruktor
   #�bergabewert
   #Prozesswarteschlange
   #Block