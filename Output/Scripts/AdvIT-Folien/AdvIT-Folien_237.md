private  int writecount  = 0;
private  Semaphore  mutex1  = new Semaphore  (1, true);
private  Semaphore  mutex2  = new Semaphore  (1, true);
private  Semaphore  mutex3  = new Semaphore  (1, true);
private  Semaphore  w = new Semaphore  (1, true);

   Tags & Topics:
   