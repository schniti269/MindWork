public static void enterMutex ( GlobalVariable busy ) {
boolean local;do {
local = SyncStatement.testAndSet ( busy );
} while ( local == true);
}

   Tags & Topics:
   

[Previous: #BS-Folien_141](BS-Folien_141.md)

[Next: #BS-Folien_141](BS-Folien_141.md)