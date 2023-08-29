public void append (String data){
try{
System.out.println(”Prod  arriving”);
empty.acquire();
mutex.acquire();

   Tags & Topics:
   