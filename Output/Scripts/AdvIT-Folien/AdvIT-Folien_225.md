f.write ( index, data ); // k.A.
w.release();
} // write
public int read ( int index, byte[] data ) throws InterruptedException  {
mutex.acquire();

   Tags & Topics:
   

[Previous: #AdvIT-Folien_226](AdvIT-Folien_226.md)

[Next: #AdvIT-Folien_226](AdvIT-Folien_226.md)