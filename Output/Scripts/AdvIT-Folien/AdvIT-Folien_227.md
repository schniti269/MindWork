readcount--;
if ( readcount  == 0 ) w.release();  // last reader
mutex.release();
return byteCount;
} // read

   Tags & Topics:
   