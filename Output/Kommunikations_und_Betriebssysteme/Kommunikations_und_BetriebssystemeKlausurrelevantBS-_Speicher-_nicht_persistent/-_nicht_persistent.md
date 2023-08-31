 #Kommunikations_und_Betriebssysteme #Klausurrelevant #BS #-_Speicher #-_nicht_persistent- Speicher zuteilung zu Programmen
  - Einteilung in Bereiche
    - Hauptspeicher Kacheln
    - Pro programm in einem stück belegen
    - Arrays
      - Kopf mit information wie lang array ist
      - Elemente hintereinander 
    - Externe Fragmanetierung
      - Ablehnen
      - Defragmentieren /Basisregister zum verschieben
      - Swapspace nutzen
  - Overlay technik
    - Residenter Teil
      - Bleibende Teile
    - Overlay bereich
      - Austauschen
    - Benötigt schnellen Massenspeicher
    - Verwaltung
      - Core map -> belegung
      - Auftragssteuerung
    - Möglicherweise Interne + Externe Fragmentierung
  - Variable länge
    - linked list an freihen bereichen
    - Verschmelzen von frei gewordenen benachbarten bereichen
    - Einsatz im Heap
    - Strategien
      - First fit
        - Übrigen bereich wieder einketten
        - Bessere Fragmentierung
      - Best fit
        - Bereich mit wenigstem rest
        - Schlechtere Fragmentierung
      - Buddy 
        - Freier Speicher ist gegeben
        - Vergibt nur vielfaches von 2er potenzen
        - Eigene Liste für jede Größe (16,32..)
        - Fragmentierung ist intern
        - Wenn zu groß element aus enstprechender Liste wird halbiert
        - Man darf nur mit buddy verschmelzen
        - Buddy ist die andere Hälfte vom halbieren
        - Auf geschwindigkeit ausgelegt hat aber hohen speicherbedarf

   Tags & Topics:
   #Arrays
   #Fragmanetierung
   #Element
   #ablehnen
   #Teile
   #Kopf
   #kopf
   #/Basisregister
   #Liste
   #Vergibt
   #Bereich
   #Verschmelzen
   #länge
   #Swapspace
   #l�nge
   #Variable
   #Massenspeicher
   #Verwaltung
   #Elemente
   #Strategie
   #Austauschen
   #Strategien
   #Teil
   #Ablehnen
   #Verschmelz
   #Hälfte
   #Array