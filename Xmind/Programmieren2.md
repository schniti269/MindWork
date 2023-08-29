# Programmieren 2 

## Exception handling

### Throwable
interface

- Exeption

	- Unchecked

		- Runtime
		- Automatische Weitergabe
		- Kann behandelt werden 
		- Oftmals logische Fehler

			- Oft of Bunds
			- DIV By 0

	- checked

		- Exception
		- Muss behandelt werden
		- Explizites auslösen

- Error

	- Stack

		- Stack overflow

### Grundprinzip

- Laufzeitfehler

	- Wird ausgelöst 

- Fehlerbehandlung

	- Direkte Behandlung
	- Weitergabe
“hot Potato“

- Weitergabe
- Nichtbezahlung-> Laufzeitfehler

### Exception klassen

- Klasse extends Exception
- Konstruktor ruft Superkonstruktor auf

	- InfoString

- Möglichst früh Aufrufen
- Throwable

	- Fehlertext
	- To String Objektinfos
	- Stracktrace

### Keywords

- Try und Catch

	- Try

		- Code under Inspektion
		- Code that might Throw exception
		- Semantik neighbours

	- Catch

		- Aufruf Exception

			- e

		- Verpflichtend
		- E.getMessage()
		- Stacktrace
		- Besonderheit

			- Methode die mehrere Ausnahmen werfen kann
			- Eigene Catchblöcke

				- Instance of
				- Ziel:
so spezifisch wie möglich abfangen
				- 

	- Finally

		- Immer ausgeführt
		- Unabhängig von Methode

- Throw

	- Throws

		- Exceptionklasse aufführen an Methode
		- Zwingt Methode die Exception zu behandeln

	- Throw

		- An aufrufer geben
		- Werfen = jemand muss fangen ( spätestens Main) 
		- Abarbeiten, kaskadierend nach oben

### Try with Recource

- in die klammer hinter try kommt die ressource
- benötight kein finally mehr 
- bspw cloasable interface
- Try With resource

	- Pro

		- Vermeiden von schachtelnden

	- Con

		- Aber andere reinholte

## Collection Framework

### 

- List

	- Eigenschaften

		- duplikate erlaubt
		- wahfrei durch Index

	- Nutzen

		- List x = new  Arraylist();
		- Mehoden
(nicht alle)

			- add();
			- remove();
			- sequenzieller Zugriff 
			- Contains();
			- IndexOf();

	- Aufbau

		- Enthält Objects
		- Linked list Datenstruktur
		- Iterator

			- Iterator x = MyList.iterator();
			- Pointer auf ein Aktives Element
			- Vorteile

				- während Iteration kann man elemente modifizieren

			- methoden

				- next();
				- remove();
				- add();

	- Arten

		- ArrayList

			- Liste klassisch

		- Vektor

			- Liste gut für multithreading
			- Syncronisiert

- Mengen

	- Eigenschaften

		- keine Duplikate
		- eigenständige Ordnung
		- Zugriff über iteratoren 
		- kein Wahlfreier Zugriff

	- Set

		- hash set

	- Sorted Set

		- Tree set

			- Eigne Klassen müssen Comparable Interface nutzen

- Map

	- Interface Map

		- immer Schlüssel werte paare
		- Eideutig

	- Arten

		- Treemap

			- keys kommen in treeset
			- gepaart mit value

		- Hashmap

	- Funktionen

		- put

			- (a,b)

		- key set
		- values
		- get
		- remove
		- size
		- clear

### Zuständig für

- Dynamisches Speichern von Objekten
- import java.util.x
- Smmlung von Klassen

### Generics

- Nutzen

	- <PLACEHOLDER>

		- Bei angebe wird es auf
angegebenen Typ Konkretisiert
		- typecast auf angegebenen typ auch Möglich
		- Wrapperklassen nutzen

	- <>

		- Behandlung wie Object

- Wrapperklasse

	- für alle elementaren Datentypen
	- datentyp in objekt kapselm

		- autoUnboxing

	- eigene Methoden

		- parse

### Relevante Interfaces

- Comparable Interface

	- Methode

		- CompareTo();
		- vergleich

			- <0

				- vor

			- =0

				- Gleich

			- >0

				- hinter

	- Sinn

		- Vergleichsoperation muss implementiert 
sein um eine reihenfolge möglich zu machen
		- Ordnungsrelation möglich machen
		- Vergleichsoperation wird auch zur überprüfung auf Dopplung genutzt

	- Sonst 

		- Class cast exception

	- Equals , compareTo, hashCode sollten sich konsistent verhalten

- eignene Comparator Klasse

	- implements Comparator<Typ>
	- methode

		- Compare
		- eigene Logik für eigenes Sortieren
		- Auch als Lambda funktion

	- Einsatz

		- set<> x = new Treeset<>(new *eigene sort klasse());
		- (geht auch mit Listen etc)

### equals()

- bei vergleich mit null muss false
- reflexiv
- symmetrisch
- transitiv
- konstistent
- dierekte subklasse

	- alias check

		- this == o

	- test null

		- o== null

	- instanzen der gleichen klasse?

		- this.getClass() != o.getClass()

	- Feldvergleich

		- 

- indierekte subklasse

	- alias check
	- delegation zur oberklassse

		- super.equals()

	- Feld Vergleich überprüft die Inhaltliche Gelichhetit der Subklasse

### hashCode()

- surjektive funktion
- bitverknüpung durch ^

	- bei long
	- (int)(field>>>32) ^(int)(field &0xFFFFFFFF

		- >>> bitshift

- field==null ? 0: field.hashCode()
- hash start

	- jede klasse anders

- hash multiplyer

	- primzahl die den hash start multipliziert

## Swing

### UI Implementierung

### Unterschiede und Gemeinsamkeiten zu AWT

- Awt

	- Heavyweight

		- schnell

	- Fenster aus betriebssystem nehmen
	- Peer klassen werden gesteuert
	- Klasse selbst ist betriebssystem spezifisch
	- Rendering AUS BETRIEBSSYSTEM

- SWING

	- lightweight

		- langsam

	- eigene Komponenten
	- mehr plattformunabhängigkeit
	- alle klassen fangen mit J an
	- Rendering AUS JAVA SELBST

- Swing und AWT

	- Main Takeaway:
Swing erbt aus AWT
+ eigene implementierung

abstraktion über component 
-> schachtelung

### Fenster

- Container
- Layout manager

### Listener Konzept

- event

	- event source 

		- wirft evet objekte

			- auslösen

		- Es wird immer ein Event ausgelöst wenn etws getan wird
		- immer das objekt mit dem das event passiert

	- arten

		- Action 
		- item

			- selectieren
			- deselectieren

		- Focus event

- listener

	- listener ist an bestimmten event regisstriert
	- ist interface mit welchen moethoden verabeitet wird

## IO Streams
(nr)

### Dateisystem

- Die Klasse File

	- räpräsentiert

		- Laufwerke
		- Verzeichnisse
		- Dateine

- Anzeigen der Laufwerke

	- Java IO Paket
	- ListRoots();

		- root. getpath()

			- wo ist es

		- root.canread

			- lesezugriff

		- root.canwrite

			- schreibzugriff

		- root.exists
		- root.isfile
		- root.isdirectory
		- root.listfiles

			- file[]

- vorgehensweisen

	- set systempropertieskeys  = systemproperties.keyset

		- informationen über die Umgebung in der Das Javaprogramm läuft

			- zb Fileseperator 
			- z.b. lineseperator
			- exists

				- nur anlegen wenn es das nicht schon gibt
				- löschen erst wenn es etwas gibt

			- Username
			- path
			- userdirectory = verzeichnis in dem das programm läuft != HOME verzeichnis
			- os version
			- native encoding
			- und viele mehr

	- umgang mit verzeichnissen und dateien

		- neue Dateien anlegen
		- löschen
		- umbenennen
		- Gucken ob noch da

### != Util Streams

- Stream= übertragung von daten von quelle in zeil
- unterschied

	- io hat xterne ressource

		- datei
		- netzs
		- datenbank

	- Util

		- Datenquellen

			- map
			- reduce
			- filter

		- funktionale prog
		- von collection -> zu collection

			- zwischendrin filtern

### arten

- buffered 
- unbuffered

### Schreiben und lesen Datei
(klausurrelavant weil Exception handling)

- Writer

	- .write

		- möchte string
		- schreibt alles hintereinader weg

			- \n
			- lineseperator

	- mögliche fehler

		- Schreiben
		- lesen
		- sonstige

	- blockiert solange datei wie wir sie benutzen

- Reader

	- File reader

		- mögliche fhler

			- io exception

		- Cloasable interface für try with ressource

			- damit man das verschachtelte finally nicht notwendig tist

		- Schleife zum lesen

## Datenstrukturen

### Elemenare Datentypen

### Objekte

### Listen

- Que

	- First in First out
	- Element kennt das element vor ihm
	- Operationen

		- Enque

			- Einketten "hinten"

		- Deque

			- Ausketten "vorn"

- Linked list

	- One way linked list

		- list

			- first node

		- node

			- value
			- next node

	- Two way linked list

		- List

			- First node
			- Last node

		- Node

			- Value
			- Next node
			- Previous node

- Stack

	- Last in First out
	- Element kennt darunterliegendes
	- Operationen

		- Push
		- Pop
		- Peek

	- Warum gut wenn als linked list implementiert

		- Komplex O(1)
		- Hinzufügen immer eine operation
		- "Aufrücken" ist atomatisch

### Bäume

- Knoten

	- Wurzel

		- Ursprung

	- Wenn knoten keine unterknoten mehr hat-> BLATT

- Vorraussetzung

	- Im baum definiert wie was einzuordnen ist
	- EINE transitiv gültige relation für gesamten baum

- Arten

	- Binärbaum

		- Node

			- Left
			- Data
			- Right

		- Spezial

			- maximal 2 Kanten pro node
			- Suche Komplexität von O(log(n))
			- Einfügen Komplexität von O(log(n))

		- Balancieren

	- AVL TREE

		- Adelson-velski landis
		- Eigenschaften

			- Balanciert sich selbst
			- Cs.usfca.edu

		- Balancieren

			- Differenz der Tiefe/Höhe der beiden Kinder mehr als 1
			- Rechts zu viel 

				- Linksrotation

			- Links zu viel 

				- Rechtsrotation

			- Rekursiv so tief runtergehen, dass man irgendwo die Differenz weg null Node hat

## Algorithmen

### Komplexität

- Laufzeit des alogrythmus
- "Eingabe von werten beeinflusst sich wiederholenden code"
- Wird relevant bei Dynamischen strukturen
- O-Notation

	- Vergleich von Algorythmus verhalten
(nur laufzeit)
	- Klassen

		- Linear

			- "Es passiert X* Etwas"

		- Logaritmisch

			- "Alle ver x Fachungen wird es um 1 höher"

		- Quadratisch

			- "Es passirt X*X*Etwas"

		- Exponential

			- "Es passiert Etwas mal selbst  x mal"

		- Faktoriell

	- Cases betrachtung

		- Best case
		- Average case
		- Worst case

	- Faktoren werden gestrichen => O(n/2) =O(n)

### traversion ( Bäume)

- pre order

	- Wurzel des einstiegs ausgeben
	- dann teilbaum LINKS
	- dann Teilbaum Rechts
	- wozu

		- neu generieren

- in order

	- links
	- root
	- rechts
	- wozu

		- ausgeben

- post order

	- Links 
rechts 
root
	- wozu

		- löschen/ invertieren
		- Wenn zu löschende kinder hat
=> Invertieren 
-> zu löschende nun keine kinder mehr

### Sortierung

- Bubblesort

	- so lange aufsteigen bis ein größerer dort ist
	- 
	- Struktogramm

		- Mit swap

	- implementierung
	- O(n**2)

- selection sort

	- größtes element suchen und nach hinten tun
	- 
	- Struktogramm

## Exkurse

### J Unit Tests

- Assert

	- Does throw
	- Does Not throw

- exeptions testen

	- test mit assertion

- @Test Annotation

### Innere Klassen

- Klassen Struktur
- Top level

	- Statisch
	- Sichbarkeit kann modifiziert werden

- element

	- nicht statisch
	- nur im Kontext eines Objekts der äußeren

- lokal

	- nur innerhalb von methoden

- anonym

	- ohne Bezeichner
	- referenz
	- #

### Labmda funktionen

- Funktionales Interface einer Methode
- zugriff auf umliegenden Kontext

### Fenster grössen

- Virtueller bildschirm enthält alle bildschirme
- Koordinaten
- Default screen device.getDEFAULTconfigutation().getbounds

	- Getwitdth()
	- Get height()

- Get displaymode
- Graphics device 

	- Graphics enviroment,getlocalgraphicsenviroment

- Virtual graphics env.getScreen []

### Serialisieren von objekten

- Problem

	- manche datenstrukturen sind keine Reihen ( zb listen) sonder haben tiefe 
	- aufschreiben ist aber eine Reihe

- Wo

	- Bäume
	- Graphen

- Was

	- definierte reihenfolge

		- man wies wie man es geschrieben hat
		- das ganze wieder einlesen und dann objekt erzeugen

- Beispiel

	- Personen objekt

		- name: klaus
		- alter: 27

	- csv variante

		- serialize();

			- person.file=
klaus;27
peter;46

		- json

			- taggen

		- xml

			- taggen

- wie 

	- serializable interface

		- java macht das automatisch
		- id sollte man final setzen
		- ein stream der schreibt 

		- ein stream der die objekte seriealisiert und den anderen stram bekommt

- transien modifier

	- redundatnte daten ausschließen
	- persistentens nicht gefährdet

