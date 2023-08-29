System.out.println(”Prod  active with ”+ data);
buﬀer[nextfree]  = data;
nextfree = (nextfree+1)  % size;
ctr++;
mutex.release();

   Tags & Topics:
   