printer = new Semaphore  (anz, true);
}
public void printFile (File f) {
try{
printer.acquire();

   Tags & Topics:
   