    if (args.length  > 0) {host = args[0];}
    for (int i = 1; i < 1024; i++) {      try {
        Socket s = new Socket(host,  i);        System.out.println(
         ”There  is a server on port ” + i + ” at ” + host);        s.close();      }
      catch (UnknownHostException  e) {        System.err.println(e);

   Tags & Topics:
   #Ther
   #System.err.println(e
   #Socket(host