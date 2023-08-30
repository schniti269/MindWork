 UI Implementierung
 Unterschiede und Gemeinsamkeiten zu AWT
  - Awt
    - Heavyweight
      - schnell
    - Fenster aus betriebssystem nehmen
    - Peer klassen werden gesteuert
    - Klasse selbst ist betriebssystem spezifisch
    - Rendering AUS BETRIEBSSYSTEM
  - SWING
    - lightweight
      - langsam
    - eigene Komponenten
    - mehr plattformunabhängigkeit
    - alle klassen fangen mit J an
    - Rendering AUS JAVA SELBST
  - Swing und AWT
    - Main Takeaway:
  Swing erbt aus AWT
  + eigene implementierung
  abstraktion über component 
  -> schachtelung
 Fenster
  - Container
  - Layout manager
 Listener Konzept
  - event
    - event source 
      - wirft evet objekte
        - auslösen
      - Es wird immer ein Event ausgelöst wenn etws getan wird
      - immer das objekt mit dem das event passiert
    - arten
      - Action 
      - item
        - selectieren
        - deselectieren
      - Focus event
  - listener
    - listener ist an bestimmten event regisstriert
    - ist interface mit welchen moethoden verabeitet wird

   Tags & Topics:
   