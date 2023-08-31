# Kommunikations und Betriebssysteme

## Kommunikations Systeme

### Übertragen

- pysical Layer

	- Nyquist

	- Übertragungsmedium

		- Kabel

			- Coax

			- Twisted Pair

		- Kabellos

			- Bluetooth

			- Wifi

- Regelungen

	- Protokolle

		- Header

		- Trailer

		- Modelle

			- OSI

				- 7 Application Layer

				- 6 Darstellung

				- 5 Session

				- 4 Transport Layer

				- 3 Network Layer

				- 2 Datalink Layer

				- 1 Pysical Layer

			- TCP IP

				- Anwendung

				- Transport

				- Internet

				- Netz

			- Vorlesung

				- 5 Application Layer

				- 4 Transport Layer

				- 3 Network Layer

				- 2 Datalink Layer

				- 1 Pysical Layer

	- Flow control

		- Datenstruktur

			- Header

			- payload

			- Trailer

		- Sliding window

			- Empfangsfenser ändert sich laufend

			- Beschädigte frames bleiden stehen bis sie korrigiert wurden

			- Puffer beider seiten 

			- Bestätigt wird immer das höchtse element aus dem gesamten block

		- Schnittstellen

			- Abholen

				- Networklayer

				- Ack ( acknowledge)

			- Weitergeben

				- Physical layer

				- Wait for event

		- Sequenznummern

			- Nummer des pakets

			- Nummer des „trys“

		- nummerierte pakete

			- Nicht angekommene werden erneut angefordert

		- Go back n

		- Selective repeat

	- Netzwerkschicht

		- Probleme

			- Eindeutige Bezeichner

			- Pakete Weiterleiten

		- Routing

			- Welche route ist im MOMENT die beste

			- Flooding

				- An Alle schicken

				- Alle leiten an alle weiter

				- Unendlich viele Nachhrichten

					- Lösen durch

						- TTL

							- Runterzählen eines counters für jede weiterleitung

							- Bei 0 wird gelöscht

						- Speichern was bereits gesehn wurde

			- Minimaler spannbaum

				- Von sich ausgehend eien baum bilden durch den gesendet wird

				- Dijkstra algorythmus

					- Aller erreichabren knoten gewichten

					- Jeder bringt nachricht näher an das zeil#

			- DISTANCE vector routing

				- Jeder veröffentlicht regelmäßig seine Kosten zum erreichen 

				- Kleinste kombination wird genutzt

				- Count to infinity problem

					- Wenn ein eingegliederter Konten ausfällt

					- Gegenseitiges hochzählen weil gewichtungsprozess nicht vollständig synchron

			- Link state routing

				- Broadcastinfos in Teilnetz

					- Flooding

					- link state Paket

						- Welche Kosten

						- Welche nachbarn

				- Spannbaum bilden

					- Dijkstra

				- Schnelle Konvergenz

			- Hirarchisches routing

				- Verfahren skalieren nicht mit wachsender Größe des netzes

				- Routing tabellen sind zu groß

				- Mehrstufiges routing 

					- Unterteilen in Regionen

					- Routen bis zur region

					- Simplifizieren der Struktur 

	- Transportschicht

		- ziel

			- einheitliche dienste für einheitliche vorgänge

			- anwendungen schnittstelle liefern 

				- System calls

		- adressierung

			- TSAP

				- Transport service ACcess Point

				- Kommunikation zwischen 2 prozessen

				- kommunikationsendpunkt = Socket

					- Socket adtesse = ( Ip adresse, port nummer)

			- Unterknoten 2

		- verbindungsorientiere kommunikation

			- CR: Erster Versuch zum verbindungsaufbau

			- DR: Disconnect request

			- Ack: bestätigung

			- Data

			- was bei fehlern:

				- Anforderung geht verloren

					- nochmal senden

				- bestätigung ging verloren

					- weitere verbindung aufbauen ( unnötige last)

				- eins von beidem wird verzögert

					- in timeout laufen und erneut aufbauen

			- Sequenznummern 
Dreifacher Handshake

				- immer eindeutige sequenznummern verwenden

				- ISN : Initiale Sequenznummer

				- Beide nehmen seperate zähler für ihre nachrichten x,y

				- nicht passsende werden verworfen

			- Verbindungsabbau

				- problem der 2 Armeen
(distributed consensus)

					- kann man wirklich wissen ob die verbindung abgebaut werden soll

					- wir wissen von der letzten nachricht nicht ob sie ankam

				- lösung per Timeout

					- server werden "ungeduldig"
brechen dann schneller ab

					- hosts führen relesase connection nach fehlender antwort durch

					- auch nicht optimalm, weil problem unlösbar

			- Flusskontrolle

				- Ziel

					- Speichersparsam weil sliding window zu ville puffer bräuchte

				- TPDUs

					- segmente

				- puffer

					- nur noch nicht bestätigte TPDUs werden gepuffert

					- es ist sinnvoll große puffer zu haben für schnelle übertragung
aber wenigersinnvoll für speicher

					- sobald freigegeen wird nachricht aus puffer entfernt

					- sender weis wie viele pufferplätze empfänger hat, wenn er keine merh hat sendet er nicht bis empfänger verarbeitet hat

					- bestimmung der Größe

						- c*r = "übertragungsgeschwindigkeit"

						- wie viele können wir in einer RTT senden 

		- TCP

			- Transmissuin Control Protocolll

			- TCP= zuverlässige end to end verbindung

			- segmente 

				- TPDUs

				- Fragmentierung wenn zu groß

			- Sockets

				- streamorientiert aus sicht der anwendung

				- socket adresse

					- ip adresse

					- port nummer

			- ablauf einer kommunikation 

			- TCP Handshake

			- Sillywindow Syndrom

				- wenn puffer voll und immer nur in kleinen stücken geleert

				- viele pakete senden weil immer wieder etwas frei wird

				- Eigener Puffer im programm implementieren

					- flush befehl
sendet dann den eigenen Puffer dann wieder an TCP puffer

- Anwendungsschicht

	- was 

		- verarbeitungsschicht

		- Dienste

	- DNS

		- aufgabe

			- auflösen IP, zu Dienst

			- Domains auflösen

		- Server

			- verteilte Datenbank

			- leistet die umsetzung

			- kaskadierend von Top level Domain aus

				- rekursiv

					- cache

				- iterativ

					- kein cache

		- CACHE

			- speichern bereits aufgelöster ung benutzter adressen

	- WWW

		- html

		- hypermedia

		- http

		- Subtopic 4

	- Komprimierung

		- Daten lassen sich reduzieren

		- nachteil

		- Prinzipielle Verfahren

		- Entropie

			- Verlustfrei

			- lauflängen

				- AAAA -> 4A

			- Statistisch

				- wörterbuch der Codes wird mitgesendet

				- huffman

					- allg

					- baum

		- Quellkodierung

			- Color lookup table

				- wiederholende farben werden gespeichert

			- differenzialkodierung

				- nur differenzen übertragen bei zb. video

			- Transformationskodierung

				- DCT

				- Fourier

			- vectorquantisierung

				- zweidimensionaleBilder werden in quadrate gerastert

			- Verlustbehaftet

			- jpeg

	- Datensicherheit

		- Ziele

			- Schutz Vertraulicher Daten

			- Sicheres ermitteln verfasser

			- Integrität

		- Symetrisch

			-  

			- kennt man wirklich den sender?

		- Asymetrisch

			-  

			- 2 schlüssel

		- Datenschutz unterschied

			- datenschutz = personenbezogen

		- TSL

			- Name, Schlüssel = zertifikat

			- nicht jeder kann zertifizieren

			- Sitzung

- Store and Forward Prinzip

	- Einpacken und Versenden

	- Puffern, Auspacken, auswerten, verschicken

- Frame

	- anfang

		- DLE STX

	- Ende

		- DLE ETX

	- Fehler Korrektur

		- Crc

	- Bit stuffing

		- Erkläten

- Mac Sublayer

	- ALOHA

		- Timeout wird genutzt

		- Kollisionen

			- Poisson verteilung

				- T Frame Zufallsvariable

					- Neu eingetroffene Frames

				- Parameter N 

					- Wahrscheinlichkeit im Mittel dass gesendet wird

				- Parameter G

					- >= N

					- Zusätzlich also kollisionen

					- Kanalbeslastung

					- P0=E^-2G

				- Durchsatz S

					- G*p0

	- CSMA

		- Carrier sense multiple Access

		- 1 persistent

			- Warten bis kanal fri

				- Erst hören dann senden

		- Nicht persistent

			- Wenn kanal belegt warte zufällige zeit

		- P persistent

			- Falls slot frei sende mit wahrscheinlichkeit p

	- CSMA/CD

		- Carrier sense multiple access collision detection

		- Kanal lauschen  bie übertragung

		- Beginen sobald kanal frei

		- Lausche auch während übertragung

		- Wenn kollision brich ab und warte mit wahrscheinlichkeit p

	- Bit map

		- Reservierden

		- „Connection slots“

			- Konkurenzphase

	- Binäre countdown

		- Station bekommt id

			- Id => prio

		- Eigene ID als binärzahl senden in konkurenzphase

		- Kanal verknüft oder schritt für schritt 

		- Id die nicht übereinstimmt hört nichtmehr zu

		- Einsatz im canbus 

			- Steuergeräte im auto

		- Mok und Ward

			- Wenn gesendet hat wird prio auf 0 gesetzt

	- Ethernet

		- Frame layout

			- Preamble

			- Frame delimiter

			- Destination

			- Source

			- Length of data

			- Padding

				- Zufällg für mindestlänge

			- Checksum crc

			- Freitext

		- Csma/cd

			- Binary exponential backoff

				- Zufallszeit warten nach ersteer kollision

					- Nach 1 kollision jetzt oder im nächsten frame

					- Nach 2 jetzt oder bis zum 4ten

				- Immer verdoppeln nach weiterer kollision

				- Nicht mehr als 10

		- Fast ethernet

			- Mehr datenrate

		- Gigabit ethernet

			- Keine kollisionserkennung 

			- Nur noch switches

### Netzwerke

- Topologie

	- Bus

		- Akteure an einem Gemeinsamen Bus

		- Kollision möglich

	- Ring

		- Akteure in einem Ring Organisiert

		- Token wird als "Rederecht" genutzt

- Routing

- Verbundsystem

	- Geräte

		- Endgerät

			- Netzwerkkarte

				- MAC Adresse

				- Netzwerklokale IP adresse

		- Verwaltungsgerät

			- Switch

			- Repeater

			- Hub

			- Bridge

			- Router

	- Verbund Netz

		- Intranet

			- Firmen Internet 

			- Nutzt Internet Protokolle

		- Extranet

			- Home Office

		- Internetzugang im Lokalen Netz

			- LAN

			- WAN

			- Internet

### Anwendungsmöglichkeiten

- VoIP

- Streaming

- E Mail

- Mehrfach Nutzen von Diensten

	- Parallel Berechnen

		- Compute Cluster 

	- Update Delivery Optimization

	- Dateitransfer

	- Einbettung ins Betriebssystem 

		- Zuordnung Nachricht zur Anwendung (Port nummer)

		- Interrupt Konzept

### IP

- Ip Adressen

	- besondere Adressen

		- 0.0.0.0

			- dieser Host

		- 0.0.Host

			- Unterknoten 1

		- netz.255.255

			- Broadcast adresse

	- NAT protokoll

		- Private Adressen über eine Internetfähige Adresse

		- Internetfähiger Router übernimmt zugriff

		- Router MAppt Private Adressen auf eine Netzadresse

	- Subnetting

		- CIDR

			- Notation

				- /24 =255.255.255.0

				- /"anzahl der 1er"

			- Routing tabelle 

				- IP adresse ist mit NEtzmaske bereits gespeichert

				- ergebnis einer gültigen "rechnung" sit mit einem ausgangsinterface verknüpft

			- verfahren

				- Adresse AND subnetzmaske

				- ergibt netzadresse

- IP routing

	- Open Shortest path first

		- Benefits

			- Schnelle konvergenz

			- Loop frei

			- VLSM und CIDR subnetting

		- Characteristics

			- SPF alogrythmus

			- Link state routing

		- Features

			- Gruppenkonzept zum simplifizieren

			- möglichkeit BFD Protokoll zu nutzen

	- BGP ( Border Gateway Protocol)

		- Typ

			- Exterior Gateway routing

			- modifiziertes distance vector routing

				- "behebt" count to infinity

		- Eigenschaften

			- sehr große routing tabellen

			- Manuelle Regeln

				- konfiguration von routing "nogos"

		- Netze werden verschaltet

	- ICMP ( Internet Control Message Protocol)

		- Internet Control Message Protocol

		- Nutzen

			- Pings

			- Fehler

			- Status

		- Erkennen von ICMP Paketen

			- wenn ein Paket verloren geht wird nocht reagiert

			- der Sender "wartet" bis etwas ankommt

				- mit timeout

	- ARP

		- Adress Resolution Protokol

		- Nutzen

			- Aufschlüsseln von MAC und IP im "heim"Netz

		- ARP Request

			- Aufbau

				- Frage

					- Who has "adresse"

					- broadcast

				- Antwort

					- der Besitzer der adresse Antwortet

		- ARP Erkennen

			- Schicht 2 Header ( Mac)

		- ARP Spoofing

			- der falsche antwortet absichtlich dass er die Adresse hat

			- Interner Angriff

	- IPv6

		- Aufbau

			- Adressen

				- Hexadezimal ziffern

					- :: -> 00en 1x pro adressse für kürzung

				- 16 Byte gesamt

				- global unicast ( GUA)

				- site local

			- paket

				- Class

					- label

				- header

				- Destination

				- source 

		- Header

			- wurde möglichst klein gehalten 

			- keine TTL

		- Features

			- jumbo pakete ( 4gb)

			- kleinere Routing tabellen

			- mehr sicherheit

			- QoS

			- Anycast

				- an eine Gruppe 

				- geringere Netzlast als Broadcast

				- Nachricht wird vom schnellsten geantwortet

			- Multicast

				- Gruppen kommunikation

			- Stateless Adress autoconfig (slaac)

				- fe80:: MAC:

				- test auf neigbour solicitation  anstelle von ARP

				- Anschließend des generieren einer (global unicast)

### IP paket header

- 32 Bits

	- Version

		- IHL

			- Type of Service

				- Totallenght

	- Identification

		- Fragment offset

	- TTL

		- Protocol

			- Headerchecksum

	- Source Adress

	- Destination Adress

	- Options (0 oder mehr)

		- Optionen

			- security

				- wird nicht verwendet

			- Strict source routing

				- testzwecke

			- Loose source

				- Liste von Routern die besucht werden sollen

			- Record ROUTE

				- TraceRT

			- Timestamp

### Wahl der Timeout Ziet

- Subtopic 1

- ETT Timeout abschätzung

	- schätzen mittelwert

	- schätzen Standardabweichung

### UDP

- Verbindungslos

- Übertragung roher pakete

- pseudo header

- Anwendungen versenden kurzer nachrichten

## Hardware Grundlagen

### von Neumann

- Bus

	- Datenbus

	- Adressbus

	- Steuerbus

- EA Geräte

	- Oft unabhängig von Prozessor

	- eigene Controller

	- Direct Memory Access

		- Auslesen und eingeben

		- ohne Mithilfe vom Prozessor

- Speicher

	- Hauptspeicher

		- Byte orientiert

		- Wort orientiert

		- Kapazität

			- KiB

				- 2^10

			- KB

				- 1000 Byte

	- Cache

		- Kaskadierend

			- L1

			- L2

			- L3

		- Koherenz

			- Write back

			- Write through

			- Snoopy

	- RAM

- Interruption

	- Ursachen

		- Synchron

			- Programmbezogen

				- Fehler

		- Asynchron

			- Systembezogeb

				- Hardware

	- Wirkung

		- Unterbrechung

		- Welcher code ?

			- interrupt Vektor aus Tabelle

		- Nach abarbeiten weitermachen As Usual

	- zulassen oder unterbinden

		- IRR

			- Anforderung

		- IER

			- Erlaubnis

		- Prioritäten Konzept

- Prozessor

	- Register

		- Mehrzweckhalle

		- Gleitpunkt

		- Steuer

			- Befehlszähler

			- Befehls Register

			- Kellerregister

		- Dopplung der Register

			- virtuelle Prozessorkerne

			- Wechsel zwischen den Registern

	- Rechenwerk

	- Steuerwerk

	- Prozessor Zustand 

		- Maschienenzustand

			- An 

			- Aus

			- Boot

		- Funktionszustand

			- Gültiger registersatz

		- Privilegien

			- Zugriffs schutzkonzept

				- Virtuelle Adressen

			- Usermode

				- Eingeschränkte Befehle

			- Privileged

				- Alle Befehle

- System Calls

	- benutzerprogramme aus Routinen

	- Fork

		- Erzeugen eines Kindprozesses

	- Wait Pid

		- Warten bis kindprozess beendet

	- Exit

		- Rausgehen

	- (Linux Kommandos)

## Betriebs Systeme

### Aufgaben

- Prozesse

- Speicher

	- Speicherverwaltung

		- Working set

			- Von einem programm wird working set erstellt

			- Einzelne teile des programms werden ausgelagert

			- Quasi: Ungenutzte routinen bleiben ungeladen

		- Paging Daemon

			- Regelmäßig kacheln freiräumen

			- Kacheln sind schon frei, dass nichts extra ausgelaget wird wenn es was zu tun gibt

		- Gemeinsam Verwendete seiten

			- Copy on write

				- Fork kopiert den elternprozess

				- Effizienter

					- Nur seitentabelle kopieren

					- Eltern und kindprozesse verwenden selbe seiten

					- Alle seiten sind read only

					- Bei schreibzugriff

						- Schutzverletzung

							- Interrupt

					- Seite wird erst bei schreiboperationen wirklich kopiert 

- Dateisystem

	- Datei

		- Dateiarten

			- Programme

			- Makros

			- Objektprogramme

			- Binärprogramme

				- ausführbar

			- auftragsprotokolldateien

			- System protokoll dateien

			- archivdatei

		- Namensverwaltung

			- hirarchisch

				- Selber name in verschiedenen Verzeichen möglich

				- Verzeichnisoperationen möglich

				- Dateibaum

					- user directories

					- Verzeichnisse

			- Dateiverzeichniseintrag

				- attribute

				- Werte

			- Dateiverzeichnis unabhängig

				- verweis auf Verwaltungsstruktur

			- links

				- hardlinks

					- "pointer"

					- kein baum mehr

						- mögliche Zyklen

						- keine hardlinks auf verzeichnisse

					- zähler von verweisen

				- symbolic link

					- verweis auf pfad

	- Aufgaben

		- einheitlicher zugriff egal wie oder wo gespeichert

		- Organisieren vom Speicherplatz

		- Logische zugriffsoperationen

		- Schutzmechanismen

	- Schichtenmodell

		- Hardware

			- Festplatte

				- Einteilung in Spuren->sektoren-> blöcke

				- Langsame zugrifsszeiten

			- Solid State Drive

				- Flash speicher

				- schnelle zugrifsszeiten

		- Controller

			- zugriffsoperationen regeln

			- gezieltes Speichern und löschen 

	- Physikalisches Dateisystem

		- begriffe

			- Datei

				- menge von zusammengehörigen blöcken 

			- Block

				- zusammenhängender speicherbereich

			- Plattendateiverzeichnis

				- inhaltsverzeichnis

			- Dateideskriptor

				- Dateityp

				- Position

				- länge

		- aufgaben

			- organisation auf externen Datenträgern

			- verwaltung der Dateien

			- parallele zum Virtuellen speicher

		- verwaltung des Dateisystems

			- partitionen 

				- boot

				- super

				- freespace

				- I-Nodes

				- root

			- Probleme von caching

				- möglicher verlust von Baumteilen

			- Journaling

				- log 

					- infos über was getan wurde

					- wird sofort geschrieben

					- wiederherstellung

				- änderungen von Metadaten persistent machen

			- anforderungen an ei Modernes System

				- große partitionen

				- schnell

				- sicher vor crashes

	- Freier Speicher

		- Listenmethode

			- verkettete liste

		- Index methode

			- freie blöcke werden indexiert verwaltet

			- baum struktur

				- blatt = index

				- ast = weitere liste

			- bitvektor

				- fibt an ob belegt oder nicht

		- vektor methode

	- Strategien

		- zusammenhängend

		- Gestreut

			- wenn datei zu groß,
weiteren deskriptor nutzen

	- Schutz

		- Discretionary Access Control

			- Zugriffsrechte

				- read

				- write

				- exec

				- delete

			- Benutzerkategorien

				- System

				- Subtopic 2

			- Schutzmatrix,
wer von wem

			- Benutzerverwaltung

			- Anwendung

				- unix hat das konzept ohne löschen

		- Allgemeine Zugriffsmatrix

			- Nutzer in reihen

			- Dateien in Spalten

			- Wert = Zugriff

			- Nachteil

				- viel speicher

		- acess control list

			- Auflösen der Zugriffsmatrix in für ein Objekt alle Subjekte

			- leere fallen weg

			- probleme

				- benutzerlöschen

		- capability list

			- Auflösen der matrix pro benutzer ( subjekte)

			- leere rechte fallen weg

			- probleme

				- benutzer hatte mal rechte, aber sie sind weg

				- altesTicket wird genutzt

				- löschen einer Datei

		- Mandatory acess control

			- Bell Lapardula

				- Subjekte und Objekte Klassifizieren

				- Zugriffsrechte von System entschieden

				- Klassifikation

					- geheim

					- vertraulich

					- öffentlich

			- Rollenbasiert

				- Benutzern werden rollen zugeordnet

				- Rechte aus Kontext und Rolle

				- viel administration nötig

			- probleme

				- Komplex und Unhändlich

## Klausurrelevant 

### BS

- Semaphore

	- Semaphor Konzept

		- Synchronisierung 

			- Innerhalb

			- Außerhalb

			- Syncro

				- multithreading

					- Race cnditions vermeiden

						- Syncro 

							- schlecht

								- Busywaiting

							- Gut

								- Dekker

									- Atomare speicheroperationen+

							- Besser

								- Eigener prozessorbefehl

									- Spin lock warteschliefe

									- Test and set befehl

		- Definition

			- Up and down

				- Atomar durch mutex

			- Zähler 

				- Wie viele betriebsmittel sind da

				- Buchführung 

				- Positiv

					- Anzahhl der Verfügbaren

				- Negativ

					- Wie lang ist die warteschlange

			- Prozesswarteschlange

		- Implementierung

			- Konstruktor 

				- FIFO warteschlange

				- Counter = übergabewert

			- P = down

				- Mutex

					- Counter —

					- Counter< 0

						- Block prozess

						- Assign

			- V=up

				- Mutex

					- Counter++

					- Counter <=0

						- Deblock

		- Gegenseitiger ausschluss

			- Mutex

				- Mutex.p

				- Mutex.v

				- kritischer abschnitt

					- Enter mutex

					- Prozess

					- Exit mutex

- Prozessverwaltung

	- Interrupts

		- E/A  Operationen

			- Rahmen bedingungen:

				- Geschwindigkeitsunterschiede

				- Parallelarbeit von CPU und E/A

			- Synchrone schnittstelle

				- Eigener System call

				- E/A Gerät  arbeitet für sich parallel

				- Gerät erzeugt interrupt

				- E/A interrupt handler

				- Timer interrupt handler

					- Resign

					- Assign

				- Eigene Blockiert warteschlange pro gerät

				- Recap: Prozess bleibt nicht im kontrollfluss

			- Asynchrone E/A Schnittstelle

				- System calls

					- Iostart

						- Anstoßen der E/A

					- Io wait

						- Warten bis daten vorliegen

				- Gerät schickt interrupts

				- E/A interrupt handler

					- Notieren 

						- Wenn io wiat noch nicht war

					- Blockieren

						- Wenn io wait läuft

				- Wenn noch nicht abgearbeitet

					- Timer innterrupt handler

				- Recap: Prozess der wartet bleibt im kontrollfluss

				- nebenläufige Abläufe

	- Scheduling

		- Prozessorganisiation

			- Dialog

				- Interaktiv

				- Ziel ist interaktives arbeiten

				- bevorzugt io

			- Stack

				- in Batches

				- Ziel ist auslastung

				- Bevorzugt prozesse die Ressourcen brauchen die gerade ungenutzt sind

			- Real time

				- Ziel einhaltung der Zeitgarantie

				- Bevorzugt Prozesse die knappe fristen haben

		- Thread vs Prozess

			- Thread ist bestandteil von prozess

				- Thread hat immer einen kontrollfluss

		- Timeline

			- Kurzzeit

				- Welcher prozess akut

				- Aufruf in kurzen abständen

			- Langzeit 

				- Swapping

					- Auftrag Sofort zu prozessoren

					- Überlast zustand -> zurückstellung in externen datentrger

				- Autragsverwaltung

					- Auftragswarteschlange

					- Je nach last

					- Überlast -> verdrängung

						- Swapspace auf Festplatte

		- Kriterien

			- Zeit

				- Wartezeit

				- Umlaufzeit

				- Echtzeit

				- Antwortzeit

			- Leistung

				- Leistungsfähigkeit

				- Auslastung

				- Durchsatz

		- Klassifikation

			- kooperativ

				- Keine gezielte kontrolle

				- Nur durch interrupts

			- Verdrängendes

				- Prozess wird verdrängt

		- verfahren

			- First come first serve

				- Der der am längsten im rdy zustand ist ist an der reihe

				- Keine verdrängung

				- Leere anweisung-> NOP Schleife

			- Shortest processing time

				- Der der am schnellsten vorbei ist

				- CPU Burst

				- Shortest job first

				- Duchschnitt der zeit des Prozesses wird genommen

			- Shortest remaining time

				- Verdrängung

				- Wird ein prozess mit kürzerem burst bereit dann wird der aktuelle abgelöst

			- round robin

				- Time Sharing

				- Gleicher anteil alle nach einander

				- Zeitscheibe

					- Klein

						- Kaum fortschritt

					- Groß

						- Nicht responsive

			- Highest priority first

				- Nicht verdrängend

					- Bis selber freigeben

				- Verdrängend

					- Sobald ein höer priorisierter da ist wird der aktuelle abgelöst

				- Statisch

					- Bei erzeugung

					- Geschätzer burst

					- Geschätzer io

					- Geschätzter speicher

				- Dynamisch

					- Kann bei laufzeit geändert werden

					- Aktuellerburst

					- Aktueller io

					- Aktueller speicher

				- Starvaation

					- Aging gegenstrategie

			- Mehrstufen verfahren

				- Kombination aus mehreren

		- Die ready warteschlange

			- Process management

				- Dispatcher

					- Intern verfügbar

				- Schnittstellen operationen

					- System calls

					- Interrupt handler

					- Timer Interrupt durch Prozessor selbst

						- Register selbst

			- Implementierung

				- Array mit prozessen

					- Konstruktor aufruf bei start

				- Running

					- Terminate macht inactive

				- Ready

					- Assign macht running

				- Inactive

					- initiate dann wird ready

				- Scheduler

					- Wählt aus

				- Store and load reg

					- Store

						- Werte werden gespeichert

					- load

						- Werde werden geladen

					- Das eigene Stack wird operiert

				- Test and set befehl

					- Atomare operation

					- Spinlock waiting

- Speicher

	- Persistent

		- I-Node

			- Beschreibung attribute

			- Zeitstempel

			- Zugriffsrechte

				- r

				- w

				- x

			- Beschreibung auf Referenzen

				- referenzen auf dierekte Dateiblöcke auf platte

				- indierekt

					- Einfach

						- block ist selbst nur eine Index Tabelle

					- zweifach

						- index tabelle 2 layer

					- dreifach

						- index tabelle 3 layer

					- vorteil viel größere Dateien möglich

	- nicht persistent

		- Speicher zuteilung zu Programmen

			- Einteilung in Bereiche

				- Hauptspeicher Kacheln

				- Pro programm in einem stück belegen

				- Arrays

					- Kopf mit information wie lang array ist

					- Elemente hintereinander 

				- Externe Fragmanetierung

					- Ablehnen

					- Defragmentieren /Basisregister zum verschieben

					- Swapspace nutzen

			- Overlay technik

				- Residenter Teil

					- Bleibende Teile

				- Overlay bereich

					- Austauschen

				- Benötigt schnellen Massenspeicher

				- Verwaltung

					- Core map -> belegung

					- Auftragssteuerung

				- Möglicherweise Interne + Externe Fragmentierung

			- Variable länge

				- linked list an freihen bereichen

				- Verschmelzen von frei gewordenen benachbarten bereichen

				- Einsatz im Heap

				- Strategien

					- First fit

						- Übrigen bereich wieder einketten

						- Bessere Fragmentierung

					- Best fit

						- Bereich mit wenigstem rest

						- Schlechtere Fragmentierung

					- Buddy 

						- Freier Speicher ist gegeben

						- Vergibt nur vielfaches von 2er potenzen

						- Eigene Liste für jede Größe (16,32..)

						- Fragmentierung ist intern

						- Wenn zu groß element aus enstprechender Liste wird halbiert

						- Man darf nur mit buddy verschmelzen

						- Buddy ist die andere Hälfte vom halbieren

						- Auf geschwindigkeit ausgelegt hat aber hohen speicherbedarf

		- Subtopic 2

			- Virtueller Speicher

				- Speicher wird durch swap space ergänzt

				- Programm hat eigene tabelle

				- Nutzbare adressen eines programms sind virtuell

					- Umrechnung in echte adressen

						- Seitentabelle

							- Verweis welche seite in welcher Kachel

							- Verweis ob im hauptspeicher

							- Prozess liegt in einer Reihe

							- Map auf hauptspeicher

							- Seitennummer P

							- Wort W

					- MMU

					- Rechnen

						- N# seiten = virtuelle speicherröße / seitengröße

						- Speichergröße = wortgröße ausgerechnet

					- Seitentabelleneintrag

						- Kachelnummer

						- Präsenz bit

							- Ist es im hauptspeicher oder nicht

							- Seitenfehler interrupt
(pagefault interrupt)
-> Festplatte läd inspeicher

								- Block, assign, deblock, running

						- Referenz bit

							- Ist adresse genutzt

						- C bit

							- Ist etwas geändert

						- Read

						- Write

						- Execute

						- Hintergrundadresse

					- hintergrundspeicher

						- kacheln werden abgelegt 

					- Eigene Seitentabellen von prozessen

						- prozesse getrennt

						- Schutz

				- Strategien

					- Random

					- Least frequently used

					- Most frequently used

					- Second chance

						- nicht wichtig im detail für klausur

					- Optimal

				- Probleme

					- Trashing

						- Zu viele prozesse gestartet

						- Großteil der zeit ist nur ein und auslagern

						- Lösungsansatz:

							- Ersetzungsstrategie

								- Lokal

									- Nur die seiten die Fehler verursachen werden beachtet

									- Für den prozess besser

								- Global

									- Seiten können unabhängig von ihrer prozesszugehörigkeit ausgelagert werden

									- Im großen und ganzen besser

							- Long wait neuer zustand

							- Prozesse die zu lange allein für die festplatte brauchen, auslagern bis zeit und ressourcen da sind

					- Residente seiten

						- Seiten in EA Operation einbezogen sind

						- Locked down bits

							- Wenn gesetzt .-> kann nicht ausgelagert werden

			- Speicher 

				- Arbeitsspeicher

					- Adressräume

						- Zuteilung

							- Code Daten

								- statische variablen

								- Globale Variablen

							- Heap

								- Objekte

								- datenstrukturen

							- Stack

								- Stackframe mit Rücksprungadressen

								- Unterprogramme

								- Deren Variablen

						- Rechte

							- Veränderung Löschung

							- Zugriffsschutz

					- Swapspace

						- Paging file / auslagerungsdatei

						- Zeitweise Teile des Speichers Auf Festplatte

				- Datenerhaltung Hauptspeicher

					- Zugriffe

						- Lesen

						- Schreiben

					- Abstraktion Datei

						- Dateisystem

## Crc

