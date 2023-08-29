w.release();
mutex2.acquire();
writecount  = writecount  - 1;
if ( writecount  = = 0 ) r.release();
mutex2.release();

   Tags & Topics:
   

[Previous: #AdvIT-Folien_246](AdvIT-Folien_246.md)

[Next: #AdvIT-Folien_246](AdvIT-Folien_246.md)