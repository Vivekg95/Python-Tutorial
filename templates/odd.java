import java.util.Scanner;
class Odd
{
	public static void main(String args[])
	{
        int n,count1=0,count2 = 0;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number:");
        n=sc.nextInt();
		for(int i = 1;i <=n;i++)
		{
			if(i%2 == 0)
			{
				count1=count1+1;
            }
            else{
                count2=count2+1;
            }
		}
        System.out.println("The Count Of even Numbers are:" + count1);
        System.out.println("The Count Of odd Numbers are:" + count2);
	}
}