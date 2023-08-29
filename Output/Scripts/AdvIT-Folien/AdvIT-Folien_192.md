public BB1 (int size){
this.size = size;
buﬀer = new String[size];
empty = new Semaphore  (size, true);
}

   Tags & Topics:
   