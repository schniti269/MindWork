 #Programmieren_2 #Exkurse J Unit Tests
  - Assert
    - Does throw
    - Does Not throw
  - exeptions testen
    - test mit assertion
  - @Test Annotation
 Innere Klassen
  - Klassen Struktur
  - Top level
    - Statisch
    - Sichbarkeit kann modifiziert werden
  - element
    - nicht statisch
    - nur im Kontext eines Objekts der äußeren
  - lokal
    - nur innerhalb von methoden
  - anonym
    - ohne Bezeichner
    - referenz
    - #
 Labmda funktionen
  - Funktionales Interface einer Methode
  - zugriff auf umliegenden Kontext
 Fenster grössen
  - Virtueller bildschirm enthält alle bildschirme
  - Koordinaten
  - Default screen device.getDEFAULTconfigutation().getbounds
    - Getwitdth()
    - Get height()
  - Get displaymode
  - Graphics device 
    - Graphics enviroment,getlocalgraphicsenviroment
  - Virtual graphics env.getScreen []
 Serialisieren von objekten
  - Problem
    - manche datenstrukturen sind keine Reihen ( zb listen) sonder haben tiefe 
    - aufschreiben ist aber eine Reihe
  - Wo
    - Bäume
    - Graphen
  - Was
    - definierte reihenfolge
      - man wies wie man es geschrieben hat
      - das ganze wieder einlesen und dann objekt erzeugen
  - Beispiel
    - Personen objekt
      - name: klaus
      - alter: 27
    - csv variante
      - serialize();
        - person.file=
  klaus;27
  peter;46
  - wie 
    - serializable interface
      - java macht das automatisch
      - id sollte man final setzen
      - ein stream der schreibt 
      - ein stream der die objekte seriealisiert und den anderen stram bekommt
  - transien modifier
    - redundatnte daten ausschließen
    - persistentens nicht gefährdet

   Tags & Topics:
   #Sichbarkeit
   #Personen
   #Doe
   #Objekt
   #Beispiel
   #Serialisieren
   #Labmda
   #Statisch
   #Graphen
   #Default
   #Serialisier
   #Person
   #Objekts
   #Bäume
   #Annotation
   #Reihe