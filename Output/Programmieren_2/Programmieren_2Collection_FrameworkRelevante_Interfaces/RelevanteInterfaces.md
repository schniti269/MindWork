 #Programmieren2 #CollectionFramework #RelevanteInterfaces- Comparable Interface
  - Methode
    - CompareTo();
    - vergleich
      - <0
        - vor
      - =0
        - Gleich
      - >0
        - hinter
  - Sinn
    - Vergleichsoperation muss implementiert 
sein um eine reihenfolge möglich zu machen
  - Sonst 
    - Class cast exception
  - Equals , compareTo, hashCode sollten sich konsistent verhalten
- eignene Comparator Klasse
  - implements Comparator<Typ>
  - methode
    - Compare
    - eigene Logik für eigenes Sortieren
    - Auch als Lambda funktion
  - Einsatz
    - set<> x = new Treeset<>(new *eigene sort klasse());
    - (geht auch mit Listen etc)

   Tags & Topics:
   #Vergleichsoperation
   #Comparator
   #Equal
   #Sortieren