Adressformat (nach RFC 5952)Adressen werden in 8 Bl¨ocke zu je 16 Bit mittels Doppelpunkten unterteilt.Hexadezimale Schreibweise, wobei alle in einer Adresse vorkommendenBuchstaben (a,b,c,d,e,f) immer klein geschrieben werden.F¨uhrende Nullen werden weggelassen. Der erste Bereich mitaufeinanderfolgenden “0000“-Bl¨ocken ”wird als “::“ notiert.Beispiel: Die korrekte Schreibweise der Adresse2001:0db8:0000:0000:0001:0000:0000:0001lautet2001:db8::1:0:0:1
Prof. Dr. Henning Pagnia (DHBW Mannheim)Kommunikationssysteme©Fr¨uhjahr 2023138 / 188Network Layer IPv6
IPv6 (Forts.)
Broadcastf¨ur IPv6 nicht mehr deﬁniert, stattdessen Multicast oder Anycast)geringere Netzlast als Broadcasts.AnycastNachricht an eine Gruppe von Rechnern mit identischer IP-Adresse, diedenselben Dienst erbringen.Wird nur an den laut Routing-Tabelle am besten erreichbaren Rechnerzugestellt und nur dieser antwortet.Anycasts k¨onnen Broadcasts in vielen Anwendungsf¨allen ersetzen:z. B. bei DNS, in CDNs u. a.Vorteile: bessere Skalierbarkeit und Ausfallsicherheit.
Prof. Dr. Henning Pagnia (DHBW Mannheim)Kommunikationssysteme©Fr¨uhjahr 2023139 / 188Network Layer IPv6

   Tags & Topics:
   #mannheim)kommunikationssysteme
   #Multicast
   #Anycast)geringere
   #Netzlast
   #Adresse2001:0db8:0000:0000:0001:0000:0000:0001lautet2001
   #AnycastNachricht
   #Ausfallsicherheit

[Previous: #KS_IPv6_5](KS_IPv6_5.md)

[Next: #KS_IPv6_5](KS_IPv6_5.md)