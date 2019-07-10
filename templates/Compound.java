import java.io.*;
public class Compound{
    public static void main(String[] args) {
        double principal=1200,rate=5,time=2;
        double CI=principal*(Math.pow((1+rate/100),time));
        System.out.println("compound interset is:" + CI);
    }
}