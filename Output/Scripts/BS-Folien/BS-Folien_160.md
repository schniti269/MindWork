} // terminateprivate void block ( ProcessQueue q ) {
runningProcess.state = Pcb.BLOCKED;q.put ( runningProcess );
} // block
Betriebssysteme DHBW Mannheim ©Henning Pagnia Version 4.23 Fr¨uhjahr 2023 BS–67Prozessverwaltung Implementierung der Prozessverwaltun g Implementierung von Prozessen
Prg. 10 Implementierung der Dispatcher-Operationen – Teil 3private void deblock ( ProcessQueue q ) {

   Tags & Topics:
   #Prozessverwaltun
   #Dispatcher-Operation
   #ProcessQueue