import java.util.Scanner;
public class PN{
    public static void main(String[] args) {
        double n;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number");
        n=sc.nextDouble();
        
            if(n>0){
                System.out.println("number is positive:"+ n);
            }
            else{
                System.out.println("number is negative:"+ n);

            }
        
        sc.close();
        
        
    }
}