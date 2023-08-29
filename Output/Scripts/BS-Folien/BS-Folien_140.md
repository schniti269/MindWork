public static void enterMutex ( GlobalVariable busy ) {
boolean local;do {
local = SyncStatement.testAndSet ( busy );
} while ( local == true);
}

   Tags & Topics:
   