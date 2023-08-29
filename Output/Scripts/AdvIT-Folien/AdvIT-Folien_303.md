    entry endWrite() {
activeWriter  = false;
// LESERPRIORITAET
if (readctr > 0)    reader.signal();
else    writer.signal();    }

   Tags & Topics:
   #activeWriter
   #endWrite
   #activewriter
   #endwrite

[Previous: #AdvIT-Folien_304](AdvIT-Folien_304.md)

[Next: #AdvIT-Folien_304](AdvIT-Folien_304.md)