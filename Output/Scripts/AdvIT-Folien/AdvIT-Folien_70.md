Dispatcher-Code: Worker-Code:
while (TRUE) { while (TRUE) {
get_next_ request(&buf); wait_for_work(&buf)
handoff _work(&buf); look_for_ page _in_cache(&buf, &page);
} if(page _not_in_ cache(&page))

   Tags & Topics:
   #Code
   #Worker-Code