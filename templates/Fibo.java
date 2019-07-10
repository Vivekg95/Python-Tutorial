import java.util.Scanner;
public class Fibo{
    public static void main(String[] args){
        int i,n,t1=0,t2=1,next_term;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number of terms:");
        n=sc.nextInt();
        System.out.println("fibonacci is:");
        for(i=1;i<=n;i++){
            System.out.print(t1);
            next_term=t1+t2;
            t1=t2;
            t2=next_term;
        }
        sc.close();
    }
    
}