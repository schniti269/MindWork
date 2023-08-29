⇒Gegenseitiger Ausschluss liegt vor.
Der Interrupt-Handler der Prozessverwaltung zum Prozessw echsel wird aufgerufen.
Da dieser ebenfalls mit enterMutex undexitMutex geklammert ist, bleibt er am Test&Set -
Befehl h¨angen.
Die Operation, die den gegenseitigen Ausschluss hergestel lt hat, kann nicht beendet werden!

   Tags & Topics:
   #Handler
   #Interrupt-Handler
   #Befehl