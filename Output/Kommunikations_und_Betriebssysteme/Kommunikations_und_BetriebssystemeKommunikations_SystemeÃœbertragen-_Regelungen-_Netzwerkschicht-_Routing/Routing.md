 #KommunikationsundBetriebssysteme #KommunikationsSysteme #Übertragen #Regelungen #Netzwerkschicht #Routing- Welche route ist im MOMENT die beste
- Flooding
  - An Alle schicken
  - Alle leiten an alle weiter
  - Unendlich viele Nachhrichten
    - Lösen durch
      - TTL
        - Runterzählen eines counters für jede weiterleitung
        - Bei 0 wird gelöscht
      - Speichern was bereits gesehn wurde
- Minimaler spannbaum
  - Von sich ausgehend eien baum bilden durch den gesendet wird
  - Dijkstra algorythmus
    - Aller erreichabren knoten gewichten
    - Jeder bringt nachricht näher an das zeil#
- DISTANCE vector routing
  - Jeder veröffentlicht regelmäßig seine Kosten zum erreichen 
  - Kleinste kombination wird genutzt
  - Count to infinity problem
    - Wenn ein eingegliederter Konten ausfällt
    - Gegenseitiges hochzählen weil gewichtungsprozess nicht vollständig synchron
- Link state routing
  - Broadcastinfos in Teilnetz
    - Flooding
    - link state Paket
      - Welche Kosten
      - Welche nachbarn
  - Spannbaum bilden
    - Dijkstra
  - Schnelle Konvergenz
- Hirarchisches routing
  - Verfahren skalieren nicht mit wachsender Größe des netzes
  - Routing tabellen sind zu groß
  - Mehrstufiges routing 
    - Unterteilen in Regionen
    - Routen bis zur region
    - Simplifizieren der Struktur 

   Tags & Topics:
   #Runterzhlen
   #Jeder
   #Verfahren
   #Mehrstufiges
   #gegenseitige
   #Flooding
   #Wenn
   #Speichern
   #Konten
   #Gegenseitiges
   #Routing
   #Konto
   #Kosten
   #Lsen
   #Paket
   #Konvergenz
   #Minimaler
   #Unterteile