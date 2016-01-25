// By Aman Jain
// 14/1/16

#include <iostream>

using namespace std;

int main(){
	int flag=0;
	long long a,b,c,d;
	cin >> a >> b >> c;
	d=1;
	while(d<a){
		d*=c;
	}
	while(d>=a && d<=b){
		flag=1;
		cout << d << " ";
		d*=c;
	}
	if(flag==0)
		cout << -1;
	return 0;
}