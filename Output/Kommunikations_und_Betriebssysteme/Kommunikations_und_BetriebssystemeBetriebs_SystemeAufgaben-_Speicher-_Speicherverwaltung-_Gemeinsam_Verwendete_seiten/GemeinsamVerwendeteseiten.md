 #KommunikationsundBetriebssysteme #BetriebsSysteme #Aufgaben #Speicher #Speicherverwaltung #GemeinsamVerwendeteseiten- Copy on write
  - Fork kopiert den elternprozess
  - Effizienter
    - Nur seitentabelle kopieren
    - Eltern und kindprozesse verwenden selbe seiten
    - Alle seiten sind read only
    - Bei schreibzugriff
      - Schutzverletzung
        - Interrupt
    - Seite wird erst bei schreiboperationen wirklich kopiert 

   Tags & Topics:
   #Fork
   #Seite
   #Effizienter
   #Eltern
   #Schutzverletzung