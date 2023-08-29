i = 0 x5f3759df - ( i >> 1 ); // what the fuck ?
y = * ( float * ) &i;
y = y * ( threehalfs - ( x2 * y * y ) ); // 1st iteration
// y = y * ( threehalfs - ( x2 * y * y ) ); // 2nd iteration , this can be removed
return y;

   Tags & Topics:
   

[Previous: #Analysis-Lineare_Algebra-230308_607](Analysis-Lineare_Algebra-230308_607.md)

[Next: #Analysis-Lineare_Algebra-230308_607](Analysis-Lineare_Algebra-230308_607.md)