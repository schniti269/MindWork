 Throwable
  interface
  - Exeption
    - Unchecked
      - Runtime
      - Automatische Weitergabe
      - Kann behandelt werden 
      - Oftmals logische Fehler
        - Oft of Bunds
        - DIV By 0
    - checked
      - Exception
      - Muss behandelt werden
      - Explizites auslösen
  - Error
    - Stack
      - Stack overflow
 Grundprinzip
  - Laufzeitfehler
    - Wird ausgelöst 
  - Fehlerbehandlung
    - Direkte Behandlung
    - Weitergabe
  “hot Potato“
  - Weitergabe
  - Nichtbezahlung-> Laufzeitfehler
 Exception klassen
  - Klasse extends Exception
  - Konstruktor ruft Superkonstruktor auf
    - InfoString
  - Möglichst früh Aufrufen
  - Throwable
    - Fehlertext
    - To String Objektinfos
    - Stracktrace
 Try with Recource
  - in die klammer hinter try kommt die ressource
  - benötight kein finally mehr 
  - bspw cloasable interface
  - Try With resource
    - Pro
      - Vermeiden von schachtelnden
    - Con
      - Aber andere reinholte

   Tags & Topics:
   