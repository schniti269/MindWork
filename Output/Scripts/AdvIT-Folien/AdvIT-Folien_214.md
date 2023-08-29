private Semaphore  printer;
private Semaphore  mutex = new Semaphore  (1, true);
private boolean[] printerFree;
public Bmv (int anz) {
this.anz = anz;

   Tags & Topics:
   