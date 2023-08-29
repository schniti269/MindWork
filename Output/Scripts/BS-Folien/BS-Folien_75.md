⋄erzeugen eines identischen Kind-Prozesses
⋄R¨uckgabewert pid == 0 im Kind-Prozess, neue PID sonst
pid = waitpid (pid, &statloc, options)
⋄warten bis Kind-Prozess zu Ende ist
⋄irgendein Kind: pid = –1, statlocenth¨alt exit-Status

   Tags & Topics:
   #Kind-Prozess
   #kind
   #Kind

[Previous: #BS-Folien_76](BS-Folien_76.md)

[Next: #BS-Folien_76](BS-Folien_76.md)