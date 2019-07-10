import java.util.Scanner;
import java.io.*;

public class Cub{
    public static void main(String[] args) {
        double n,mul,m=3;
        Scanner sc=new Scanner(System.in);
        System.out.println("enter no:");
         n=sc.nextInt();
         mul=Math.pow(n,m);
        System.out.println("Cube is:"+mul);
    }
}