import java.util.*;

public class Practise10 {
   public static void main(String[] args) {

      // create a new hashtable
      Dictionary d = new Hashtable();

      // add some elements
      d.put("1", "Chocolate");
      d.put("2", "Cocoa");
      d.put("5", "Coffee");

      // return an enumeration of the keys from this dictionary.
      for (Enumeration e = d.keys(); e.hasMoreElements();) {
         System.out.println(e.nextElement());
      }
   }
}