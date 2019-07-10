import java.util.Scanner;
public class Multiplication{
    public static void main(String[] args) {
        int i,n,table=0;
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the number whose table you want: ");
        n=sc.nextInt();
        for(i=1;i<=10;i++){
            table=n*i;
            System.out.println(n +"*"+ i+"="+table);
        }
        sc.close();
        
       


    }
}