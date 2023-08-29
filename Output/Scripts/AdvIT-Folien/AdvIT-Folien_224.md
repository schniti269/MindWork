public LS ( File f ) {
this.f = f;
}
public void write ( int index, byte[] data ) throws InterruptedException  {
w.acquire();

   Tags & Topics:
   