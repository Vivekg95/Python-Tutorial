import java.util.Scanner;
public class PL{
    public static void main(String[] args) {
        float Profit,Loss,Sp,Cp;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the Cost Price");
        Cp=sc.nextFloat();
        System.out.println("Enter the Selling Price");
        Sp=sc.nextFloat();
        if(Sp>Cp){
            Profit=Sp-Cp;
            System.out.println("Profit is:"+Profit);
        }
        else{
            Loss=Cp-Sp;
            System.out.println("loss is:"+Loss);
        }
        
            
        
        sc.close();
        
        
    }
} 