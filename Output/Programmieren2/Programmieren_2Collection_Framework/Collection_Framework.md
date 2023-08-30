 Zuständig für
  - Dynamisches Speichern von Objekten
  - import java.util.x
  - Smmlung von Klassen
 Generics
  - Nutzen
    - <PLACEHOLDER>
      - Bei angebe wird es auf
  angegebenen Typ Konkretisiert
    - <>
      - Behandlung wie Object
  - Wrapperklasse
    - für alle elementaren Datentypen
    - datentyp in objekt kapselm
      - autoUnboxing
    - eigene Methoden
      - parse
 equals()
  - bei vergleich mit null muss false
  - reflexiv
  - symmetrisch
  - transitiv
  - konstistent
  - dierekte subklasse
    - alias check
      - this == o
    - test null
      - o== null
    - instanzen der gleichen klasse?
      - this.getClass() != o.getClass()
    - Feldvergleich
      - 
  - indierekte subklasse
    - alias check
    - delegation zur oberklassse
      - super.equals()
    - Feld Vergleich überprüft die Inhaltliche Gelichhetit der Subklasse
 hashCode()
  - surjektive funktion
  - bitverknüpung durch ^
    - bei long
    - (int)(field>>>32) ^(int)(field &0xFFFFFFFF
      - >>> bitshift
  - field==null ? 0: field.hashCode()
  - hash start
    - jede klasse anders
  - hash multiplyer
    - primzahl die den hash start multipliziert

   Tags & Topics:
   