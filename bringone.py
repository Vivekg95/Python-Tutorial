def main():
    a  =input("Enter the number").split()
    if (a==1):
        return 0
    elif(a%2==0 ):
        return 1 + list.count(a/2)
    else:
        return 1+ min(list.count(a-1),list.count(a+1))

if __name__=="__main__":main()



''' #// CPP program to count minimum 
// steps to reduce a number 
#include <iostream> 
#include <cmath> 

using namespace std; 

int countways(int n) 
{ 
	if (n == 1) 
		return 0; 
	else if (n % 2 == 0) 
		return 1 + countways(n / 2); 
	else
		return 1 + min(countways(n - 1), 
					countways(n + 1)); 
} 

// Driver code 
int main() 
{ 
	int n = 15; 

	cout << countways(n)<< "\n"; 

	return 0; 
} 

count = 0.
number = int(input("Enter a number "))
while (number > 0):
number = number//10.
count = count + 1.
print ("Total number of digits : ",count)
'''