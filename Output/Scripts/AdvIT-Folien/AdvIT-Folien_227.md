readcount--;
if ( readcount  == 0 ) w.release();  // last reader
mutex.release();
return byteCount;
} // read

   Tags & Topics:
   

[Previous: #AdvIT-Folien_228](AdvIT-Folien_228.md)

[Next: #AdvIT-Folien_228](AdvIT-Folien_228.md)