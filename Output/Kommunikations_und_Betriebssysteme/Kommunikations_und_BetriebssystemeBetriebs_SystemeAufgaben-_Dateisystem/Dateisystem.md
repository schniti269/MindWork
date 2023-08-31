 #KommunikationsundBetriebssysteme #BetriebsSysteme #Aufgaben #Dateisystem- Aufgaben
  - einheitlicher zugriff egal wie oder wo gespeichert
  - Organisieren vom Speicherplatz
  - Logische zugriffsoperationen
  - Schutzmechanismen
- Schichtenmodell
  - Hardware
    - Festplatte
      - Einteilung in Spuren->sektoren-> blöcke
      - Langsame zugrifsszeiten
    - Solid State Drive
      - Flash speicher
      - schnelle zugrifsszeiten
  - Controller
    - zugriffsoperationen regeln
    - gezieltes Speichern und löschen 
- Physikalisches Dateisystem
  - begriffe
    - Datei
      - menge von zusammengehörigen blöcken 
    - Block
      - zusammenhängender speicherbereich
    - Plattendateiverzeichnis
      - inhaltsverzeichnis
    - Dateideskriptor
      - Dateityp
      - Position
      - länge
  - aufgaben
    - organisation auf externen Datenträgern
    - verwaltung der Dateien
    - parallele zum Virtuellen speicher
  - verwaltung des Dateisystems
    - partitionen 
      - boot
      - super
      - freespace
      - I-Nodes
      - root
    - Probleme von caching
      - möglicher verlust von Baumteilen
    - Journaling
      - log 
        - infos über was getan wurde
        - wird sofort geschrieben
        - wiederherstellung
      - änderungen von Metadaten persistent machen
    - anforderungen an ei Modernes System
      - große partitionen
      - schnell
      - sicher vor crashes
- Freier Speicher
  - Listenmethode
    - verkettete liste
  - Index methode
    - freie blöcke werden indexiert verwaltet
    - baum struktur
      - blatt = index
      - ast = weitere liste
    - bitvektor
      - fibt an ob belegt oder nicht
  - vektor methode
- Strategien
  - zusammenhängend
  - Gestreut
    - wenn datei zu groß,

   Tags & Topics:
   #Block
   #Langsame
   #Organisieren
   #Aufgabe
   #Position
   #Dateien
   #Speicher
   #Plattendateiverzeichnis
   #Strategien
   #Listenmethode
   #INodes
   #Einteilung
   #Dateisystems
   #Flash
   #Schutzmechanismen