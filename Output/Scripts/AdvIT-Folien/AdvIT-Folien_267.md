public void print ( File f, int threadId ) {
mutex.acquire();  // Eintrittsprotokoll
if ( printerFree  ) { // Drucker reservieren
printerFree  = false;
privsem[threadId].release();  // nachher NICHT warten!

   Tags & Topics:
   #ThreadId].release
   #privsem[threadId].release

[Previous: #AdvIT-Folien_268](AdvIT-Folien_268.md)

[Next: #AdvIT-Folien_268](AdvIT-Folien_268.md)