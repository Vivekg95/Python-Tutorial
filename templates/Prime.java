import java.util.Scanner;
public class Prime{
    public static void main(String[] args){
        int i,n,count=0;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number:");
        n=sc.nextInt();
        
        for(i=1;i<=n;i++){
            if(n%i==0){
                count=count+1;
            }
            
        }
        if(count==2){
            System.out.println(n +" is prime");
        }
        else{
            System.out.println(n +" is not prime");
        }
        sc.close();
    }
    
}

/*package com.instanceofjava;
 
public class PrintMessage {

public static void main(String[] args) throws IOException{
 
       System.out.write("Hello World".getBytes());
}
}*/