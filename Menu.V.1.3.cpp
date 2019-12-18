/* AUTORES: ADRIÀN BURGOS, MATEO CASTILLO

REQUISITO FUNCIONAL: 
EL PROGRAMA DEBERÁ CREAR UN ARCHIVO PLANO, ESCRIBIR EN EL ARCHIVO PLANO, LEER EL ARCHIVO PLANO.
*/
#include <stdio.h>
#include <stdlib.h>

void mostrar();
void Crear(FILE *fp);
void Escribir(FILE *fp, char cad[100]);
void Consultar (FILE *fp, char cad[100]);

int main(){
char opc;
char cadena[100];
FILE *fp; //La declaración para un fichero siempre será FILE *nombre

do{
mostrar();
scanf("%s",&opc);
switch(opc){
case '1':
	system("cls");
	Crear(fp);
	system("PAUSE");
	system("cls");
	break;
case '2':
	system("cls");
	printf("INGRESE UNA CADENA\n");
	scanf("%s",&cadena);
	Escribir(fp,cadena);
	system("PAUSE");
	system("cls");
	break;
case '3':
	system("cls");
	printf("El contenido es: \n");
	Consultar(fp,cadena);
	printf("\n");
	system("PAUSE");
	system("cls");
	break;
case '4':
	system("cls");
	printf("Ha salido con exito\n");
	exit(0);
default:
	system("cls");
	printf("Error, recuerda ingresa un valor NUMERICO del 1 al 4\n");//La pantalla se pausará por 5 seg
	system("PAUSE");
	system("cls");
}
}while(opc!=4);

}
void mostrar(){
printf("\n\n			MENU\n\n");
printf("		1.- Crear Fichero\n");
printf("		2.- Escribir en el fichero\n");
printf(" 	        3.- Consultar el fichero\n");
printf("		4.- Salir\n");
printf("\n		INGRESE UNA OPCION:\n");	
}

void Crear(FILE *fp){
	
	fp = fopen("prueba.txt","a"); //Crea el archivo plano  nombre_archivo = fopen ("nombre.txt","a"), abrirá para escribir al final del archivo, si no existe lo crea
	if((fp = fopen("prueba.txt","a"))==NULL){ //Restricción que nos validará la creación del archivo, si está  vacío no lanzará un error
		printf("ERROR\n");
		fclose(fp);
		exit(0);//En caso de que se lanzara un error, la ejecución terminará
	}else{
		printf("El fichero ha sido creado con exito\n");
	}
}

void Escribir(FILE *fp, char cad[100]){
fp = fopen("prueba.txt","w");
fprintf(fp,"%s\n",cad);
fclose(fp);
}

void Consultar (FILE *fp, char cad[100]){
fp = fopen("prueba.txt","r");
fscanf(fp,"%s",cad);
printf("\n %s",cad);
fclose(fp);//Cierra el fichero
}
