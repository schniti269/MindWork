Die Ausf¨uhrung vonloadRegister stellt den Prozesswechsel dar:
⋄Jeder Prozess besitzt seinen eigenen Stack.
⋄Beim Laden der Register wird der Stackpointer ¨uberschrieben.
⇒Der Stack des unterbrochenen Prozesses wird zum aktuellen Stack.
⇒Auf diesem Stack liegt die R ¨ucksprungadresse des assign-Aufrufs.

   Tags & Topics:
   #Stackpointer
   #Laden
   #assign-Aufruf