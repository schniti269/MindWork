public class EchoClient  {  public static ﬁnal int serverPort  = 7; // echo server
  public static void main(String[]  args) {    // declare variables ﬁrst    String hostname  = ”localhost”;    PrintWriter  networkOut  = null;    BuﬀeredReader  networkIn  = null;    Socket s = null;    try {      s = new Socket(hostname,  serverPort);      System.out.println(”Connected  to echo server”);      networkIn  = new BuﬀeredReader(  new InputStreamReader(s.getInputStream()));      BuﬀeredReader  userIn = new BuﬀeredReader(  new InputStreamReader(System.in));      networkOut  = new PrintWriter(s.getOutputStream());
      // now do the real things:      while (true) {        String theLine = userIn.readLine();        if (theLine.equals(”.”))  break;        networkOut.println(theLine);        networkOut.ﬂush();        System.out.println(networkIn.readLine());      } // end while
    } catch (IOException  e) {      System.err.println(e);    } ﬁnally {      try {        if (s != null)  s.close();      } catch (IOException  e) {}    } // ﬁnally  }  // end main
}  // end EchoClient

   Tags & Topics:
   #InputStreamReader(s.getInputStream
   #System.err.println(e
   #serverport
   #System.out.println(networkIn.readLine
   #networkOut.ﬂush
   #networkOut.println(theLine
   #EchoClient
   #s.getInputStream
   #main(string
   #InputStreamReader(System.in