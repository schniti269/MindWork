IPv6 (Forts.)
Aufbau von IPv6-AdressenGlobal Routing Preﬁx (48 Bit)Subnet (16 Bit)Host (64 Bit)Adresstypen mit Pr¨aﬁxen (nach RFC 4291)Global Unicast Address (GUA):2000::/3Internet-weit g¨ultige, eindeutige Adresse.Site Local Address:fc00::/7Private Addresse, die nicht im Internet gerouted wird.Link Local Address:fe80::/10Tempor¨are Adresse, nur im LAN g¨ultig (f¨ur SLAAC beimStart-Up).Multicast Address:ff00::/8F¨ur die Gruppenkommunikation: Nachricht an eine Gruppe vonNetzwerkknoten.Anycast Address:2000::/3Pr¨aﬁx wie GUA, aber identische Adresse f¨ur mehrere Ger¨ate.Prof. Dr. Henning Pagnia (DHBW Mannheim)Kommunikationssysteme©Fr¨uhjahr 2023140 / 188Network Layer IPv6
IPv6 (Forts.)
Stateless Address Autoconﬁguration (SLAAC)Host w¨ahlt eigenst¨andig eine Link Local Address (nur im LAN g¨ultig):Aufbau der Adresse i. A. aus festem Pr¨aﬁx (fe80:) und MAC-Ger¨ateadresse.Test auf Eindeutigkeit mittelsNeighbor SolicitationNachricht (anstelle vonARP).Anschließend ggf. Generieren einer GUA f¨ur Verbindungen ins Internet (mitHilfe des Routers).)DHCP und NAT somit nicht mehr notwendig.
Prof. Dr. Henning Pagnia (DHBW Mannheim)Kommunikationssysteme©Fr¨uhjahr 2023141 / 188

   Tags & Topics:
   #Ger¨at
   #Adresstype
   #Routers).)DHCP
   #Addres
   #MAC-Ger¨ateadresse
   #site
   #mitHilfe
   #AdressenGlobal
   #SolicitationNachricht
   #bit)subnet
   #mannheim)kommunikationssysteme
   #gua):2000::/3internet
   #beimstart
   #up).multicast
   #GUA):2000::/3Internet-weit
   #Addresse
   #Site
   #fe80::/10Tempor¨are
   #Ger¨ate