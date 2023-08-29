private int nextfree = 0;
private int nextfull = 0;
private Semaphore  mutex = new Semaphore(  1, true );
private Semaphore  full = new Semaphore  (0, true);
private Semaphore  empty;

   Tags & Topics:
   

[Previous: #AdvIT-Folien_192](AdvIT-Folien_192.md)

[Next: #AdvIT-Folien_192](AdvIT-Folien_192.md)