import java.util.Scanner;
public class Oddn{
    public static void main(String[] args) {
        int i,n;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number upto which u want odd no");
        n=sc.nextInt();
        for(i=1;i<=n;i++){
            if(i%2 !=0){
                System.out.println("odd number is:"+ i);
            }
        }
        sc.close();
        
        
    }
}