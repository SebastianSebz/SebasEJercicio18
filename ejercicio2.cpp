# include <iostream>

using std::cout;
using std::endl;

int main(){

float h = 0.1; float z = 0; float x = 0; float y = 1; float N = 10/h; 

for (int i=0; i<N; i++){
	
	float z = z-h*y;
	float y = y+ h*z;
	float x = x+h;

cout << x << " " << y << " "<< z << endl;

}

return 0;
}

