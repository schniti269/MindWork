readctr--;
if (readctr == 0)    writer.signal();    }
    entry startWrite() {
if (readctr > 0 || activeWriter)    writer.wait();
activeWriter  = true;    }

   Tags & Topics:
   #startWrit
   #activeWriter
   #activewriter
   #startwrite

[Previous: #AdvIT-Folien_303](AdvIT-Folien_303.md)

[Next: #AdvIT-Folien_303](AdvIT-Folien_303.md)