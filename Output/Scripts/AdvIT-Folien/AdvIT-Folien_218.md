mutex.release();
f.printOnPrinter(usePrinterNo);
mutex.acquire();
printerFree[usePrinterNo]  = true;
mutex.release();

   Tags & Topics:
   #f.printOnPrinter(usePrinterNo
   #f.printOnPrinter
   #printerfree[useprinterno