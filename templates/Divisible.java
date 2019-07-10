import java.util.Scanner;
class Divisible{
    public static void main(String[] args) {
        int n;
        Scanner sc=new Scanner(System.in);
        System.out.println("enter number:");
        n=sc.nextInt();
        if(n%11==0){
            System.out.println(n +" is Divisible by 11");
        }
        else{
            System.out.println(n +" is Not divisble by 11");
        }
    }

}