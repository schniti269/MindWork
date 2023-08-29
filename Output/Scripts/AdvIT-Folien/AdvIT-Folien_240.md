mutex3.acquire();
r.acquire();
mutex1.acquire();
readcount  = readcount  + 1;
if ( readcount  = = 1 ) w.acquire();

   Tags & Topics:
   