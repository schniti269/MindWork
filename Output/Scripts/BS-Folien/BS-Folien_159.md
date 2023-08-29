Prg. 9 Implementierung der Dispatcher-Operationen – Teil 2//Dispatcher-Operationen
private void initiate ( Context c ) {
Pcb process = inactiveQueue.get();process.initPcb ( c );process.state = Pcb.READY;readyQueue.put( process );
} // initiateprivate void terminate () {
runningProcess.state = Pcb.INACTIVE;inactiveQueue.put ( runningProcess );

   Tags & Topics:
   #2//Dispatcher
   #Dispatcher-Operation
   #INACTIVE;inactiveQueue.put
   #READY;readyQueue.put