import java.io.*;
import java.util.Date;
public class DaytimeServer  {  public ﬁnal static int DEFAULT PORT = 13;  public static void main(String[]  args) {    int port = DEFAULT PORT;    PrintWriter  out = null;    Socket connection  = null;    try {     ServerSocket  server = new ServerSocket(port);     while (true) {       try {         connection  = server.accept();         out = new PrintWriter(connection.getOutputStream());         Date now = new Date();         out.println(now.toString());         out.ﬂush();       } catch (IOException  e) {e.printStackTrace(); }       ﬁnally {         try {           if (connection  != null) connection.close();         } catch (IOException  e) {}       } // end ﬁnally     }  // end while   } catch (IOException  e) {     System.err.println(e);   } // end catch  } // end main
} // end DaytimeServer
Prof. Dr. Henning Pagnia (DHBW Mannheim) Advanced IT Herbst 2023 123/132Server-Programmierung Sockets in Java

   Tags & Topics:
   #ServerSocket
   #123/132Server
   #serversocket(port
   #System.err.println(e
   #main(string
   #Date
   #out.println(now.toString

[Previous: #AdvIT-Folien_377](AdvIT-Folien_377.md)

[Next: #AdvIT-Folien_377](AdvIT-Folien_377.md)