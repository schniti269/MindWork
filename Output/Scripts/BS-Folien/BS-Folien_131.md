int otherPID = 1 - myProcessID;need[myProcessID] = true; // Prozess will in den kA
turn = otherPID; // n¨achstes Mal darf der andere
while ( need[otherPID] && turn == otherPID ); // ggf. warten
} // enterMutexpublic static void exitMutex ( int myProcessID ) {
need[myProcessID] = false;

   Tags & Topics:
   #need[myProcessID
   #need[otherPID