# Advanced IT

## shell

### Unix

- Mehrbenutzersystem

- zu großem Teil in C geschrieben

- nahezu an allen Geräten zu finden

### Programm&Prozess

- Programm ist nur der Code

- Prozess ist sobald ausgeführt

- Prozess umfängt zusätzlich Adressbereich

- Vordergrund&Hintergrundprozess

	- Läuft der Proezess in der Shell ? wenn ja Vordergrund

### Umgebungen

- $Home

- $path

### Bash

- Bourne Again Shell

- Platzhalter Bash

	- * für Beliebig viele Zeichen

	- ? für genau ein zeichen

- Umleiten

	- Pipe

		- weiterleiten Ausgabe mit eingabe von A nach B

		- Verkettung Funktionalitäten

	- <

		- standardeingabe

	- >

		- Standard Ausgabe

	- 2>

		- Standard fehlerausgabe

	- /dev/

		- null

			- hierhin kann man dinge leiten wenn sie egal sind

		- zero

			- Endloe folge null

		- urandom

			- Zufalls bits

- Programme

### copy on write

- Copy ist ein Link auf original

- änderungen werden gespeichert

- link counter

	- behält wie viele auf das dokument zeigen

	- erst wenn auf 0 dann darf man löschen

## Prozesse und Threads

## Sockets

## Syncronisation

