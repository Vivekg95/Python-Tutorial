import java.util.Scanner;
public class Multiply{
    public static void main(String[]args){
        int n;
        Scanner sb = new Scanner(System.in);
        System.out.println("enter a number:");
        n=sb.nextInt();
        if(n%2==0){
            System.out.println("It Is even");
        }
        else{
            System.out.println("Number is odd");
        }
    }
}