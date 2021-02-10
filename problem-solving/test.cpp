#include <iostream>
#define SIZE 99
using namespace std;
int main (){
	long long int n;
	int r,a[SIZE],i=0;
	cin>>n;
	if(n==0){
		cout<<n<<": ";
	}
    while(n>0){
    	r=n%10;
        a[i]=r;
    	n=n/10;
    	i++;
	}
	if(i>=SIZE+1){
		return 0;
	}
	else{
	for(int j=i-1;j>=0;j--){
		cout<<a[j]<<": ";
		for(int k=1;k<=a[j];k++){
			cout<<a[j];
		}
		cout<<"\n";
	}
   }
	
	return 0;
}
