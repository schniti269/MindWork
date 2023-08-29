L¨osung des Ersten Leser-Schreiber-Problems
private  Semaphore  extra = new Semaphore  (1, true);
public  void write ( int index,  byte[] data ) {
extra.acquire();
w.acquire();

   Tags & Topics:
   #problem
   #Leser-Schreiber-Problem

[Previous: #AdvIT-Folien_234](AdvIT-Folien_234.md)

[Next: #AdvIT-Folien_234](AdvIT-Folien_234.md)