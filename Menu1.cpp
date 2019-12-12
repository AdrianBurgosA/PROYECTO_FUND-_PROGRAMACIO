#include <stdio.h>
#include <stdlib.h>
#include <windows.h> //Esta librería nos permitirá pausar la pantalla por milisegundos

void mostrar();
void Crear(FILE *fp);
void Escribir(FILE *fp, char cad[100]);
void Consultar (FILE *fp, char cad[100]);

int main(){
int opc;
char cadena[100];
FILE *fp; //La eclaración para un fichero siempre será FILE *nombre

do{//Bucle para repetir el menu hasta escoger la opcion de salir
Sleep(500); //La pantalla se pausará por 5 seg
system("cls");//Limpiar pantalla
mostrar();
scanf("%i",&opc);//Scanf cumple con la misma función del comando cin de la librería iostream, %i es el formato de la variable entera
switch(opc){
case 1:
	system("cls");
	Crear(fp);
	Sleep(500);//La pantalla se pausará por 5 seg
	break;
case 2:
	system("cls");
	printf("INGRESE UNA CADENA\n");
	scanf("%s",&cadena);//Scanf cumple con la misma función del comando cin de la librería iostream, %s es el formato de la variable de tipo string
	Escribir(fp,cadena);
	Sleep(500);//La pantalla se pausará por 5 seg
	break;
case 3:
	system("cls");
	printf("El contenido es: \n");//Cumple con la misma función del comando cout de la librería iostream

	Sleep(500);//La pantalla se pausará por 5 seg
	break;
case 4:
	system("cls");
	printf("Ha salido con exito\n");
	exit(0);
default:
	system("cls");
	printf("Error\n");//La pantalla se pausará por 5 seg
	Sleep(500);//La pantalla se pausará por 5 seg
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
		fclose(fp);//fclose(nombre) sirve para cerrar el archivo plano
		exit(0);//En caso de que se lanzara un error, la ejecución terminará
	}else{
		printf("El fichero ha sido creado con exito\n");
	}
}

void Escribir(FILE *fp, char cad[100]){
fp = fopen("prueba.txt","a");//Se abre el archivo con tipo de apertura "2", abrir un archivo para escritura al final del contenido, si no existe se crea.
fprintf(fp,"%s\n",cad);//Escribe la cadena ingresada anteriormente en el fichero
fclose(fp);//Cierra el fichero
}
