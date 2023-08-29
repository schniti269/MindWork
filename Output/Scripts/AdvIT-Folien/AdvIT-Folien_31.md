zum Bearbeiten von Dateien und Filtern von Ein- und Ausgaben
Beispiele: echoAdvanced IT | awk ’ {print$2}’
awk ’{if (NR>1) {sum = sum+ $2; max++ }}END{print "avg =", sum/max }’ notenliste
*Buch¨uber die Shell-Programmierung inkl. sed und awk:
http://openbook.rheinwerk-verlag.de/shell_programmi erung/index.htm

   Tags & Topics:
   #Beispiel
   #END{print
   #Filter
   #Filtern