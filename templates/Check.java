import java.util.Scanner;
public class Check
{ 
    public static void main(String[] args)
     {
         int n,m=0,sum=0;
         Scanner s=new Scanner(System.in);
         System.out.print("enter number");
         n=s.nextInt();
         while(n>0){

         
         m=n%10;
         sum=sum+m;
         n=n/10;
         }
         System.out.println("sum of number is:"+sum);
         



        
    }

}