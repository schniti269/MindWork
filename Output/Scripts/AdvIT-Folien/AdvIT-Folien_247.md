writecount wird von mehreren Schreibern verwendet
⇒mutex2erforderlich
Verwendung des Semaphors r, damit sich Schreiber anmelden k ¨onnen:
◮falls ein Schreiber angemeldet ist und Leser noch aktiv sind , werden weitere
Leser vor rblockiert, damit sie nicht readcount erh¨ohen k¨onnen

   Tags & Topics:
   

[Previous: #AdvIT-Folien_248](AdvIT-Folien_248.md)

[Next: #AdvIT-Folien_248](AdvIT-Folien_248.md)