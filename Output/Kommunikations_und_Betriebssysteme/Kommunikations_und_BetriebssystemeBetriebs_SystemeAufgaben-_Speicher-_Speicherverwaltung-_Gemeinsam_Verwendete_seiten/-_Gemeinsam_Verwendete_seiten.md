- Copy on write
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
   