# ## Aufgaben 

 - Prozesse 
 - #Speicher 

	 - Speicherverwaltung 

		 - Working #set 

			 - #Von einem #programm #wird working set erstellt #
			 - Einzelne #teile des programms #werden #ausgelagert 
			 - Quasi #: #Ungenutzte #routinen #bleiben #ungeladen 

		 - Paging #Daemon 

			 - Regelmäßig #kacheln #freiräumen 
			 - #Kacheln sind schon #frei , #dass nichts extra #ausgelaget #wird #wenn #es was #zu tun #gibt 

		 - #Gemeinsam #Verwendete seiten #

			 - Copy on write 

				 - #Fork kopiert #den #elternprozess 
				 - #Effizienter 

					 - #Nur #seitentabelle #kopieren 
					 - #Eltern und kindprozesse #verwenden #selbe seiten #
					 - #Alle seiten #sind read #only 
					 - Bei #schreibzugriff 

						 - #Schutzverletzung 

							 - #Interrupt 

					 - #Seite #wird #erst #bei #schreiboperationen #wirklich #kopiert 

 - #Dateisystem 

	 - #Datei 

		 - Dateiarten 

			 - #Programme 
			 - #Makros 
			 - Objektprogramme 
			 - #Binärprogramme #

				 - ausführbar #

			 - #auftragsprotokolldateien 
			 - #System #protokoll #dateien 
			 - #archivdatei #

		 - #Namensverwaltung #

			 - #hirarchisch 

				 - #Selber #name in #verschiedenen #Verzeichen #möglich #
				 - #Verzeichnisoperationen #möglich 
				 - #Dateibaum 

					 - #user #directories 
					 - #Verzeichnisse 

			 - Dateiverzeichniseintrag 

				 - #attribute 
				 - #Werte 

			 - #Dateiverzeichnis unabhängig 

				 - #verweis #auf #Verwaltungsstruktur 

			 - #links 

				 - #hardlinks #

					 - " #pointer " 
					 - kein #baum #mehr 

						 - #mögliche #Zyklen #
						 - #keine #hardlinks #auf verzeichnisse #

					 - #zähler #von #verweisen 

				 - symbolic #link 

					 - #verweis auf #pfad 

	 - Aufgaben #

		 - #einheitlicher #zugriff egal #wie #oder #wo gespeichert 
		 - #Organisieren #vom #Speicherplatz 
		 - #Logische #zugriffsoperationen 
		 - Schutzmechanismen 

	 - #Schichtenmodell 

		 - #Hardware 

			 - #Festplatte #

				 - #Einteilung in #Spuren->sektoren- #> blöcke 
				 - Langsame #zugrifsszeiten 

			 - #Solid #State #Drive #

				 - #Flash speicher 
				 - #schnelle #zugrifsszeiten 

		 - Controller #

			 - #zugriffsoperationen regeln 
			 - gezieltes Speichern #und #löschen 

	 - #Physikalisches #Dateisystem 

		 - #begriffe 

			 - #Datei 

				 - #menge #von #zusammengehörigen blöcken 

			 - #Block 

				 - zusammenhängender #speicherbereich 

			 - #Plattendateiverzeichnis 

				 - #inhaltsverzeichnis 

			 - #Dateideskriptor 

				 - Dateityp 
				 - #Position 
				 - #länge #

		 - aufgaben #

			 - #organisation #auf #externen #Datenträgern #
			 - #verwaltung #der #Dateien 
			 - #parallele #zum #Virtuellen speicher #

		 - #verwaltung #des #Dateisystems 

			 - #partitionen 

				 - #boot 
				 - super #
				 - #freespace 
				 - I - #Nodes 
				 - #root #

			 - #Probleme von caching 

				 - #möglicher #verlust von #Baumteilen 
				 - 

			 - Journaling 

				 - #log 

					 - #infos über #was #getan wurde 
					 - wird sofort #geschrieben 
					 - wiederherstellung 

				 - änderungen #von #Metadaten #persistent #machen 

			 - anforderungen an #ei #Modernes System #

				 - #große #partitionen 
				 - schnell #
				 - #sicher #vor crashes 

	 - Freier #Speicher 

		 - Listenmethode 

			 - verkettete #liste 

		 - #Index methode #

			 - #freie blöcke #werden indexiert #verwaltet 
			 - #baum #struktur 

				 - blatt #= index 
				 - #ast #= #weitere liste 

			 - #bitvektor 

				 - #fibt an #ob #belegt #oder #nicht 

		 - vektor #methode 

	 - Strategien #

		 - zusammenhängend 
		 - #Gestreut 

			 - #wenn #datei #zu #groß #, 
 weiteren #deskriptor #nutzen 

	 - Schutz 

		 - #Discretionary #Access Control 

			 - #Zugriffsrechte 

				 - read 
				 - #write 
				 - #exec #
				 - delete 

			 - #Benutzerkategorien 

				 - #System 
				 - #Subtopic 2 

			 - #Schutzmatrix , #
 wer #von #wem 
			 - #Benutzerverwaltung 
			 - #Anwendung 

				 - #unix #hat #das konzept #ohne #löschen 

		 - #Allgemeine #Zugriffsmatrix 

			 - #Nutzer in #reihen 
			 - #Dateien in #Spalten #
			 - #Wert #= #Zugriff 
			 - Nachteil #

				 - #viel speicher #

		 - acess control list 

			 - #Auflösen #der #Zugriffsmatrix in für #ein #Objekt #alle #Subjekte 
			 - #leere fallen #weg 
			 - #probleme 

				 - benutzerlöschen 

		 - #capability list 

			 - #Auflösen #der matrix pro #benutzer ( subjekte #) 
			 - #leere #rechte fallen #weg 
			 - #probleme 

				 - #benutzer hatte #mal #rechte , #aber #sie sind weg 
				 - #altesTicket #wird #genutzt 
				 - #löschen #einer #Datei 

		 - Mandatory acess #control 

			 - #Bell #Lapardula 

				 - #Subjekte und #Objekte #Klassifizieren 
				 - #Zugriffsrechte #von #System #entschieden 
				 - #Klassifikation 

					 - geheim 
					 - #vertraulich 
					 - #öffentlich #

			 - #Rollenbasiert 

				 - #Benutzern werden rollen #zugeordnet 
				 - #Rechte #aus #Kontext und #Rolle 
				 - #viel #administration #nötig 

			 - #probleme 

				 - #Komplex und #Unhändlich #
