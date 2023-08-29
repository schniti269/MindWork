monitor RW1mon {    boolean activeWriter  = false;    int readctr = 0;    Condition  reader = new Condition();    Condition  writer = new Condition();    entry startRead()  {
readctr++;
if (activeWriter)    reader.wait();
reader.signal();    }
    entry endRead()  {

   Tags & Topics:
   #activeWriter
   #activewriter