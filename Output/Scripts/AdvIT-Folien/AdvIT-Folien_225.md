f.write ( index, data ); // k.A.
w.release();
} // write
public int read ( int index, byte[] data ) throws InterruptedException  {
mutex.acquire();

   Tags & Topics:
   