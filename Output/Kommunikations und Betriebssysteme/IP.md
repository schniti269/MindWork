# ## #IP 

 - #Ip #Adressen 

	 - #besondere #Adressen #

		 - #0.0.0.0 

			 - #dieser #Host #

		 - 0.0.Host 

			 - Unterknoten 1 

		 - #netz.255.255 

			 - Broadcast #adresse 

	 - NAT #protokoll #

		 - Private #Adressen #über eine Internetfähige #Adresse 
		 - #Internetfähiger #Router #übernimmt #zugriff 
		 - #Router #MAppt #Private #Adressen #auf #eine #Netzadresse 

	 - #Subnetting 

		 - #CIDR #

			 - #Notation 

				 - /24 #= 255.255.255.0 #
				 - #/"anzahl der #1er " 

			 - Routing tabelle 

				 - #IP #adresse #ist mit NEtzmaske #bereits #gespeichert 
				 - #ergebnis einer #gültigen " #rechnung #" sit mit #einem ausgangsinterface verknüpft 

			 - #verfahren 

				 - #Adresse #AND #subnetzmaske #
				 - #ergibt #netzadresse 

 - #IP #routing #

	 - Open Shortest #path first 

		 - #Benefits #

			 - #Schnelle #konvergenz #
			 - #Loop #frei #
			 - #VLSM und #CIDR subnetting 

		 - #Characteristics 

			 - #SPF alogrythmus #
			 - #Link #state #routing #

		 - Features 

			 - #Gruppenkonzept #zum #simplifizieren #
			 - #möglichkeit #BFD #Protokoll #zu #nutzen 

	 - #BGP ( #Border #Gateway Protocol #) #

		 - #Typ 

			 - Exterior #Gateway routing 
			 - #modifiziertes #distance #vector routing 

				 - " #behebt " #count to infinity #

		 - #Eigenschaften #

			 - #sehr #große #routing tabellen 
			 - #Manuelle #Regeln 

				 - #konfiguration #von routing #" #nogos #" #

		 - #Netze #werden #verschaltet #

	 - #ICMP ( #Internet #Control #Message #Protocol #) 

		 - #Internet #Control #Message #Protocol 
		 - #Nutzen 

			 - #Pings 
			 - #Fehler 
			 - Status 

		 - #Erkennen von #ICMP #Paketen 

			 - #wenn ein #Paket verloren #geht wird #nocht #reagiert 
			 - #der #Sender #" wartet " #bis etwas #ankommt 

				 - #mit #timeout 

	 - ARP #

		 - #Adress Resolution #Protokol #
		 - #Nutzen 

			 - #Aufschlüsseln #von #MAC #und #IP #i m #" heim"Netz 

		 - #ARP #Request #

			 - #Aufbau 

				 - #Frage 

					 - Who has " adresse " #
					 - #broadcast 

				 - Antwort 

					 - #der #Besitzer #der #adresse #Antwortet 

		 - #ARP #Erkennen #

			 - #Schicht 2 Header ( #Mac ) 

		 - #ARP Spoofing 

			 - der #falsche #antwortet #absichtlich #dass er die #Adresse #hat 
			 - #Interner #Angriff 

	 - #IPv6 

		 - #Aufbau 

			 - #Adressen #

				 - #Hexadezimal #ziffern #

					 - : : - > #00en #1x pro adressse #für #kürzung 

				 - 16 Byte gesamt 
				 - global unicast ( #GUA ) 
				 - #site local 

			 - #paket #

				 - #Class 

					 - #label #

				 - #header 
				 - #Destination 
				 - #source 

		 - #Header 

			 - #wurde möglichst #klein gehalten 
			 - #keine #TTL 

		 - Features #

			 - #jumbo pakete ( #4 #gb ) #
			 - kleinere #Routing tabellen 
			 - #mehr #sicherheit 
			 - QoS #
			 - #Anycast 

				 - #an #eine Gruppe 
				 - geringere #Netzlast #als #Broadcast 
				 - #Nachricht #wird #vom #schnellsten #geantwortet 

			 - #Multicast 

				 - #Gruppen #kommunikation 

			 - #Stateless #Adress #autoconfig ( slaac ) #

				 - #fe80 : : #MAC : 
				 - #test #auf neigbour #solicitation   #anstelle #von #ARP 
				 - #Anschließend #des #generieren #einer ( global #unicast #) 
