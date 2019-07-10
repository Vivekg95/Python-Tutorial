import java.util.Scanner;
public class Revers{
    public static void main(String[] args){
        int a,b,sum=0,i=0;
        Scanner s=new Scanner(System.in);
        System.out.println("enter no");
        a=s.nextInt();

        while(a>0){
            b=a%10;
            a=a/10;
            sum=sum+b;
            System.out.println("number is"+b);
        

        }
        System.out.println("sum is"+sum);
    }
}