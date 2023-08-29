public void print ( File f, int threadId ) {
mutex.acquire();  // Eintrittsprotokoll
if ( printerFree  ) { // Drucker reservieren
printerFree  = false;
privsem[threadId].release();  // nachher NICHT warten!

   Tags & Topics:
   #privsem[threadId].release
   #ThreadId].release