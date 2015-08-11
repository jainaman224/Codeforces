#include <iostream>

using namespace std;

int main(){
	int a,c=0,d=0,e=0;
	cin >> a;
	int b[a][3];
	for (int i=0;i<a;i++){
		cin >> b[i][0] >> b[i][1] >> b[i][2];
		c+=b[i][0];
		d+=b[i][1];
		e+=b[i][2];
	}
	if (c==0 && d==0 && e==0){
		cout << "YES";
	}
	else{
		cout << "NO";
	}
}