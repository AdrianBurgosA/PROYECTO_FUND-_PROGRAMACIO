#include <iostream>
#include <stdlib.h>

using namespace std;

int main (){
	
int numero,numero1,numero2,aux,menor;
cout<<"Ingrese los 3 numeros"<<endl;

cin>>numero;
cin>>numero1;
cin>>numero2;

if ((numero>numero1)&&(numero1>numero2)){
    aux=numero;
}
else if ((numero1>numero)&&(numero1>numero2)){
    aux=numero1;
}
else {
    aux=numero2;
}

if ((numero<numero1)&&(numero1<numero2)){
	menor=numero;
} 
else if ((numero1<numero)&&(numero1<numero2)){
	menor=numero1;
} else {
	menor = numero2;
}

cout<<"El numero mayor es: "<<aux<<endl;
cout<<"El numero menor es: "<<menor<<endl;
return 0;
}

