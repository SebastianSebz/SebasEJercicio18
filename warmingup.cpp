# include <iostream>

using std::cout;
using std::endl;

int main(){

float h = 0.1;
float x = 0.0;
float y = 1;
int N = 3/h;

for (int i=0; i<N; i++){
	
	float y = y -h*y;
	float x = x+h;

cout << x << " " << y << endl;

}

return 0;
}

