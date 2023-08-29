import java.util.concurrent.Semaphore;
public class MutexSem  {  static Semaphore  mutex = new Semaphore(  1, true ); // true => FIFO  static Runnable r = new Runnable()  {    public void run() {      while ( true ) {        try {          mutex.acquire();          // k.A. beginnt          System.out.println(  Thread.currentThread().getName()  + ” im k.A.”  );          Thread.sleep(3000);          // k.A. endet          mutex.release();        } catch ( InterruptedException  e ) {          e.printStackTrace();          Thread.currentThread().interrupt();          break;        } catch ( Exception  e ) {          e.printStackTrace();        }      } // while    } // run  }; // Runnable
  public static void main( String[] args ) {    new Thread( r ).start();    new Thread( r ).start();    new Thread( r ).start();  } // main
} // class
Prof. Dr. Henning Pagnia (DHBW Mannheim) Advanced IT Herbst 2023 63/132Speicherbasierte Synchronisation Semaphore

   Tags & Topics:
   #Thread.currentThread().getName
   #InterruptedException