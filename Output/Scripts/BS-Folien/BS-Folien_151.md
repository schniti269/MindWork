⇒Gegenseitiger Ausschluss liegt vor.
Der Interrupt-Handler der Prozessverwaltung zum Prozessw echsel wird aufgerufen.
Da dieser ebenfalls mit enterMutex undexitMutex geklammert ist, bleibt er am Test&Set -
Befehl h¨angen.
Die Operation, die den gegenseitigen Ausschluss hergestel lt hat, kann nicht beendet werden!

   Tags & Topics:
   #Interrupt-Handler
   #Befehl
   #Handler

[Previous: #BS-Folien_152](BS-Folien_152.md)

[Next: #BS-Folien_152](BS-Folien_152.md)