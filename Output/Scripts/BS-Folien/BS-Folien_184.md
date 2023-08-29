⋄Beim Wert0wird eine Zeitscheibenunterbrechung (Timer Interrupt ) erzeugt.
Dieassign-Operation muss um das Laden des Zeitgeberregisters erg ¨anzt werden.
Prg. 11 zeigt den Timer-Interrupt-Handler als Schnittstellenoperation der PV.
Prg. 11 Implementierung des Timer-Interrupt-Handlerpublic void timerInterruptHandler () {
enterMutex();

   Tags & Topics:
   #Zeitscheibenunterbrechung
   #Handler
   #Handlerpublic
   #Zeitgeberregister
   #Dieassign
   #timerInterruptHandler
   #Zeitgeberregisters