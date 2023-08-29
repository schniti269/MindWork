Betriebssysteme DHBW Mannheim ©Henning Pagnia Version 4.23 Fr¨uhjahr 2023 BS–95Prozessverwaltung Gegenseitiger Ausschluss Das Semaphor -Konzept
Prg. 13 Gegenseitiger Ausschluss mit einem Semaphorpublic class MutualExclusionSemaphore {
//mutex ist ein Semaphor, das von mehreren Prozessen verwende t werden kann
//f¨ur gegenseitigen Ausschluss wird es mit dem Wert 1 initialisi ert
static Semaphore mutex = new Semaphore (1);public static void main ( String[] args ) {

   Tags & Topics:
   #-Konzept