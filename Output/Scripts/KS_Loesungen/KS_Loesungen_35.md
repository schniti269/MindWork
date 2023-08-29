// compute checksum
for(intj = 0; j <= (frame . length −generator . length ); j++)
if(frame [ j ] != 0) // else result = 0 −>continue
for(inti = 0; i <generator . length ; i++)
frame [ i+j ] = frame [ i+j ] ˆ generator [ i ]; // XOR

   Tags & Topics:
   

[Previous: #KS_Loesungen_36](KS_Loesungen_36.md)

[Next: #KS_Loesungen_36](KS_Loesungen_36.md)