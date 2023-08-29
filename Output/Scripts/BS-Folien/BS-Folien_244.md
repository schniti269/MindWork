private Semaphore printer;
//Verwaltungsobjekt erzeugen, das n identische Drucker verw altet
public IdenticalPrinter1 ( int n ) {
printer = new Semaphore (n);
} //Konstruktor

   Tags & Topics:
   