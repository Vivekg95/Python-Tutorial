import java.util.Scanner;
public class Biggest{
    public static void main(String[] args){
        int a, b,c;
        Scanner s=new Scanner(System.in);
        System.out.println("enter number");
        a=s.nextInt();
        System.out.println("enter second  number");
        b=s.nextInt();
        System.out.println("enter third number");
        c=s.nextInt();
        if(a>b & a>c){
            System.out.println("largest number is:"+a);
        }
        else if (b>a & b>c) {
            System.out.println("largest is:"+b);
            
        } else {
            System.out.println("largest is "+c);
            
        }
            
        }


    }

