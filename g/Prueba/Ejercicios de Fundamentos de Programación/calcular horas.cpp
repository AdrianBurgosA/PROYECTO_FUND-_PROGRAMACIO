
#include <iostream>
#include <math.h>
#include <stdlib.h>

using namespace std;

int main ()
{
	system ("color 3f");
    //DECLARAR VARIABLES
    float minutos,minfi,horas;

    //INGRESO DE DATOS
    cout<<"Ingrese el numero de minutos"<<endl;
    cin>> minutos;
    
    //CALCULOS
    horas=minutos/60;
    minfi=(horas-trunc(horas))*60;
    horas=trunc(horas);
    
    //IMPRESION DE RESULTADOS
    cout<<"Para:  "<<minutos<<" Corresponde a: "<<horas<<" y "<<minfi<<" minutos "<<endl;
    system ("cls");
    system ("PAUSE");
    return 0;
    
}
