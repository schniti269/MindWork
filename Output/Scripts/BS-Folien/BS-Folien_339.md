Betriebssysteme DHBW Mannheim ©Henning Pagnia Version 4.23 Fr¨uhjahr 2023 BS–135Speicherverwaltung Auslagerungsstrategien Speicherver waltung virtueller Systeme
Least Recently Used ( LRU)
•Lagere die Seite aus, auf die am l ¨angsten nicht mehr zugegriﬀen wurde.
Implementierung mittels Hardware-m ¨aßig zu setzenden Referenz-Bits (Reference Bit ):
if (Kachelzugriﬀ ) referenzbit := 1;

   Tags & Topics:
   #BS–135Speicherverwaltung
   #bs–135speicherverwaltung
   #Referenz