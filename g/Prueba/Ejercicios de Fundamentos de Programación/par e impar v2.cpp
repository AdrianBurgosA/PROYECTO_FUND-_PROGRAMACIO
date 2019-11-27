#include<iostream>
#include <conio.h>
using namespace std;
int main()
{
    //declarar variables
    int numero;
    //lectura de datos
    cout<<"ingrese el numero entero"<<endl;
    cin>>numero;
    //desarrollo
    if(numero==0)
    {
        cout<<"El numero es cero"<<endl;
    }
    else
    {
       if(numero%2==0)
            cout<<"EL numero es par"<<endl;
       else
            cout<<"EL numero es impar"<<endl;
    }
    getch();
    return 0;
}
