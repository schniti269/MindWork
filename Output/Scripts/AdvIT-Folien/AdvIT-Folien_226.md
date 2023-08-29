readcount++;
if ( readcount  == 1 ) w.acquire();  // ﬁrst reader
mutex.release();
int byteCount  = f.read ( index, data );  // k.A.
mutex.acquire();

   Tags & Topics:
   

[Previous: #AdvIT-Folien_227](AdvIT-Folien_227.md)

[Next: #AdvIT-Folien_227](AdvIT-Folien_227.md)