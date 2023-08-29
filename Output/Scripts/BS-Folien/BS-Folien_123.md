Beispiel 2: P1 und P2 rufen gleichzeitig q.put(...)auf.
⋄Beide Prozesse ermitteln das letzte Element mit dem null-Ze iger.
⋄Beide Prozesse h ¨angen an dieses Element ihr neues Element an.
⋄Nur das zuletzt angeh ¨angte Element beﬁndet sich anschließend in der Warteschlang e.→Fehler!
⇒Die gef¨ahrlichen (kritischen) Codeabschnitte m ¨ussen unter gegenseitigem Ausschluss ausgef¨uhrt

   Tags & Topics:
   