printer = new Semaphore  (anz, true);
}
public void printFile (File f) {
try{
printer.acquire();

   Tags & Topics:
   

[Previous: #AdvIT-Folien_212](AdvIT-Folien_212.md)

[Next: #AdvIT-Folien_212](AdvIT-Folien_212.md)