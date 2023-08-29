# ## #Schreiben und lesen #Datei 
 ( #klausurrelavant #weil #Exception #handling ) 

 - #Writer 

	 - .write 

		 - möchte #string 
		 - #schreibt alles #hintereinader weg 

			 - #\n 
			 - #lineseperator 

	 - #mögliche #fehler 

		 - #Schreiben 
		 - lesen 
		 - #sonstige 

	 - #blockiert #solange datei #wie #wir sie #benutzen 

 - #Reader 

	 - #File #reader 

		 - #mögliche #fhler 

			 - #io #exception 

		 - Cloasable #interface #für try with #ressource 

			 - #damit #man das #verschachtelte finally #nicht notwendig tist 

		 - Schleife zum lesen 
