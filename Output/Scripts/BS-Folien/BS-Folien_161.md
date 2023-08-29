Pcb process = q.get();process.state = Pcb.READY;readyQueue.put ( process );
} // deblockprivate void resign () {
runningProcess.state = Pcb.READY;readyQueue.put ( runningProcess );
} // resignprivate void assign () {
Pcb process = s.schedule ();process.state = Pcb.RUNNING;runningProcess.storeRegister();runningProcess = process;runningProcess.loadRegister();

   Tags & Topics:
   #READY;readyQueue.put

[Previous: #BS-Folien_162](BS-Folien_162.md)

[Next: #BS-Folien_162](BS-Folien_162.md)