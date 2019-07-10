import java.util.Scanner;
public class Even{
    public static void main(String[] args) {
        int i,n;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter number");
        n=sc.nextInt();
        for(i=1;i<=n;i++){
            if(i%2==0){
                System.out.print("\t"+i);
            }
        }
    }
}