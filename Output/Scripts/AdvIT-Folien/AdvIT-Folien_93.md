Prof. Dr. Henning Pagnia (DHBW Mannheim) Advanced IT Herbst 2023 30/132Prozesse, Threads und Actors Nebenl¨auﬁgkeit
Threads in Java (Code-Beispiel)
public class MyThread1  extends Thread {  private int id;    // Thread ID  public MyThread1(  int id ){      this.id = id;  } // Konstruktor
  public void run() {      try {  Thread.sleep(  (int) ( Math.random()  * 1000 ) );      } catch (Exception  e) {}      System.out.println(  ”Hello World (ID = ”+ id + ”)” );  }  // run
  public static void main( String[] args ) {      for (int i=1; i<10; i++){  Thread t = new MyThread1(  i );  t.start();      }  } // main

   Tags & Topics:
   #Thread.sleep
   #Konstruktor
   #Exception

[Previous: #AdvIT-Folien_94](AdvIT-Folien_94.md)

[Next: #AdvIT-Folien_94](AdvIT-Folien_94.md)