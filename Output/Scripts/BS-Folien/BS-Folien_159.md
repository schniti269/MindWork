Prg. 9 Implementierung der Dispatcher-Operationen – Teil 2//Dispatcher-Operationen
private void initiate ( Context c ) {
Pcb process = inactiveQueue.get();process.initPcb ( c );process.state = Pcb.READY;readyQueue.put( process );
} // initiateprivate void terminate () {
runningProcess.state = Pcb.INACTIVE;inactiveQueue.put ( runningProcess );

   Tags & Topics:
   #2//Dispatcher
   #READY;readyQueue.put
   #INACTIVE;inactiveQueue.put
   #Dispatcher-Operation

[Previous: #BS-Folien_16](BS-Folien_16.md)

[Next: #BS-Folien_16](BS-Folien_16.md)