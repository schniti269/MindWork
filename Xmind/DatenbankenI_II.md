# Datenbanken I+II

## Grundlagen 
Datenbank

### Struktur

- Aufbau
- Begriffe

	- DB

		- Speicherung und Organisation von Daten.

	- DBS

		- Funktionen

			- Bietet Tools und Funktionen, um Datenbanken zu verwalten. 
			- Durchführen der CRUD Operationen
			- Bereitstellen von Backup- und 

	- DMBS

		- Beschreibt das Gesamtsystem, das die Daten (DB), das Managementsystem (DBMS), und die Hardware, auf der das DBMS und die Datenbank ausgeführt werden beinhaltet

### Operationen

- CRUD

	- Create
	- Read
	- Subtopic 3

### Architektur

- Ansi Sparc3

	- Ebenen Modell
	- Regeln

		- Änderungen an einer Ebene keine Auswirkung auf die nächste

## Modelle

### Entity Relationship Model
(ERM)

- kardinalitäten
- Entitäten
- Relationen

	- Kopfkomponente

		- Eindeutige Namen der Relation und Attribute 
		- "Header"

	- Körperkomponente

		- Tupel über  unterschiedliche Wertebereiche (Domäne)
		- "value"

	- Regeln

		- in einer Relation müssen Tupel Eindeutig sein

	- Relationen und tabellen sind gleich

### Begriffe

- Tupel

	- Besteht aus mehreren Werten
	- Werte in der selben Domäne immer gleiche Reihenfolge

- Domäne

	- Wertebereich für ein Attribut
	- Integer, String, Double

- Schlüssel

	- Unterstrichenes attribut
	- eideutig
	- dient zur identifikation
	- Natural/Surogate

		- natural= Buisness relavant-> auch Kundennummer
		- Surogate (künstlich): nur für Technische Funktion der Datenbank IDR Femdschlüssel

	- Arten

		- Fremdschlüssel

			- "link"
			- Schlüssel aus anderer Tabelle

		- Primärschlüssel

			- ein Ausgesuchter Primärschlüssel

		- Kandidaten Schlüssel

			- "rausstreichen"
bei erhalt von Funktionale Abhängigkeit

		- Superschlüssel

			- Menge die funktional Abhängig ist

- Funktionale Abhängigkeit
- Attribute

	- Werte

## Relationsoperationen

### Vereinigung

- Tabellen Vereinigen alles was doppelt wäre ist dennoch nur einzeln
- U

### Differenz

- -
- Schnittmenge wird aus Ausgangsmenge abgezogen

### Schnitt

- Nur wenn in beiden

### Projektion

- neue Tabelle aus alter wird erzeugt
mit ausgewählten spalten

### Aggregation

- Zusammenfassung
- idr numerisch

### KarthesischesProdukt

- Alle mit allem Verlinke
- Es werdeb zwangsläufig unechte tupel erzeugt
- Diese werden ausgefiltert
- in verknüpfung mit selektion -> Join= auflösen einer Fremdschlüsselbeziehung

## Joins

### inner

- Cross

	- Karthesisches Produkt

- Theta

	- Cross join mit filter 

- Natural

	- nur wenn beide Tabellen gleichnamige Attribute
	- Filter sind automatisch

		- Cross vs Natural
		- Aus erster Tabelle wird attribut genutzt

### Outer

- Left

	- Alle wo es Fremdschlüssel gibt wird ausgefüllt
	- Alles andere Null
	- Carl ist da aber kurs NULL

- Right

	- Selbes wie LEft nur reihenfolge anders
	- Carl taucht nicht auf weil kein kurs
	- Kurse ohne studenten

- Full

	- Beides wird kombiniert und "quasi" über eine vereinigung vermengt

- Vergleich

