import java.util.Scanner;
public class Power{
    public static void main(String[] args) {
        double i ;
         int n;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number upto which u want odd no");
        n=sc.nextInt();
        i=Math.pow(n, 2);
        
        System.out.println("odd number is:"+ i);
            
        
        sc.close();
        
        
    }
} 