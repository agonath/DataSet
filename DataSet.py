# -*- coding: utf-8 -*-

from copy import deepcopy
from builtins import int

#
# Simple Dataset Object, 2-Dimensional.
#
class DATASET(object):
	
	__slots__= ['__data', '__rowTitles', '__colTitles', '__numRows', '__numCols'];

	def __init__(self, _cols=int(0), _rows=int(0)):
		
		self.__data = []; # 2 Dimensionales Array
		self.__colTitles = [];
		self.__rowTitles = [];
		self.__numCols = _cols;
		self.__numRows = _rows;
		
		#__data initialisieren
		if((_cols > 0) and (_rows > 0)):
			for row in range(0, _rows):
				
				self.__data.append([]); #neue Zeile hinzufügen (Array)
				
				for col in range(0, _cols):
					self.__data[row].append(None); #neue Spalte hinzufügen, Werte im Array
				#end for col
			#end for row
			
		#Die Title Arrays initialisieren
		for i in range(0, _rows):
			self.__rowTitles.append(None);
		
		for i in range(0, _cols):
			self.__colTitles.append(None);
	#end __init__


	#STR Funktion für DATASET Objekte, gibt Dataset als reinen String zurück.
	def __str__(self):
		result = "";
		for row in self.__data:
			for col in range(0, len(row)):
				result += "|\t";
				result += str(row[col]);
				result += "\t";
			#end for col
			result += "|\n";
		#end for row
		return result;
	#end __str__
	
	
	#Dataset mit Titel als String zurückgeben. (wie STR(...))
	def stringWithTitles(self):
		result = "";
		rowCounter = 0; #counter
		
		#Abstand bis zur ersten Spalte überbrücken
		result += "\t";
		
		#Spaltentitel zuerst anhängen...
		for i in range(0, self.__numCols):
			if(self.__colTitles[i] == None):
				result += "\t\t";
			else:
				result += "   " + self.__colTitles[i] + "\t";
		
		# neue Zeile
		result += "\n";
		
		#Werte für die Zeilen und Spalten ausgeben.
		#Inkl. Zeilentitel.
		for row in self.__data:
			
			#Zeilentitel anhängen, nur wenn nicht <None>
			if(None != self.__rowTitles[rowCounter]):
				result += str(self.__rowTitles[rowCounter]) + "\t";
			else:
				result += "\t";
			rowCounter += 1;
			
			for col in range(0, len(row)):
				result += "|\t";
				result += str(row[col]);
				result += "\t";
			#end for col
			result += "|\n";
		#end for row
		return result;
	#end stringWithTitles


	# Inhalt über den Index setzen. (z.B.: test[0][3] = 4.5)
	def __setitem__(self, _idx, _value):
		try:
			self.__data[_idx] = _value;
		except(IndexError):
			print("Index is out of range! --> " + str(_idx));
			raise;
	#end __setItem__


	# Inhalt über den Index lesen. (z.B.: test = dataset[0][3])
	def __getitem__(self, _idx):
		try:
			return self.__data[_idx];
		except(IndexError):
			print("Index is out of range! --> " + str(_idx));
			raise;
	#end __getItem__
	
	#Anzahl Zeilen zurückliefern
	def getRowCount(self):
		return self.__numRows;
	
	#Anzahl Spalten zurückliefern
	def getColCount(self):
		return self.__numCols;
	
	# Eine bestimmte Zeile zurückliefern.
	def getRow(self, _rowIndex):
		
		try:
			return deepcopy(self.__data[_rowIndex]);
		except(IndexError):
			print("Index is out of range! --> " + str(_rowIndex));
			raise;
	#end getRow
	
	
	# Eine bestimmte Spalte zurückliefern
	def getCol(self, _colIndex):
		
		try:
			result = [];
			
			for row in self.__data:
				result.append(row[_colIndex]);
			
			return result;
		except(IndexError):
			print("Index is out of range! --> " + str(_colIndex));
			raise;
	#end getCol
	
	#Eine Zeile benennen
	def setRowTitle(self, _rowIndex, _title):
		try:
			self.__rowTitles[_rowIndex] = _title;
		except(IndexError):
			print("Index is out of range! --> " + str(_rowIndex));
			raise;
	#end setRowTitle
	
	#Eine Spalte benennen
	def setColTitle(self, _colIndex, _title):
		try:
			self.__colTitles[_colIndex] = _title;
		except(IndexError):
			print("Index is out of range! --> " + str(_colIndex));
			raise;
	#end setColTitle
	
	#Fügt eine neue Zeile vor dem angegebenen Index oder am Ende ein.
	#Inkl. Titel.
	#Index = -1 --> Zeile wird am Ende hinzugefügt
	def addRow(self, _rowIndex=-1):
		try:
			#Anzahl Zeilen
			self.__numRows += 1;
			
			if(_rowIndex < 0):
				self.__data.append([]);
				self.__rowTitles.append(None);
				
				#Spalten der neuen Zeile mit Standardwert <None> füllen
				# Index von -1 (_rowIndex) würde auch funktionieren, das hier ist aber klarer
				for col in range(0, self.__numCols):
					self.__data[self.__numRows-1].append(None);
				
			else:
				self.__data.insert(_rowIndex, []);
				self.__rowTitles.insert(_rowIndex, None);
				
				#Spalten der neuen Zeile mit Standardwert <None> füllen
				for col in range(0, self.__numCols):
					self.__data[_rowIndex].append(None);
				
		except(IndexError):
			raise(IndexError);
	#end addRow
	
	#Fügt eine Spalte vor dem angegebenen Index oder an das Ende ein.
	#Inkl. Titel.
	#Index = -1 --> Spalte wird am Ende hinzugefügt
	def addCol(self, _colIndex=-1):
		#Python Bug kompensieren...Python fügt bei einem ungültigen, positiven
		#Index für die Funktion "insert" den Wert einfach am Ende der Liste ein.
		if(_colIndex > (self.__numCols-1)):
			raise(IndexError);
			return;
		try:
			#Anzahl Spalten
			self.__numCols += 1;
			
			#negativer Index --> Ende der Liste
			if(_colIndex < 0):
				self.__colTitles.append(None);
				for row in self.__data:
					row.append(None);
			else:
				#sonst vor dem angegebenen Index einfügen
				self.__colTitles.insert(_colIndex, None);
				for row in self.__data:
					row.insert(_colIndex, None);
				
		except(IndexError):
			raise(IndexError);
	#end addCol
	
	#Entfernt die Zeile <n> aus dem Dataset.
	#Inkl. Titel.
	#Index = -1  --> letzte Zeile wird entfernt
	def delRow(self, _rowIndex=-1):
		try:
			#Anzahl Zeilen
			self.__numRows -= 1;
			
			# -1 --> letzte Zeile löschen
			if(_rowIndex == -1):
				self.__rowTitles.pop();
				self.__data.pop();
			else:
				self.__rowTitles.pop(_rowIndex);
				self.__data.pop(_rowIndex);
		except(IndexError):
			raise(IndexError);
	#end delRow
	
	#Entfernt die Spalte <n> aus dem Dataset.
	#Inkl. Titel.
	# Index = -1  --> letzte Spalte wird entfernt
	def delCol(self, _colIndex=-1):
		try:
			#Anzahl Spalten
			self.__numCols -= 1;
			
			if(_colIndex == -1):
				self.__colTitles.pop();
				for row in self.__data:
					row.pop();
			else:
				self.__colTitles.pop(_colIndex);
				for row in self.__data:
					row.pop(_colIndex);
		except(IndexError):
			raise(IndexError);
	#end delCol
	
	#Returns a CSV compatible String of the Dataset
	def getCSVString(self, _delimiter=","):
		result = "";
		
		#Titles
		for value in range(0, self.__numCols):
			
			result += str(self.__colTitles[value]);
			
			if (value < self.__numCols-1): #don't add the delimiter after last value
				result += _delimiter;
		
		result += "\n"; #new line after title, remove last delimiter
		
		#Rows
		for row in self.__data:
			
			for value in range(0, self.__numCols):
				
				result += str(row[value]);
				
				if(value < self.__numCols-1): #don't add the delimiter after last Value
					result += _delimiter;
			
			# new line after every row
			result += "\n";
		
		return result;
	#end getCSVString
	
	
	#Returns a HTML string of the dataset. (complete HTML)
	#Optional with titels and a custom stylesheet.
	#The "_stylesheet" parameter is the name or path + name of the stylesheet.
	def getHTMLString(self, _colTitles=False, _rowTitles=False, _stylesheet=""):
		
		result = "";
		rowTitleCounter = 0; #used if _rowTitle=True
		
		#write HTML head code...
		result="<!DOCTYPE html>\n";
		result += "<HTML>\n<HEAD>\n<link rel=\"stylesheet\" href=\"" + _stylesheet +\
		       "\">\n</HEAD>\n<BODY>\n<table id=\"table\">\n";
		
		#Spaltenname schreiben, in eigener Tabellenzeile
		if(True == _colTitles):
			
			#Zuerst eine neue Zeile beginnen und eine Leere Spalte hinzufügen.
			#Sonst stimmen die Spalten Titel nicht mit dem Inhalt überein.
			result += "<TR>\n<TD></TD>\n";
			
			#Jetzt den Rest hinzufügen.
			#Titel nur, wenn ungleich "None".
			for title in self.__colTitles:
				result += "<TD>" + str(title if(title!=None) else "") + "</TD>\n"; 
			
			#Tabellenzeile schließen	
			result += "</TR>\n";
		#end if
		
		
		#Tabelle mit Inhalt füllen...
		#Zeilenweise
		for row in self.__data:
			
			result += "<TR>\n";
			
			#wenn _rowTitles == True dann eine Spalte vorher einfügen
			#Zeilen-Titel einfügen, nur wenn ungleich "None".
			if(True == _rowTitles):
				if(rowTitleCounter < self.__numRows):
					result += "<TD>"
					result += str(self.__rowTitles[rowTitleCounter] if(self.__rowTitles[rowTitleCounter] != None) else "");
					result += "</TD>\n";
				#Counter für Zeilen-Titelnamen erhöhen
				rowTitleCounter += 1;
			#end if
			
			for col in range(0, self.__numCols):
				result += "<TD>";
				result += str(row[col]);
				result += "</TD>\n";
			#Zeile schließen
			result += "</TR>\n";
		
		
		#write HTML footer...
		result += "</table>\n</body>\n</HTML>";
		return result;
	#end getHTMLString
	
#end class DATASET





def main():
	
	#Testing the module if called directly...
	
	#Create test object 
	print("Create Dataset Object.");
	testobject = DATASET(3,5);
	assert(testobject!=None);
	print("--> OK\n");
	
	#Set up value in test object using the index operator.	
	try:
		testobject[4][2] = 50;
	except Exception:
		raise Exception;
	
	#Read and print a value.
	print("Wert von [3][2]: " + str(testobject[3][2]));
	print("\n");
	
	#Print the whole object.
	print("Das gesamte Dataset Objekt: \n");
	print(testobject);
	print("\n");
	
	#Test function "getRow"
	print("Lese eine Zeile aus dem Dataset.")
	Zeile = testobject.getRow(4);
	assert(Zeile != None);
	print("Gelesene Zeile: " + str(Zeile));
	assert(id(testobject[4]) != id(Zeile));
	print("ID der Zeile im Dataset: " + str(id(testobject[4])));
	print("ID der gelesenen Zeile: " + str(id(Zeile)));
	print("\n");
	
	#Test function "getCol"
	print("Lese eine Spalte aus dem Dataset.")
	Spalte = testobject.getCol(2);
	assert(Spalte != None);
	print("Gelesene Spalte: " + str(Spalte));
	assert(id(testobject[2]) != id(Spalte));
	print("ID der gelesenen Spalte: " + str(id(Spalte)));
	print("\n");
	
	#Test function "setRowTitle"
	testobject.setRowTitle(3, "Zeile 4");
	testobject.setRowTitle(4, "Zeile 5");
	
	#Teste Funktion "setColTitle"
	testobject.setColTitle(0, "Spalte 1");
	testobject.setColTitle(1, "Spalte 2");
	testobject.setColTitle(2, "Spalte 3");
	
	#Test function "stringWithTiles"
	print("Das gesamte Dataset Objekt mit Titel:\n");
	print(testobject.stringWithTitles());
	
	#Test function "addRow"
	old = testobject.getRowCount();
	print("Zeilen: " + str(testobject.getRowCount()) + ".");
	print("Eine Zeile zwischen 4 und 5 hinzufügen....");
	testobject.addRow(4);
	new = testobject.getRowCount();
	assert(old < new and (old+1) == new);
	print("Zeilen: " + str(testobject.getRowCount()) + ".\n");
	print(testobject.stringWithTitles());
	
	#Test function "addCol"
	old = testobject.getColCount();
	print("Spalten: " + str(testobject.getColCount()) + ".");
	print("Eine Spalte zwischen der ersten und zweiten Spalte hinzufügen....");
	testobject.addCol(1);
	new = testobject.getColCount();
	assert(old < new and (old+1) == new);
	print("Spalten: " + str(testobject.getColCount()) + ".\n");
	print(testobject.stringWithTitles());
	
	#Test function "delRow"
	old = testobject.getRowCount();
	print("Zeilen: " + str(old) + ".");
	print("Die Zeile Nr. 5 (zwischen 'Zeile 4' und 'Zeile 5') entfernen....");
	testobject.delRow(4);
	new = testobject.getRowCount();
	assert(old > new and (old-1) == new);
	print("Zeilen: " + str(new) + ".\n");
	print(testobject.stringWithTitles());
	
	#Test function "delCol"
	old = testobject.getColCount();
	print("Spalten: " + str(old) + ".");
	print("Die Spalte Nr. 2 (zwischen 1 und 3, unbeschriftet) entfernen....");
	testobject.delCol(1);
	new = testobject.getColCount();
	assert(old > new and (old-1) == new);
	print("Spalten: " + str(new) + ".\n");
	print(testobject.stringWithTitles());
	
	#Test function "getCSVString"
	print("Generate a CSV string for export.\n");
	print(testobject.getCSVString());
	
	#Test function "getHTMLString"
	print("Generate a HTML string for export.\n");
	print(testobject.getHTMLString(_colTitles=True, _rowTitles=True));
	

if __name__ == "__main__":
	main();
