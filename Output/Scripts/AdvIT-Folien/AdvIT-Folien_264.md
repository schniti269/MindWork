private File[] ﬁles; // Verwaltung  der auszudruckenden  Dateien
private boolean[] waiting; // Verwaltung,  welche Threads warten
private Semaphore[]  privsem; // private Semaphore
private Semaphore  mutex = new Semaphore  (1, true); // wegen Verwaltungsdaten
private static ﬁnal int NOID = -1; // undeﬁnierte  Thread-ID

   Tags & Topics:
   #Verwaltung