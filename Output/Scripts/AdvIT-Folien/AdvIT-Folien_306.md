synchronized l¨asst sich auch f ¨ur einzelne Bl ¨ocke deﬁnieren
⇒un¨ubersichtlich, kann u.U. zu Deadlocks f ¨uhren!
es gibt keine Conditions (so wie bereits vorgestellt)
◮stattdessen besitzt jeder Monitor genau eine (namenlose) W arteschlange, an
der Threads warten k ¨onnen (und dabei die Monitorkontrolle aufgeben)

   Tags & Topics:
   #Condition