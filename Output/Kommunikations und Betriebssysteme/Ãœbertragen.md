# ## #Übertragen 

 - pysical #Layer 

	 - Nyquist 
	 - #Übertragungsmedium 

		 - #Kabel 

			 - Coax 
			 - #Twisted #Pair 

		 - #Kabellos 

			 - #Bluetooth 
			 - #Wifi 

 - #Regelungen 

	 - #Protokolle 

		 - #Header 
		 - #Trailer 
		 - #Modelle 

			 - #OSI 

				 - 7 #Application #Layer 
				 - 6 #Darstellung 
				 - 5 #Session 
				 - 4 #Transport #Layer 
				 - 3 #Network #Layer 
				 - 2 #Datalink #Layer 
				 - 1 Pysical #Layer 

			 - #TCP #IP 

				 - #Anwendung 
				 - #Transport 
				 - #Internet 
				 - Netz 

			 - #Vorlesung 

				 - 5 #Application #Layer 
				 - 4 #Transport #Layer 
				 - 3 #Network #Layer 
				 - 2 #Datalink #Layer 
				 - 1 #Pysical #Layer 

	 - #Flow #control 

		 - #Datenstruktur 

			 - #Header 
			 - #payload 
			 - #Trailer 

		 - Sliding #window 

			 - #Empfangsfenser ändert sich #laufend 
			 - #Beschädigte #frames bleiden stehen #bis #sie korrigiert #wurden 
			 - #Puffer #beider seiten 
			 - Bestätigt #wird #immer #das #höchtse #element aus #dem gesamten #block 

		 - Schnittstellen 

			 - #Abholen 

				 - #Networklayer 
				 - #Ack ( #acknowledge ) 

			 - #Weitergeben 

				 - Physical #layer 
				 - Wait for #event 

		 - Sequenznummern 

			 - #Nummer des pakets 
			 - #Nummer #des #„trys“ 

		 - nummerierte pakete 

			 - #Nicht angekommene #werden #erneut angefordert 

		 - Go #back #n 
		 - Selective #repeat 

	 - #Netzwerkschicht 

		 - #Probleme 

			 - Eindeutige #Bezeichner 
			 - #Pakete #Weiterleiten 

		 - #Routing 

			 - #Welche #route ist i m #MOMENT die #beste 
			 - #Flooding 

				 - An Alle schicken 
				 - Alle leiten an alle #weiter 
				 - #Unendlich viele #Nachhrichten 

					 - Lösen #durch 

						 - #TTL 

							 - #Runterzählen #eines counters #für #jede #weiterleitung 
							 - #Bei 0 #wird #gelöscht 

						 - #Speichern was #bereits gesehn #wurde 

			 - #Minimaler #spannbaum 

				 - #Von #sich ausgehend #eien baum bilden #durch den #gesendet #wird 
				 - Dijkstra #algorythmus 

					 - Aller #erreichabren knoten gewichten 
					 - Jeder #bringt #nachricht näher an #das #zeil # 

			 - #DISTANCE #vector routing 

				 - #Jeder #veröffentlicht #regelmäßig seine Kosten #zum #erreichen 
				 - #Kleinste #kombination wird #genutzt 
				 - #Count to #infinity #problem 

					 - #Wenn ein eingegliederter Konten #ausfällt 
					 - #Gegenseitiges #hochzählen weil #gewichtungsprozess #nicht #vollständig #synchron 

			 - #Link #state #routing 

				 - Broadcastinfos in #Teilnetz 

					 - #Flooding 
					 - link #state #Paket 

						 - #Welche #Kosten 
						 - #Welche nachbarn 

				 - Spannbaum bilden 

					 - #Dijkstra 

				 - #Schnelle #Konvergenz 

			 - #Hirarchisches routing 

				 - Verfahren skalieren nicht mit #wachsender Größe #des #netzes 
				 - Routing tabellen sind #zu #groß 
				 - #Mehrstufiges routing 

					 - Unterteilen in #Regionen 
					 - Routen bis #zur #region 
					 - #Simplifizieren #der #Struktur 

	 - #Transportschicht 

		 - #ziel 

			 - einheitliche #dienste für #einheitliche #vorgänge 
			 - #anwendungen schnittstelle liefern 

				 - #System calls 

		 - #adressierung 

			 - #TSAP 

				 - #Transport #service #ACcess #Point 
				 - Kommunikation #zwischen #2 prozessen 
				 - #kommunikationsendpunkt #= #Socket 

					 - Socket #adtesse = ( Ip #adresse #, #port #nummer ) 

			 - #Unterknoten 2 

		 - #verbindungsorientiere #kommunikation 

			 - #CR : #Erster Versuch zum #verbindungsaufbau 
			 - #DR : #Disconnect #request 
			 - #Ack #: #bestätigung 
			 - #Data 
			 - was bei #fehlern : 

				 - Anforderung geht #verloren 

					 - nochmal senden 

				 - bestätigung ging #verloren 

					 - weitere verbindung #aufbauen #( unnötige last ) 

				 - eins #von #beidem wird #verzögert 

					 - in timeout #laufen #und erneut #aufbauen 

			 - #Sequenznummern 
 #Dreifacher #Handshake 

				 - immer #eindeutige sequenznummern #verwenden 
				 - #ISN : #Initiale #Sequenznummer 
				 - Beide nehmen seperate #zähler #für #ihre #nachrichten #x , #y 
				 - nicht #passsende werden #verworfen 

			 - #Verbindungsabbau 

				 - #problem #der #2 #Armeen 
 ( distributed #consensus ) 

					 - #kann #man wirklich #wissen #ob #die verbindung #abgebaut #werden #soll 
					 - wir wissen #von der letzten #nachricht #nicht ob sie #ankam 

				 - lösung per #Timeout 

					 - #server werden " ungeduldig " 
 #brechen #dann schneller #ab 
					 - #hosts #führen #relesase connection nach #fehlender antwort #durch 
					 - auch #nicht #optimalm , weil #problem unlösbar 

			 - #Flusskontrolle 

				 - #Ziel 

					 - #Speichersparsam #weil sliding window zu ville #puffer #bräuchte 

				 - #TPDUs 

					 - #segmente 

				 - #puffer 

					 - #nur noch #nicht bestätigte TPDUs werden #gepuffert 
					 - es #ist sinnvoll #große #puffer #zu haben für #schnelle #übertragung 
 #aber #wenigersinnvoll #für #speicher 
					 - #sobald #freigegeen #wird nachricht #aus #puffer entfernt 
					 - #sender weis #wie viele pufferplätze empfänger #hat , #wenn er #keine #merh hat #sendet er nicht #bis empfänger #verarbeitet #hat 
					 - #bestimmung #der #Größe 

						 - #c*r = #" übertragungsgeschwindigkeit " 
						 - #wie #viele können wir in #einer RTT senden 

		 - #TCP 

			 - #Transmissuin #Control #Protocolll 
			 - #TCP= #zuverlässige #end to #end #verbindung 
			 - #segmente 

				 - #TPDUs 
				 - #Fragmentierung wenn #zu #groß 

			 - #Sockets 

				 - streamorientiert #aus #sicht #der #anwendung 
				 - #socket #adresse 

					 - #ip #adresse 
					 - #port #nummer 

			 - #ablauf #einer #kommunikation 
			 - #TCP #Handshake 
			 - #Sillywindow #Syndrom 

				 - #wenn #puffer #voll #und #immer nur in #kleinen stücken #geleert 
				 - #viele pakete #senden #weil #immer #wieder etwas #frei #wird 
				 - #Eigener Puffer #i m #programm #implementieren 

					 - flush befehl 
 #sendet dann #den #eigenen #Puffer dann wieder #an #TCP #puffer #

 - #Anwendungsschicht 

	 - was 

		 - #verarbeitungsschicht #
		 - #Dienste #

	 - #DNS #

		 - #aufgabe 

			 - #auflösen IP #, #zu #Dienst #
			 - #Domains #auflösen #

		 - #Server 

			 - #verteilte #Datenbank 
			 - #leistet die #umsetzung 
			 - #kaskadierend #von Top level #Domain aus 

				 - rekursiv #

					 - #cache 

				 - #iterativ 

					 - #kein #cache #

		 - #CACHE 

			 - speichern #bereits aufgelöster #ung #benutzter #adressen #

	 - #WWW 

		 - #html 
		 - #hypermedia 
		 - #http #
		 - #Subtopic 4 #

	 - #Komprimierung #

		 - #Daten lassen sich #reduzieren #
		 - #nachteil 
		 - #Prinzipielle #Verfahren #
		 - #Entropie 

			 - Verlustfrei 
			 - #lauflängen #

				 - #AAAA - > #4A 

			 - #Statistisch 

				 - wörterbuch #der Codes #wird #mitgesendet #
				 - #huffman #

					 - #allg 
					 - #baum #

		 - #Quellkodierung #

			 - #Color #lookup #table 

				 - #wiederholende farben #werden #gespeichert #

			 - #differenzialkodierung 

				 - #nur differenzen #übertragen #bei #zb . #video #

			 - #Transformationskodierung #

				 - #DCT #
				 - #Fourier 

			 - #vectorquantisierung #

				 - zweidimensionaleBilder #werden in quadrate #gerastert 

			 - #Verlustbehaftet #
			 - #jpeg #

	 - #Datensicherheit #

		 - #Ziele #

			 - #Schutz #Vertraulicher #Daten #
			 - #Sicheres ermitteln verfasser #
			 - #Integrität #

		 - #Symetrisch 

			 - 
			 - #kennt #man #wirklich #den #sender ? 

		 - #Asymetrisch 

			 - #
			 - 2 #schlüssel #

		 - #Datenschutz unterschied #

			 - datenschutz #= #personenbezogen #

		 - #TSL #

			 - #Name , #Schlüssel = zertifikat 
			 - #nicht jeder #kann #zertifizieren #
			 - #Sitzung #

 - #Store #and #Forward #Prinzip #

	 - Einpacken #und #Versenden #
	 - #Puffern , Auspacken , auswerten , verschicken #

 - #Frame #

	 - #anfang #

		 - #DLE #STX #

	 - #Ende #

		 - #DLE #ETX #

	 - #Fehler #Korrektur #

		 - Crc #

	 - #Bit #stuffing 

		 - #Erkläten 

 - #Mac #Sublayer #

	 - #ALOHA #

		 - Timeout #wird #genutzt #
		 - #Kollisionen #

			 - #Poisson #verteilung #

				 - #T #Frame #Zufallsvariable 

					 - #Neu #eingetroffene #Frames #

				 - #Parameter #N #

					 - #Wahrscheinlichkeit #i m #Mittel #dass #gesendet #wird 

				 - #Parameter #G 

					 - > #= #N 
					 - #Zusätzlich also kollisionen 
					 - #Kanalbeslastung 
					 - #P0 #= #E^-2 #G 

				 - #Durchsatz #S #

					 - #G*p0 

	 - #CSMA #

		 - #Carrier #sense multiple #Access 
		 - 1 persistent 

			 - #Warten bis kanal fri 

				 - #Erst #hören #dann #senden 

		 - #Nicht persistent 

			 - #Wenn kanal #belegt #warte #zufällige #zeit 

		 - #P persistent #

			 - #Falls #slot #frei #sende #mit #wahrscheinlichkeit #p 

	 - #CSMA / #CD #

		 - #Carrier #sense multiple #access collision #detection 
		 - #Kanal #lauschen #  #bie #übertragung 
		 - #Beginen #sobald #kanal #frei #
		 - #Lausche #auch während #übertragung 
		 - Wenn kollision #brich #ab #und #warte #mit #wahrscheinlichkeit #p 

	 - #Bit #map #

		 - Reservierden 
		 - „Connection slots“ 

			 - #Konkurenzphase #

		 - 

	 - Binäre #countdown 

		 - #Station #bekommt #i #d 

			 - I #d = #> prio 

		 - #Eigene #ID #als #binärzahl senden in #konkurenzphase 
		 - #Kanal verknüft #oder schritt für #schritt 
		 - #I #d #die nicht #übereinstimmt #hört #nichtmehr #zu 
		 - #Einsatz i m canbus #

			 - #Steuergeräte i m #auto 

		 - Mok #und Ward 

			 - #Wenn #gesendet #hat #wird #prio #auf #0 #gesetzt 

	 - #Ethernet #

		 - #Frame #layout 

			 - #Preamble 
			 - #Frame #delimiter #
			 - #Destination #
			 - #Source #
			 - #Length of #data #
			 - #Padding 

				 - #Zufällg für #mindestlänge 

			 - #Checksum #crc 
			 - #Freitext 

		 - #Csma / cd 

			 - Binary exponential backoff 

				 - #Zufallszeit #warten nach #ersteer kollision 

					 - Nach 1 #kollision #jetzt oder i m nächsten #frame 
					 - Nach 2 #jetzt #oder #bis #zum #4ten 

				 - #Immer #verdoppeln nach weiterer #kollision 
				 - Nicht #mehr als #10 

		 - Fast #ethernet #

			 - #Mehr #datenrate 

		 - #Gigabit #ethernet #

			 - #Keine #kollisionserkennung 
			 - #Nur noch switches 
