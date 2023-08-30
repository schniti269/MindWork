(nr)
 != Util Streams
  - Stream= übertragung von daten von quelle in zeil
  - unterschied
    - io hat xterne ressource
      - datei
      - netzs
      - datenbank
    - Util
      - Datenquellen
        - map
        - reduce
        - filter
      - funktionale prog
      - von collection -> zu collection
        - zwischendrin filtern
 arten
  - buffered 
  - unbuffered
 Schreiben und lesen Datei
  (klausurrelavant weil Exception handling)
  - Writer
    - .write
      - möchte string
      - schreibt alles hintereinader weg
        - \n
        - lineseperator
    - mögliche fehler
      - Schreiben
      - lesen
      - sonstige
    - blockiert solange datei wie wir sie benutzen
  - Reader
    - File reader
      - mögliche fhler
        - io exception
      - Cloasable interface für try with ressource
        - damit man das verschachtelte finally nicht notwendig tist
      - Schleife zum lesen

   Tags & Topics:
   