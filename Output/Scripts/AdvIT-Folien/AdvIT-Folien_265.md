public PrintJobManagement  ( int threadCount  ) {
waiting = new boolean[threadCount];
privsem = new Semaphore[threadCount];
ﬁles = new File[threadCount];
for ( int i=0 ; i < threadCount  ; i++ ) {

   Tags & Topics:
   