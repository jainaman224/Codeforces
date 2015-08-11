#include <iostream>

using namespace std;

int main(){
	int a,j=0,l=0;
	cin >> a;
	int b[a][2];
	for(int i=0;i<a;i++){
		cin >> b[i][0] >> b[i][1];
	}

	while(j<a){
		for(int i=0;i<a;i++){
			// to check if dress of home team matches to away dress of other team
			if (i!=j && b[j][0]==b[i][1]){
				l++;
			}
		}
		j++;
	}
	cout << l << endl;
}