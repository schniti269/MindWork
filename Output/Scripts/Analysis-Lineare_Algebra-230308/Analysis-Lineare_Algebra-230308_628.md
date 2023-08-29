int i = Float . floatToIntBits ( y ); // i = * ( long * ) &y;
i = ( (127 < <23) + (127 < <22) ) - i / 2; // i = 0 x5f400000 - ( i >> 1 );
return Float . intBitsToFloat ( i ); // y = * ( float * ) &i;
}
Da nun δin der Regel einen Wert zwischen 0und1besitzt, wird die Approximation im Schnitt über alle

   Tags & Topics:
   #floatToIntBits