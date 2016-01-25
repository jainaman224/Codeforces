#include <iostream>

using namespace std;

int main(){
	long long a,b,c=0,d,e=0;

	cin >> a >> b;
	while(a--){
		cin >> d;
		c*=b;
		c+=d;
	}

	cin >> a >> b;
	while(a--){
		cin >> d;
		e*=b;
		e+=d;
	}
	
	if(c>e)
		cout << ">" << endl;
	else if(c<e)
		cout << "<" << endl;
	else
		cout << "=" << endl;
}