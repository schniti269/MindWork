//Konstantendeﬁnitionen f ¨ur Prozesszust ¨ande
public static final int INACTIVE = 1;public static final int READY = 2;public static final int RUNNING = 3;public static final int BLOCKED = 4;int state = INACTIVE;// Sicherungsbereich fuer Register// weitere Attribute eines Prozessespublic abstract void storeRegister (); // Sichern der Register
public abstract void loadRegister (); // Zur¨uckladen der Register
public abstract void initPcb ( Context c ); // Initialisierung des PCBs
} // Pcb

   Tags & Topics:
   #Attribute
   #Attribut
   #pcb
   #Initialisierung
   #Zur¨ucklade
   #Prozesszust
   #PCB
   #Register//
   #initPcb
   #Zur¨uckladen
   #Context