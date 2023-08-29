# ## #BS 

 - Semaphore #

	 - #Semaphor #Konzept 

		 - #Synchronisierung #

			 - #Innerhalb 
			 - #Außerhalb 
			 - #Syncro 

				 - multithreading 

					 - #Race #cnditions #vermeiden 

						 - #Syncro #

							 - #schlecht 

								 - Busywaiting #

							 - #Gut 

								 - #Dekker 

									 - #Atomare #speicheroperationen+ #

							 - #Besser 

								 - #Eigener #prozessorbefehl 

									 - #Spin #lock #warteschliefe 
									 - Test and set befehl #

		 - #Definition 

			 - #Up and down 

				 - #Atomar #durch #mutex 

			 - #Zähler #

				 - Wie #viele #betriebsmittel #sind #da 
				 - #Buchführung 
				 - #Positiv 

					 - #Anzahhl #der #Verfügbaren #

				 - #Negativ #

					 - #Wie #lang ist #die #warteschlange #

			 - #Prozesswarteschlange 

		 - #Implementierung 

			 - #Konstruktor 

				 - FIFO #warteschlange #
				 - #Counter = #übergabewert #

			 - #P #= down #

				 - #Mutex 

					 - #Counter #� � 
					 - #Counter < #0 

						 - #Block #prozess 
						 - #Assign 

			 - #V #= up 

				 - #Mutex 

					 - #Counter++ #
					 - #Counter #< = 0 #

						 - #Deblock 

		 - #Gegenseitiger ausschluss #

			 - #Mutex 

				 - Mutex.p 
				 - Mutex.v 
				 - #kritischer #abschnitt 

					 - #Enter #mutex #
					 - #Prozess 
					 - #Exit #mutex #

 - #Prozessverwaltung 

	 - #Interrupts 

		 - #E / #A   #Operationen 

			 - #Rahmen #bedingungen #: 

				 - Geschwindigkeitsunterschiede 
				 - #Parallelarbeit #von #CPU und #E #/ #A 

			 - #Synchrone #schnittstelle 

				 - #Eigener #System call 
				 - #E #/ A #Gerät   #arbeitet #für sich parallel 
				 - #Gerät erzeugt interrupt 
				 - #E #/ A interrupt #handler 
				 - #Timer interrupt #handler #

					 - Resign 
					 - Assign #

				 - #Eigene #Blockiert #warteschlange pro #gerät #
				 - #Recap #: Prozess bleibt #nicht #i m #kontrollfluss 

			 - #Asynchrone #E #/ #A #Schnittstelle #

				 - #System calls #

					 - #Iostart 

						 - #Anstoßen #der E #/ #A 

					 - #Io wait 

						 - #Warten #bis daten #vorliegen 

				 - #Gerät #schickt #interrupts 
				 - #E #/ #A interrupt #handler 

					 - #Notieren 

						 - #Wenn #io wiat #noch nicht #war 

					 - #Blockieren 

						 - #Wenn #io wait #läuft 

				 - Wenn noch #nicht #abgearbeitet 

					 - #Timer #innterrupt #handler #

				 - #Recap #: Prozess #der #wartet #bleibt i m #kontrollfluss 
				 - #nebenläufige Abläufe #

	 - #Scheduling 

		 - #Prozessorganisiation 

			 - #Dialog 

				 - #Interaktiv 
				 - #Ziel ist #interaktives arbeiten 
				 - bevorzugt #io #

			 - #Stack 

				 - in #Batches 
				 - Ziel #ist #auslastung #
				 - #Bevorzugt #prozesse #die #Ressourcen brauchen #die #gerade ungenutzt #sind 

			 - Real #time 

				 - #Ziel #einhaltung #der #Zeitgarantie #
				 - #Bevorzugt #Prozesse #die #knappe #fristen #haben 

		 - #Thread vs #Prozess 

			 - #Thread #ist #bestandteil #von prozess 

				 - #Thread #hat immer einen #kontrollfluss 

		 - #Timeline 

			 - #Kurzzeit 

				 - Welcher prozess #akut 
				 - #Aufruf in #kurzen #abständen #

			 - Langzeit 

				 - #Swapping 

					 - #Auftrag #Sofort #zu #prozessoren 
					 - Überlast #zustand - #> #zurückstellung in #externen #datentrger 

				 - #Autragsverwaltung 

					 - #Auftragswarteschlange 
					 - #Je #nach last 
					 - #Überlast - #> #verdrängung 

						 - #Swapspace #auf #Festplatte #

		 - #Kriterien #

			 - #Zeit #

				 - #Wartezeit #
				 - #Umlaufzeit #
				 - #Echtzeit #
				 - #Antwortzeit 

			 - #Leistung 

				 - #Leistungsfähigkeit 
				 - #Auslastung 
				 - #Durchsatz 

		 - #Klassifikation 

			 - #kooperativ 

				 - #Keine #gezielte #kontrolle 
				 - #Nur #durch #interrupts 

			 - #Verdrängendes 

				 - Prozess wird #verdrängt #

		 - #verfahren 

			 - #First come first serve #

				 - #Der #der am #längsten #i m rdy #zustand #ist ist an #der #reihe 
				 - #Keine #verdrängung 
				 - #Leere anweisung- #> #NOP #Schleife 

			 - Shortest #processing #time 

				 - #Der #der am schnellsten #vorbei ist 
				 - #CPU #Burst 
				 - Shortest #job first 
				 - #Duchschnitt #der zeit #des #Prozesses #wird genommen 

			 - Shortest remaining #time 

				 - #Verdrängung 
				 - #Wird #ein #prozess mit kürzerem burst #bereit dann #wird #der #aktuelle #abgelöst 

			 - #round #robin 

				 - Time #Sharing 
				 - #Gleicher #anteil #alle nach #einander 
				 - #Zeitscheibe 

					 - #Klein 

						 - #Kaum fortschritt 

					 - Groß 

						 - #Nicht responsive 

			 - Highest #priority first 

				 - #Nicht #verdrängend 

					 - #Bis selber #freigeben 

				 - Verdrängend #

					 - #Sobald #ein #höer #priorisierter #da #ist #wird #der #aktuelle #abgelöst 

				 - #Statisch #

					 - #Bei #erzeugung 
					 - Geschätzer #burst 
					 - #Geschätzer #io 
					 - #Geschätzter speicher 

				 - #Dynamisch 

					 - #Kann bei #laufzeit #geändert werden 
					 - #Aktuellerburst 
					 - #Aktueller #io 
					 - #Aktueller speicher 

				 - #Starvaation 

					 - Aging gegenstrategie 

			 - #Mehrstufen #verfahren 

				 - #Kombination #aus #mehreren #

		 - Die ready #warteschlange 

			 - #Process #management 

				 - #Dispatcher #

					 - Intern verfügbar 

				 - Schnittstellen #operationen 

					 - #System #calls 
					 - Interrupt handler #
					 - #Timer #Interrupt durch Prozessor #selbst 

						 - #Register #selbst 

			 - Implementierung 

				 - #Array mit prozessen 

					 - Konstruktor #aufruf #bei start #

				 - #Running #

					 - Terminate #macht inactive 

				 - Ready 

					 - Assign #macht running #

				 - Inactive 

					 - #initiate #dann #wird ready #

				 - Scheduler 

					 - #Wählt aus 

				 - #Store and #load #reg 

					 - #Store 

						 - Werte #werden #gespeichert #

					 - #load 

						 - #Werde #werden #geladen 

					 - Das #eigene #Stack #wird operiert 

				 - #Test and set befehl 

					 - Atomare #operation 
					 - #Spinlock waiting #

 - #Speicher 

	 - #Persistent 

		 - #I - #Node 

			 - Beschreibung #attribute 
			 - #Zeitstempel 
			 - #Zugriffsrechte 

				 - #r 
				 - #w 
				 - #x 

			 - #Beschreibung #auf #Referenzen 

				 - #referenzen #auf #dierekte #Dateiblöcke #auf #platte #
				 - #indierekt #

					 - #Einfach 

						 - #block #ist selbst #nur #eine #Index #Tabelle #

					 - zweifach #

						 - #index #tabelle 2 #layer 

					 - dreifach #

						 - #index #tabelle 3 #layer 

					 - vorteil #viel größere #Dateien #möglich 

	 - #nicht persistent 

		 - Speicher #zuteilung #zu #Programmen 

			 - #Einteilung in #Bereiche 

				 - Hauptspeicher #Kacheln 
				 - #Pro #programm in #einem stück #belegen 
				 - #Arrays 

					 - #Kopf mit information #wie #lang #array #ist 
					 - #Elemente #hintereinander 

				 - #Externe #Fragmanetierung #

					 - #Ablehnen 
					 - #Defragmentieren #/Basisregister #zum #verschieben 
					 - #Swapspace #nutzen 

			 - Overlay #technik 

				 - #Residenter #Teil 

					 - #Bleibende #Teile 

				 - Overlay #bereich #

					 - Austauschen 

				 - Benötigt schnellen #Massenspeicher 
				 - #Verwaltung #

					 - #Core #map - > belegung #
					 - #Auftragssteuerung #

				 - #Möglicherweise Interne + #Externe #Fragmentierung 

			 - Variable #länge 

				 - linked #list an #freihen #bereichen 
				 - #Verschmelzen #von #frei gewordenen #benachbarten #bereichen 
				 - #Einsatz i m #Heap 
				 - #Strategien 

					 - First fit 

						 - #Übrigen #bereich #wieder einketten 
						 - Bessere #Fragmentierung 

					 - Best #fit 

						 - #Bereich mit #wenigstem rest 
						 - Schlechtere #Fragmentierung #

					 - #Buddy 

						 - #Freier #Speicher ist #gegeben #
						 - #Vergibt #nur vielfaches #von 2er #potenzen 
						 - Eigene #Liste #für jede #Größe ( 16,32 .. ) 
						 - Fragmentierung ist #intern 
						 - #Wenn zu #groß element aus #enstprechender #Liste wird #halbiert 
						 - #Man darf #nur mit #buddy #verschmelzen 
						 - #Buddy #ist die andere #Hälfte #vom #halbieren 
						 - #Auf #geschwindigkeit #ausgelegt #hat #aber #hohen speicherbedarf #

		 - #Subtopic 2 #

			 - #Virtueller #Speicher 

				 - #Speicher #wird durch swap #space ergänzt 
				 - #Programm #hat eigene tabelle #
				 - #Nutzbare #adressen eines programms #sind #virtuell 

					 - #Umrechnung in echte adressen 

						 - #Seitentabelle 

							 - #Verweis welche seite in #welcher Kachel #
							 - #Verweis ob i m hauptspeicher #
							 - #Prozess #liegt in #einer #Reihe #
							 - #Map auf #hauptspeicher 
							 - #Seitennummer #P #
							 - #Wort W 

					 - #MMU 
					 - #Rechnen 

						 - #N ## seiten = #virtuelle #speicherröße / seitengröße 
						 - Speichergröße = #wortgröße #ausgerechnet 

					 - #Seitentabelleneintrag #

						 - #Kachelnummer 
						 - #Präsenz #bit 

							 - #Ist #es i m hauptspeicher #oder #nicht 
							 - #Seitenfehler interrupt 
 ( #pagefault interrupt #) 
 - > #Festplatte #läd inspeicher 

								 - #Block #, #assign , #deblock , running #

						 - #Referenz #bit 

							 - Ist #adresse #genutzt 

						 - #C bit 

							 - Ist etwas geändert #

						 - #Read 
						 - #Write 
						 - #Execute #
						 - #Hintergrundadresse #

					 - #hintergrundspeicher #

						 - #kacheln #werden #abgelegt 

					 - #Eigene #Seitentabellen #von prozessen 

						 - #prozesse #getrennt 
						 - Schutz 

				 - #Strategien 

					 - #Random 
					 - Least frequently used 

						 - 

					 - #Most frequently used 
					 - Second chance 

						 - #nicht #wichtig #i m #detail #für #klausur 

					 - #Optimal #

				 - #Probleme 

					 - #Trashing 

						 - #Zu #viele #prozesse #gestartet #
						 - #Großteil der #zeit ist #nur #ein und #auslagern #
						 - #Lösungsansatz : 

							 - #Ersetzungsstrategie #

								 - #Lokal 

									 - #Nur die seiten #die #Fehler verursachen werden #beachtet 
									 - #Für #den prozess besser 

								 - Global 

									 - #Seiten können unabhängig #von #ihrer prozesszugehörigkeit #ausgelagert werden 
									 - I m #großen und ganzen #besser 

							 - #Long wait #neuer #zustand #
							 - #Prozesse die zu #lange #allein #für #die #festplatte #brauchen , #auslagern #bis zeit und #ressourcen #da #sind 

					 - #Residente seiten #

						 - #Seiten in #EA #Operation #einbezogen #sind 
						 - Locked down bits #

							 - #Wenn gesetzt #.- > #kann nicht #ausgelagert werden 

			 - #Speicher 

				 - #Arbeitsspeicher 

					 - Adressräume 

						 - #Zuteilung 

							 - Code Daten 

								 - #statische #variablen 
								 - #Globale #Variablen 

							 - #Heap 

								 - Objekte 
								 - #datenstrukturen 

							 - #Stack 

								 - #Stackframe mit #Rücksprungadressen #
								 - #Unterprogramme 
								 - #Deren #Variablen 

						 - #Rechte 

							 - #Veränderung Löschung 
							 - #Zugriffsschutz 

					 - #Swapspace 

						 - Paging #file / #auslagerungsdatei 
						 - #Zeitweise #Teile des #Speichers #Auf #Festplatte