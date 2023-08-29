Prg. 8 Implementierung der Dispatcher-Operationen – Teil 1public class ProcessManagement {
private Pcb[] processes;private Pcb runningProcess;private ProcessQueue readyQueue;private ProcessQueue inactiveQueue;private Scheduler s;public ProcessManagement ( int processCount ) {
processes = new Pcb[processCount];// Erzeugung eines geeigneten Scheduler-Objekts// Erzeugung der benoetigten Prozesswarteschlangen// Erzeugung der Prozesskontrollbloecke
} // Konstruktor
Betriebssysteme DHBW Mannheim ©Henning Pagnia Version 4.23 Fr¨uhjahr 2023 BS–66Prozessverwaltung Implementierung der Prozessverwaltun g Implementierung von Prozessen

   Tags & Topics:
   #Dispatcher-Operation
   #Prozessverwaltun
   #Scheduler-Objekt
   #Prozesskontrollbloecke
   #ProcessQueue
   #Objekts//
   #Pcb[processCount];//