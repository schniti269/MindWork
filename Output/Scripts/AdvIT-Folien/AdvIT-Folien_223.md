public class LS {
private File f;
private int readcount  = 0;  // counting all readers
private Semaphore  mutex = new Semaphore  (1, true);
private Semaphore  w = new Semaphore  (1, true); // mutex for writers

   Tags & Topics:
   