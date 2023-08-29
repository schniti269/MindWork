//Austrittsprotokoll aus dem kritischen Abschnitt
public static void exitMutex ( GlobalVariable busy ) {
busy.value = false;
}
} // MutualExclusion

   Tags & Topics:
   