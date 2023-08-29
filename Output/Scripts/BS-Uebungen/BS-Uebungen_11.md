schlange disk queue warten, bis sein Plattenauftrag ausgef ¨uhrt wurde.
Die Beendigung eines writeDisk -Auftrags wird von der Festplatte ¨uber eine Unterbrechung gemeldet, die von der Inter-
ruptroutine diskItrHdler (als erzwungener Prozeduraufruf) wie folgt behandelt wird:
Der zugeh ¨orige Prozess wird wieder in den ready-Zustand versetzt und der n ¨achste Plattenauftrag – sofern
vorhanden – an die Festplatte geschickt.

   Tags & Topics:
   #Plattenauftrag
   #-Auftrag

[Previous: #BS-Uebungen_12](BS-Uebungen_12.md)

[Next: #BS-Uebungen_12](BS-Uebungen_12.md)