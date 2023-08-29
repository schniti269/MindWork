# ## #Serialisieren #von #objekten #

 - #Problem 

	 - #manche #datenstrukturen sind keine Reihen ( #zb listen ) #sonder #haben #tiefe 
	 - #aufschreiben #ist #aber #eine #Reihe 

 - Wo 

	 - Bäume 
	 - #Graphen #

 - Was 

	 - #definierte #reihenfolge 

		 - #man #wies #wie #man es #geschrieben hat #
		 - #das #ganze wieder einlesen #und #dann objekt erzeugen 

 - #Beispiel 

	 - Personen #objekt 

		 - name : #klaus #
		 - alter #: 27 

	 - #csv #variante #

		 - #serialize ( ) ; 

			 - #person.file= #
 #klaus;27 
 peter;46 

		 - #json 

			 - #taggen 

		 - #xml #

			 - #taggen #

 - #wie #

	 - serializable #interface 

		 - #java #macht #das automatisch 
		 - #i #d #sollte #man final setzen 
		 - #ein #stream #der #schreibt 

		 - ein #stream #der die #objekte #seriealisiert und #den #anderen #stram #bekommt 

 - #transien modifier 

	 - redundatnte daten ausschließen 
	 - #persistentens #nicht #gefährdet 

