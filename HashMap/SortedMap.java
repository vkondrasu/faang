import java.util.*;
import java.io.*;
import java.lang.*;

public class SortedMap {

   public static void main(String args[]) {
      // Create a hash map
      TreeMap<Integer, Integer> tm = new TreeMap<>();
      
      // Put elements to the map
      tm.put(73,0);
      tm.put(74,1);
      tm.put(75,2);
      tm.put(71,3);
      tm.put(69,4);
      tm.put(72,5);
      tm.put(76,6);
      tm.put(73,7);

      

      tm.remove(73);

      tm.put(70,8);

      for(Map.Entry me : tm.entrySet()){

        System.out.print(me.getKey() + ": ");
        System.out.println(me.getValue());

      }

      System.out.println();
      
      
   }
}