vorgeschlagen wurde.
Betriebssysteme DHBW Mannheim ©Henning Pagnia Version 4.23 Fr¨uhjahr 2023 BS–53Prozessverwaltung Gegenseitiger Ausschluss: Basismecha nismen Implementierung von Prozessen
Prg. 4 Dekkers Algorithmus in der Version von Peterson – Teil 1public class Dekker { // Mutual Exclusion f ¨ur zwei Prozesse mit IDs 0 und 1
private static boolean[] need = { false,false};
private static volatile int turn; // globale Var.public static void enterMutex ( int myProcessID ) {

   Tags & Topics:
   #Var.public
   #Dekkers
   #Exclusion
   #Algorithmus
   #Dekker
   #BS–53Prozessverwaltung