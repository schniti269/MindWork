readctr--;
if (readctr == 0)    writer.signal();    }
    entry startWrite() {
if (readctr > 0 || activeWriter)    writer.wait();
activeWriter  = true;    }

   Tags & Topics:
   #startWrit
   #startwrite
   #activeWriter
   #activewriter