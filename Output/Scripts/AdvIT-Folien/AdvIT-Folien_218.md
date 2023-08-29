mutex.release();
f.printOnPrinter(usePrinterNo);
mutex.acquire();
printerFree[usePrinterNo]  = true;
mutex.release();

   Tags & Topics:
   #f.printOnPrinter
   #f.printOnPrinter(usePrinterNo
   #printerfree[useprinterno

[Previous: #AdvIT-Folien_219](AdvIT-Folien_219.md)

[Next: #AdvIT-Folien_219](AdvIT-Folien_219.md)