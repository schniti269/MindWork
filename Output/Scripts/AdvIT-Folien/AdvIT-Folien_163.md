◮SWAP: die Inhalte zweier Speicherworte werden atomarvertauscht
Prof. Dr. Henning Pagnia (DHBW Mannheim) Advanced IT Herbst 2023 55/132Speicherbasierte Synchronisation Begriﬀe und Basismechanismen
Basismechanismen (Forts.)
Spin-Lock mittels TSL (Pseudocode)
public class MutualExclusionTSL  {  // Eintrittsprotokoll  public static void enterMutex  ( Integer busy) {  // busy should initially be set to 0    Integer local;    do       local = TSL (busy);    while ( local = = 1 );  }

   Tags & Topics:
   #Spin-Lock
   #Inhalt
   #Inhalte
   #Spin
   #Integer
   #Speicherworte
   #Speicherwort