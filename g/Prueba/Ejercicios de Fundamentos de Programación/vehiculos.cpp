/* VEHÍCULOS*/
#include <iostream>
#include <stdlib.h>

using namespace std;

int main ()
{

float velocidad_a, velocidad_b, espacio, tiempo;

 cout << "INGRESE LA DISTANCIA"<<endl;
 cin >> espacio;
 system ("cls"); //Limpiar pantalla
 cout <<"INGRESE LA VELOCIDAD DEL PRIMER VEHICULO EN KM/MIN"<<endl;
 cin >> velocidad_a;
 system ("cls");
 cout <<"INGRESE LA VELOCIDAD DEL SEGUNDO VEHICULO EN KM/MIN"<<endl;
 cin >> velocidad_b;
 system ("cls");

 if (velocidad_a > velocidad_b){
    tiempo=espacio/(velocidad_a - velocidad_b);
    cout << endl;
    cout << "El vehiculo A con la mayor velocidad de " << velocidad_a << " Alcanza al vehiculo más lento con " << velocidad_b << " en " << tiempo<< " minutos "<<endl;
 } else {
    tiempo=espacio/(velocidad_b - velocidad_a);
    cout <<  endl;
    cout << "El vehiculo A con la mayor velocidad de " << velocidad_b << " Alcanza al vehiculo más lento con " << velocidad_a << " en " << tiempo<< " minutos "<<endl;
 }

 return 0;
 system ("PAUSE");
}
