Betriebssysteme DHBW Mannheim ©Henning Pagnia Version 4.23 Fr¨uhjahr 2023 BS–93Prozessverwaltung Semaphor-Deﬁnition Das Semaphor-Konzept
Prg. 12 Eine Semaphor-Implementierungpublic class Semaphore { // als Schnittstellenoperation de r PV
private int ctr;private ProcessQueue q; // FIFOpublic Semaphore ( int initValue ) {
ctr = initValue;q = new (ProcessQueue);
}public void p () { public void v () {

   Tags & Topics:
   #ProcessQueue
   #Semaphor-Konzept

[Previous: #BS-Folien_231](BS-Folien_231.md)

[Next: #BS-Folien_231](BS-Folien_231.md)