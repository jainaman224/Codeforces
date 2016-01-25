#include <iostream>
#include <math.h>

using namespace std;

int main(){
	long long a,b[2],c[2],d,e,f,g;
	cin >> a >> f;
	g=a;
	a--;
	e=0;
	b[0]=c[0]=f;
	b[1]=c[1]=1;
	d=1;
	while(a--){
		cin >> f;
		if(f==b[0] && f==c[0]){
			d++;
			b[1]++;
			c[1]++;
		}
		else if(b[0]==c[0] && (f-b[0])<2 && (f-b[0])>0){
			c[0]=f;
			c[1]++;
			d++;
		}
		else if(b[0]==c[0] && (c[0]-f)<2 && (c[0]-f)>0){
			d++;
			b[0]=f;
			b[1]++;
		}
		else if(f==b[0]){
			d++;
			b[1]=g-a;
		}
		else if(f==c[0]){
			d++;
			c[1]=g-a;
		}
		else if((b[0]-f)<2 && (b[0]-f)>0){
			if(d>e)
				e=d;
			d=g-a-c[1];
			c[0]=b[0];
			b[0]=f;
			c[1]=b[1];
			b[1]=g-a;
		}
		else if((f-c[0])<2 && (f-c[0])>0){
			if(d>e)
				e=d;
			b[0]=c[0];
			c[0]=f;
			d=g-a-b[1];
			b[1]=c[1];
			c[1]=g-a;
		}
	}
	if(d>e)
		e=d;
	cout << e << endl;
}