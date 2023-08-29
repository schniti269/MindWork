Betriebssysteme DHBW Mannheim ©Henning Pagnia Version 4.23 Fr¨uhjahr 2023 BS–102Prozessverwaltung Beispiel: Betriebsmittelverwaltung D as Semaphor-Konzept
Prg. 17 Druckerverwaltung – Teil 2//Ausgabe einer Datei auf einem der Drucker
public void print ( File f ) {
printer.p(); // einen Drucker belegen
mutex.p();

   Tags & Topics:
   #BS–102Prozessverwaltung
   #Druckerverwaltung