int i = Float . floatToIntBits ( y ); // i = * ( long * ) &y;
return ( float )( i >> 23 ) - 127;
}
Der Fehler ist dann genau der unbekannte aber kleine Wert (in der Regel ist 0≤δ <1) des Logarithmus
der Mantisse. Dank der Logarithmengesetze aus Satz 1.8 können Funktionen wie r(a) =1√a=a−1/2

   Tags & Topics:
   #floatToIntBits
   #Float

[Previous: #Analysis-Lineare_Algebra-230308_626](Analysis-Lineare_Algebra-230308_626.md)

[Next: #Analysis-Lineare_Algebra-230308_626](Analysis-Lineare_Algebra-230308_626.md)