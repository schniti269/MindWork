// ...// Prozess f¨ uhrt irgendwelche Aktionen aus;// ...// Prozess will kritischen Abschnitt betreten;mutex.p(); // Eintrittsprotokoll
// Prozess befindet sich im// kritischen Abschnitt;
mutex.v(); // Austrittsprotokoll
// ...// Prozess f¨ uhrt irgendwelche Aktionen aus;
}

   Tags & Topics:
   #Aktionen
   #Aktion