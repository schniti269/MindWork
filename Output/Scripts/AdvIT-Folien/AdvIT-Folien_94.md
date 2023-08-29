} //class MyThread1
Prof. Dr. Henning Pagnia (DHBW Mannheim) Advanced IT Herbst 2023 31/132Prozesse, Threads und Actors Nebenl¨auﬁgkeit
Threads in Java (2. Code-Beispiel)
public class MyThread2  implements  Runnable {  private int id;  public MyThread2(  int id ){      this.id = id;  }  public void run() {      try {  Thread.sleep(  (int) ( Math.random()  * 1000 ) );      } catch (Exception  e) {}      System.out.println(  ”Hello World (ID = ”+ id + ”)” );  } // run
  public static void main( String[] args ) {      for (int i=1; i<10; i++){  MyThread2  myRunnable  = new MyThread2(i);  Thread t = new Thread(myRunnable);  t.start();      }  } // main

   Tags & Topics:
   #Exception

[Previous: #AdvIT-Folien_95](AdvIT-Folien_95.md)

[Next: #AdvIT-Folien_95](AdvIT-Folien_95.md)