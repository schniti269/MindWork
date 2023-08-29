readcount++;
if ( readcount  == 1 ) w.acquire();  // ﬁrst reader
mutex.release();
int byteCount  = f.read ( index, data );  // k.A.
mutex.acquire();

   Tags & Topics:
   