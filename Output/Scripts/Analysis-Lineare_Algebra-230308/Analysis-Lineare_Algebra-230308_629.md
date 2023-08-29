Zahlen hinweg ein wenig besser, wenn eine leicht kleinere Konstante wie 0x5f3759df verwendet wird.
Die anschließende Newton-Iteration kann in Java nach einer der beiden Newton-Verfahren so aussehen:
static float newtonStep ( float a, float y)
{
return y * ( 1.5f - a / 2 * y * y ); // y * ( threehalfs - ( x2 * y * y ) );

   Tags & Topics:
   #Iteration
   #Newton-Iteration
   #Newton