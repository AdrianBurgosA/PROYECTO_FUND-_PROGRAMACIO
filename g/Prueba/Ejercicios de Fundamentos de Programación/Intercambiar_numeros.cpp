#include <iostream>

using namespace std;

int main (){
int aux,numero,numero1;
cout<<"Ingrese dos numeros: "<<endl;
cin>>numero;
cin>>numero1;
cout<<endl;

cout<<"El resultado del intercambio es: "<<endl;
aux=numero;
numero=numero1;
numero1=aux;
cout<<endl;
cout<<"El nuevo valor del primer numero es: "<<numero<<endl;
cout<<"El nuevo valor del segundo numero es: "<<numero1<<endl;

return 0;
}
