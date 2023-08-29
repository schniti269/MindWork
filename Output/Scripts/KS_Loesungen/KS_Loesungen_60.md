for (int j=0; j<DIM; j++)
if ((E[j] != 0) && (C[a][j] > 0))
if ((cost[a] + C[a][j]) < cost[j]) {
cost[j] = cost[a] + C[a][j];
pre[j] = a;

   Tags & Topics:
   #C[a][j

[Previous: #KS_Loesungen_61](KS_Loesungen_61.md)

[Next: #KS_Loesungen_61](KS_Loesungen_61.md)