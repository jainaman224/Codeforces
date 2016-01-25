// By Aman Jain
// 14/1/16

#include <iostream>

using namespace std;

int main(){
	long a,b;
	int array[1000],flag=0,j,temp;
	int i=999;
	while(i--){
		array[i]=-1;
	}
	array[0]=1;
	cin >> a;
	while(a--){
		cin >> b;
		if(b==0)
			flag=1;
		temp=0;
		j=0;
		while(array[j]>=0){	   
			temp+=b*array[j];
			array[j]=temp%10;
			temp=temp/10;
			j++;
		}
		while(temp){
			array[j]=temp%10;
			temp/=10;
			j++;
		}
	}
	j--;
	if(flag==1)
		cout << 0;
	else
		while(j>=0){
			cout << array[j--];
		}
}