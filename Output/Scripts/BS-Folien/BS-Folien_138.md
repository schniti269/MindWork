//busy bezeichnet die zur Synchronisation benutzte globale V ariable
public static boolean testAndSet ( GlobalVariable busy ) {
//Die folgenden beiden Anweisungen werden atomar durchgef¨uhrt:
boolean local = busy.value;busy.value = true;
return local;

   Tags & Topics:
   