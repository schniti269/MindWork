    entry endWrite() {
activeWriter  = false;
// LESERPRIORITAET
if (readctr > 0)    reader.signal();
else    writer.signal();    }

   Tags & Topics:
   #activeWriter
   #endWrite
   #endwrite
   #activewriter