//Konstantendeﬁnitionen f ¨ur Prozesszust ¨ande
public static final int INACTIVE = 1;public static final int READY = 2;public static final int RUNNING = 3;public static final int BLOCKED = 4;int state = INACTIVE;// Sicherungsbereich fuer Register// weitere Attribute eines Prozessespublic abstract void storeRegister (); // Sichern der Register
public abstract void loadRegister (); // Zur¨uckladen der Register
public abstract void initPcb ( Context c ); // Initialisierung des PCBs
} // Pcb

   Tags & Topics:
   #Zur¨uckladen
   #PCB
   #initPcb
   #Zur¨ucklade
   #Initialisierung
   #pcb
   #Prozesszust
   #Attribute
   #Register//
   #Attribut
   #Context

[Previous: #BS-Folien_104](BS-Folien_104.md)

[Next: #BS-Folien_104](BS-Folien_104.md)