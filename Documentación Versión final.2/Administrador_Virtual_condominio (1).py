from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import time
from os import remove

#Autores: Mateo Castillo, Adrián Burgos

def Modo_admin():
    def Ingreso():

        #Boton Cambiar contraseña
        def CambioClave(): #Cambiar clave administrador
            def minimizar3():
                cambcl.destroy()
                ingreso.deiconify()
            def Clave():
                file = open("Admin.txt","r")
                lista = file.read().split(',')
                file.close
                
                if (claveactual.get()==lista[1]):
                    if clavenueva.get()==lista[1]:
                        messagebox.showerror("Error","La clave debe ser diferente a la actual")
                    else:
                        if(clavenueva.get()==confirmar.get()):
                            file = open("Admin.txt","w")
                            lista[1] = clavenueva.get()
                            cadena = ",".join(lista)
                            file.write(cadena)
                            file.close
                            messagebox.showinfo("Clave actualizada","Su clave ha sido actualizada, por su seguridad el sistema se cerrará")
                            cambcl.quit()
                        else:
                            messagebox.showwarning("Advertencia","Las contraseñas no coinciden")
                else:
                    messagebox.showerror("Error","Contraseña actual incorrecta, vuelva a intentarlo!")

            ingreso.iconify()
            cambcl = Toplevel()
            cambcl.title("Cambiar clave de administrador")
            cambcl.geometry("400x300")
            cambcl.config(bg='cadetblue4')
            claveactual = StringVar()
            clavenueva = StringVar()
            confirmar = StringVar()
            tag = Label(cambcl,text="Ingrese la contraseña actual",bg='cadetblue4',font=('fixedsys',12)).place(x=100,y=30)
            entrada = Entry(cambcl,width=15,textvariable=claveactual).place(x=160,y=60)
            tag1 = Label(cambcl,text="Ingrese la contraseña nueva",bg='cadetblue4',font=('fixedsys',12)).place(x=100,y=90)
            entrada1 = Entry(cambcl,width=15,textvariable=clavenueva).place(x=160,y=120)
            tag2 = Label(cambcl,text="Vuelva a ingresar la contraseña nueva",bg='cadetblue4',font=('fixedsys',12)).place(x=60,y=150)
            entrada2 = Entry(cambcl,width=15,textvariable=confirmar).place(x=160,y=170)
            Button(cambcl,text="Actualizar clave",font=('fixedsys',7),width=20,command=Clave).place(x=125,y=210)
            Button(cambcl,text="Atrás",font=('fixedsys',7),width=10,command=minimizar3).place(x=20,y=270)
            Button(cambcl,text="Salir",font=('fixedsys',7),width=10,command=quit).place(x=290,y=270)

        #Boton cambiar usuario
        def CambioUser(): 
            def minimizar4():
                cambus.destroy()
                ingreso.deiconify()
            def Usuario():
                file = open("Admin.txt","r")
                lista = file.read().split(',')
                file.close
                
                if (actual.get()==lista[0]):
                    if newuser.get()==lista[0]:
                        messagebox.showerror("Error","El usuario debe ser diferente al actual")
                    else:
                        if(newuser.get()==confirmar.get()):
                            file = open("Admin.txt","w")
                            lista[0] = newuser.get()
                            cadena = ",".join(lista)
                            file.write(cadena)
                            file.close
                            messagebox.showinfo("Usuario actualizado","Su usuario ha sido actualizado, por su seguridad el sistema se cerrará")
                            cambus.quit()
                        else:
                            messagebox.showwarning("Advertencia","Los ID no coinciden")
                else:
                    messagebox.showerror("Error","Usuario actual incorrecto,vuelva a intentarlo!")

            ingreso.iconify()
            cambus = Toplevel()
            cambus.title("Cambiar ID de administrador")
            cambus.geometry("400x300")
            cambus.config(bg='cadetblue4')
            actual = StringVar()
            newuser = StringVar()
            confirmar = StringVar()
            tag = Label(cambus,text="Ingrese el ID del usuario actual",bg='cadetblue4',font=('fixedsys',12)).place(x=100,y=30)
            entrada = Entry(cambus,width=15,textvariable=actual).place(x=160,y=60)
            tag1 = Label(cambus,text="Ingrese el nuevo ID de usuario",bg='cadetblue4',font=('fixedsys',12)).place(x=100,y=90)
            entrada1 = Entry(cambus,width=15,textvariable=newuser).place(x=160,y=120)
            tag2 = Label(cambus,text="Vuelva a ingresar el usuario",bg='cadetblue4',font=('fixedsys',12)).place(x=100,y=150)
            entrada2 = Entry(cambus,width=15,textvariable=confirmar).place(x=160,y=170)
            Button(cambus,text="Actualizar usuario",font=('fixedsys',7),width=20,command=Usuario).place(x=125,y=210)
            Button(cambus,text="Atrás",font=('fixedsys',7),width=10,command=minimizar4).place(x=20,y=270)
            Button(cambus,text="Salir",font=('fixedsys',7),width=10,command=quit).place(x=290,y=270)

        #Boton añadir condominio
        def AgregarCondomino(): #Agregar condómino #Un fichero por condómino
            
            def ayuda():
                messagebox.showinfo("Ayuda","Se debe ingresar el apellido y la inicial del segundo apellido")
            
            def minimizar5():
                add.destroy()
                ingreso.deiconify()

            def Registro():
                txt = condomino.get()+".txt"
                archivo=open(txt,"w")
                archivo.write("0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0\n")
                archivo.close
                file = open("condominos.txt","a")
                file.write(condomino.get()+"\n")
                file.close
                messagebox.showinfo("Éxito","Se ha registrado el condominio")

            ingreso.iconify()
            condomino = StringVar()
            add = Toplevel()
            add.geometry("300x200")
            add.title("Añadir Condómino")
            add.config(bg='cadetblue4')
            tag = Label(add,text="Añadir Condómino",bg='cadetblue4',font=('fixedsys',20)).place(x=30,y=10)
            nombre = Label(add,text="Ingrese su nombre: ",bg='cadetblue4',font=('fixedsys',7)).place(x=20,y=50)
            entry = Entry(add,width=25,textvariable=condomino).place(x=60,y=80)
            Button(add,width=2,text="?",font=('fixedsys',7),fg='blue',command=ayuda).place(x=215,y=77)
            Button(add,width=10,text="Añadir",font=('fixedsys',7),command=Registro).place(x=120,y=120)
            Button(add,width=7,text="Atrás",font=('fixedsys',7),command=minimizar5).place(x=15,y=160)
            Button(add,width=7,text="Salir",font=('fixedsys',7),command=quit).place(x=230,y=160)

        #Boton Eliminar condominio
        def EliminarCondomino(): #Eliminar condómino
            
            def minimizar6():
                quit.destroy()
                ingreso.deiconify()
            def Eliminar():
                file = open("condominos.txt","r")
                lista = file.read().split('\n')
                if eliminar.get() in lista:
                    lista.remove(eliminar.get())
                file.close
                file = open("condominos.txt","w")
                cad = ("\n").join(lista)
                file.write(cad)
                file.close
                txt = eliminar.get()+".txt"
                remove(txt)
                messagebox.showinfo(" ","Se eliminó con éxito!")

            ingreso.iconify()
            quit = Toplevel()
            quit.title("Eliminar Condómino")
            quit.geometry("300x200")
            quit.config(bg='cadetblue4')
            tag = Label(quit,text="Seleccione: ",bg='cadetblue4',font=('fixedsys',10)).place(x=10,y=50)
            file = open("condominos.txt","r")
            eliminar = ttk.Combobox(quit,state='readonly')
            eliminar.place(x=100,y=50)
            eliminar['values'] = file.read()
            Button(quit,text="Eliminar",width=10,font=('fixedsys',7),command=Eliminar).place(x=100,y=100)
            file.close
            Button(quit,width=7,text="Atrás",font=('fixedsys',7),command=minimizar6).place(x=15,y=160)

        #Boton Info. de condominio
        def Mostrar_condominio():
            
            def minimizar7():
                cons.destroy()
                ingreso.deiconify()

            def consultar():
                def ver():
                    b = 100
                    file = open(nombre,"r")
                    lista = [l.split(',') for l in file]
                    for a in lista:
                        if not(a==lista[0]):
                            texto = "    "+a[0]+"       "+a[1]+" en el mes de "+a[3]
                            te = Label(cons,text=texto,bg='cadetblue4',font=('fixedsys',14)).place(x=90,y=b)
                            b = b + 20

                nombre=consultar.get()+".txt"
                file=open(nombre,"r")
                lista = file.read().split(',')
                tag1=Label(cons,text=consultar.get(),bg='cadetblue4',font=('fixedsys',14),fg='white').place(x=20,y=100)
                #tag2=Label(userq,text=sk,bg='cadetblue4',font=('fixedsys',14)).place(x=120,y=120)
                ver()
                file.close


            ingreso.iconify()
            cons = Toplevel()
            cons.title("Consultar Condómino")
            cons.geometry("500x400")
            cons.config(bg='cadetblue4')
            tag1=Label(cons,text="Información de condominio",bg='cadetblue4',font=('fixedsys',20)).place(x=50,y=0)
            tag = Label(cons,text="Seleccione: ",bg='cadetblue4',font=('fixedsys',10)).place(x=90,y=40)
            tag_we=Label(cons,text="Nombre:    Deudas: ",bg='cadetblue4',font=('fixedsys',14),fg='yellow').place(x=20,y=70)
            tag_we=Label(cons,text="Nombre:    Deudas:     Descripción: ",bg='cadetblue4',font=('fixedsys',14),fg='yellow').place(x=20,y=70)
            Button(cons,width=7,text="Atrás",font=('fixedsys',7),command=minimizar7).place(x=30,y=360)
            Button(cons,text="Consultar",font=('fixedsys',10),command=consultar).place(x=350,y=40)
            file = open("condominos.txt","r")
            consultar = ttk.Combobox(cons,state='readonly')
            consultar.place(x=200,y=40)
            consultar['values'] = file.read()

        def minimizar2():
            window.deiconify()
            ingreso.destroy()
        
        def Alicuota(): #Cambiar alícuota según sus valores delos servicios   #Actualizar el valor mensual de la alícuota
            def minimizar8():
                eg.destroy()
                ingreso.deiconify()
            #def Calcular():

            def Calcular():
                file = open("Alicuota.txt","w")
                file.write(valor.get())
                file.close
                messagebox.showwarning("","La alícuota ha sido actualizada")

            valor = StringVar()
            ingreso.iconify()
            eg = Toplevel()
            eg.geometry("450x200")
            eg.title("Alícuota")
            eg.config(bg='cadetblue4')
            tag4 = Label(eg,text="Definir Alícuota del conjunto",bg='cadetblue4',font=('fixedsys',15),fg='yellow').place(x=140,y=10)
            entry = Entry(eg,textvariable=valor,width=7).place(x=140,y=40)
            Button(eg,text="Actualizar",command=Calcular,width=10,font=('fixedsys',6)).place(x=160,y=140)
            Button(eg,text="Atrás",command=minimizar8,width=10,font=('fixedsys',6)).place(x=40,y=140)
            Button(eg,text="Salir",command=quit,width=10,font=('fixedsys',6)).place(x=260,y=140)

        def Reporteingresos(): #Informe de ingresos   #Registrar en fichero

            def Información():
                global Enero 
                global Febrero 
                global Marzo 
                global Abril 
                global Mayo 
                global Junio 
                global Julio 
                global Agosto 
                global Septiembre 
                global Octubre 
                global Noviembre 
                global Diciembre 
                file = open("condominos.txt","r") 
                a = file.read().split('\n')
                i = 60
                ar = open("Egresos.txt","w")
                for e in a:
                    txt = e +".txt"
                    name = open(txt,"r")
                    lineas = [i.split(',') for i in name]
                    name.close
                    name = open("Ingresos.txt","a")
                    abc = "   Condómino    Enero    Febrero    Marzo    Abril    Mayo    Junio    Julio    Agosto    Septiembre    Octubre    Noviembre    Diciembre    Total"
                    name.write
                    info = Label(ing,text=abc,bg='cadetblue4',font=('fixedsys',6)).place(x=10,y=40)
                    for lista in lineas:
                        if lista == lineas[0]:
                            mensaje = "   "+e+"       "+lista[0]+"       "+lista[1]+"       "+lista[2]+"       "+lista[3]+"      "+lista[4]+"      "+lista[5]+"      "+lista[6]+"       "+lista[7]+"       "+lista[8]+"         "+lista[9]+"       "+lista[10]+"            "+lista[11]+"        "+lista[12]
                            Enero = Enero + float(lista[0])
                            Febrero = Febrero + float(lista[1])
                            Marzo = Marzo + float(lista[2])
                            Abril = Abril + float(lista[3])
                            Mayo = Mayo + float(lista[4])
                            Junio = Junio + float(lista[5])
                            Julio = Julio + float(lista[6])
                            Agosto = Agosto + float(lista[7])
                            Septiembre = Septiembre + float(lista[8])
                            Octubre = Octubre + float(lista[9])
                            Noviembre = Noviembre + float(lista[10])
                            Diciembre = Diciembre +float( lista[11])
                            name.write(mensaje)
                            t = Label(ing,text=mensaje,bg='cadetblue4',font=('fixedsys',6)).place(x=10,y=i)
                            i = i + 20
                    name.close
                    cadena = str(Enero)+','+str(Febrero)+','+str(Marzo)+','+str(Abril)+','+str(Mayo)+','+str(Junio)+','+str(Julio)+','+str(Agosto)+','+str(Septiembre)+','+str(Octubre)+','+str(Noviembre)+','+str(Diciembre)+'\n'
                    ar.write(cadena)
                ar.close
                file.close

            def minimize():
                ingreso.deiconify()
                ing.destroy()
            
            ingreso.iconify()
            ing = Toplevel()
            ing.title("Reporte de Ingresos")
            ing.geometry("1200x400")
            ing.config(bg='cadetblue4')
            etiqueta = Label(ing,text="INGRESO",bg='cadetblue4',font=('fixedsys',20),fg='yellow').place(x=500,y=10)
            Button(ing,text="Atrás",width=10,font=('fixedsys',6),command=minimize).place(x=50,y=320)
            Información()
            name.close

        def ReporteEgresos(): #Informe de egresos  #Total por mes y quitar monto con descripción

            def minimize():
                ingreso.deiconify()
                eg.destroy()
            
            def consultar3():
                def ver():
                    b = 70
                    file = open("Egresos.txt","r")
                    lista = [l.split(',') for l in file]
                    for a in lista:
                        if not(a==lista[0]) and not(a==lista[1]):
                            texto = "    "+a[0]+"       "+a[1]+" en el mes de "+a[3]
                            te = Label(eg,text=texto,bg='cadetblue4',font=('fixedsys',14)).place(x=20,y=b)
                            b = b + 20

                #nombre=entrada_ID.get()+".txt"
                file=open("Egresos.txt","r")
                lista = file.read().split(',')
                #tag1=Label(eg,text=entrada_ID.get(),bg='cadetblue4',font=('fixedsys',14),fg='white').place(x=20,y=100)
                #tag2=Label(userq,text=sk,bg='cadetblue4',font=('fixedsys',14)).place(x=120,y=120)
                ver()
                file.close

            ingreso.iconify()
            eg = Toplevel()
            eg.title ("Reporte de Egresos")
            eg.geometry("600x400")
            eg.config(bg='cadetblue4')
            tag  = Label(eg,text="EGRESOS",bg='cadetblue4',fg='Black',font=('fixedsys',20)).place(x=250,y=10)
            tag  = Label(eg,text="Monto:    Descripción:",bg='cadetblue4',fg='Yellow',font=('fixedsys',15)).place(x=40,y=40)
            #mes = ttk.Combobox(eg,state='readonly')
            #mes.place(x=50,y=50)
            #mes['values'] = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
            Button(eg,text="Ver Egresos",font=('fixedsys',7),width=15,command=consultar3).place(x=240,y=330)
            Button(eg,text="Atrás",width=7,font=('fixedsys',6),command=minimize).place(x=30,y=360)
        
        adminw.destroy()
        ingreso = Toplevel()
        ingreso.title("Modo Administrador")
        ingreso.geometry("500x400")
        ingreso.config(bg='cadetblue4')
        etiqueta = Label(ingreso,text="Administrador",bg='cadetblue4',font=('fixedsys',20)).place(x=150,y=0)

        #Gestion de condominios
        tag = Label(ingreso,text="Gestión de condominios",bg='cadetblue4',font=('fixedsys',15)).place(x=20,y=50)
        Button(ingreso,text="Info. de condominio",width=18,font=('fixedsys',7),command=Mostrar_condominio).place(x=35,y=170)
        Button(ingreso,text="Agregar Condómino",width=18,font=('fixedsys',7),command=AgregarCondomino).place(x=35,y=90)
        Button(ingreso,text="Eliminar Condómino",width=18,font=('fixedsys',7),command=EliminarCondomino).place(x=35,y=130)

        #Gestión de dinero
        tag = Label(ingreso,text="Gestión de dinero",bg='cadetblue4',font=('fixedsys',15)).place(x=325,y=50)
        Button(ingreso,text="Cambiar Alícuota",width=18,font=('fixedsys',7),command=Alicuota).place(x=320,y=90)
        Button(ingreso,text="Reporte Ingresos",width=18,font=('fixedsys',7),command=Reporteingresos).place(x=320,y=130)
        Button(ingreso,text="Reporte Egresos",width=18,font=('fixedsys',7),command=ReporteEgresos).place(x=320,y=170)

        #Gestión de Administrador
        tag = Label(ingreso,text="Gestión de cuenta de administrador",bg='cadetblue4',font=('fixedsys',15)).place(x=110,y=210)
        Button(ingreso,text="Cambiar Clave",width=18,font=('fixedsys',7),command=CambioClave).place(x=175,y=290)
        Button(ingreso,text="Cambiar Admin",width=18,font=('fixedsys',7),command=CambioUser).place(x=175,y=250)

        #Botones de navegación 
        Button(ingreso,text="Atrás",width=10,font=('fixedsys',7),command=minimizar2).place(x=30,y=360)
        Button(ingreso,text="Salir",width=10,font=('fixedsys',7),command=quit).place(x=380,y=360)

    def validar1(): #Validar intentos
        global intentos 
        file = open("Admin.txt","r")
        lista = file.read().split(',')
        if verifica_usuario.get()==lista[0] and verifica_clave.get()==lista[1]:
            messagebox.showinfo("Éxito","Se accedió con éxito")
            Ingreso()
        else:
            messagebox.showerror("Error","Usuario y/o contraseña incorrectos")
            intentos = intentos +1
            if intentos == 3:
                messagebox.showwarning("Atención","El programa se cerrará por seguridad")
                window.destroy()
        file.close 

    def restitucion():
        file=open("Admin.txt","w")
        file.write("Admin"+","+"246810")
        file.close
        messagebox.showinfo("Listo","Se ha reiniciado el usuario con éxito")

    def minimizar():
        window.deiconify()
        adminw.destroy()

    verifica_usuario=StringVar()
    verifica_clave=StringVar()
    window.iconify()
    adminw = Toplevel()
    adminw.title("Modo Administrador")
    adminw.geometry("500x400")
    adminw.config(bg='cadetblue4')
    etiqueta = Label(adminw,text="INICIO DE SESIÓN:",font=('fixedsys',17),bg='cadetblue4').place(x=110,y=0)
    tag1=Label(adminw,text="Usuario:",font=('fixedsys',15),bg='cadetblue4').place(x=90,y=100)
    entrada_usuario=Entry(adminw,width=25,textvariable=verifica_usuario).place(x=190,y=100)
    tag2=Label(adminw,text="Contraseña:",font=('fixedsys',15),bg='cadetblue4').place(x=90,y=140)
    entrada_contraseña=Entry(adminw,width=25,textvariable=verifica_clave,show="*").place(x=190,y=140)    
    Button(adminw,text="",width=0,bg='black',fg='cadetblue4',command=restitucion).place(x=115,y=-15)
    tags=Label(adminw,text="",width=1,bg='cadetblue4',font=('fixedsys',2)).place(x=112.5,y=-12)
    Button(adminw,text="Iniciar sesión",width=15,command=validar1,font=('fixedsys',8)).place(x=200,y=180)
    Button(adminw,text="Atrás",width=7,command=minimizar,font=('fixedsys',8)).place(x=30,y=360)

def Modo_user():

    def minimize():
        window.deiconify()
        us.destroy()

    def Addmonto(): #Función para agregar monto a un condómino
        def consultar2():
            def ver():
                b = 100
                file = open(nombre,"r")
                lista = [l.split(',') for l in file]
                for a in lista:
                    if not(a==lista[0]):
                        texto = "    "+a[0]+"       "+a[1]+" en el mes de "+a[3]
                        te = Label(userw,text=texto,bg='cadetblue4',font=('fixedsys',14)).place(x=90,y=b)
                        b = b + 20

            nombre=entrada_ID.get()+".txt"
            file=open(nombre,"r")
            lista = file.read().split(',')
            tag1=Label(userw,text=entrada_ID.get(),bg='cadetblue4',font=('fixedsys',14),fg='white').place(x=20,y=100)
            #tag2=Label(userq,text=sk,bg='cadetblue4',font=('fixedsys',14)).place(x=120,y=120)
            ver()
            file.close
    
        def deudas():
            txt = entrada_ID.get() + ".txt"
            name = open(txt,"a")
            name.write(str(monto.get()+','+motivo.get()+','+mes.get()+'\n'))
            name.close
            messagebox.showinfo("Éxito","El monto ha sido agregado")

            def posicion (i):
                p = 0
                if i[2] == 'Enero'+'\n':
                    p = 0
                elif i[2]=='Febrero'+'\n':
                    p = 1
                elif i[2]=='Marzo'+'\n':
                    p = 2
                elif i[2]=='Abril'+'\n':
                    p = 3
                elif i[2]=='Mayo'+'\n':
                    p = 4
                elif i[2]=='Junio'+'\n':
                    p = 5
                elif i[2]=='Julio'+'\n':
                    p = 6
                elif i[2]=='Agosto'+'\n':
                    p = 7
                elif i[2]=='Septiembre'+'\n':
                    p = 8
                elif i[2]=='Octubre'+'\n':
                    p = 9
                elif i[2]=='Noviembre'+'\n':
                    p = 10
                elif i[2]=='Diciembre'+'\n':
                    p = 11
                return p

            name = open(txt,'r')
            linea = [i.split(',') for i in name]
            name.close
            name = open(txt,"w")
            for a in linea:
                aux = 'c'
                blo = 'i'
                if not(a==linea[0]):
                    if not (a[2]=='i'):
                        pos = posicion(a)
                        linea[0][pos] = str(float(linea[0][pos])+float(a[0]))
                        aux = a[2]
                        a[2] = blo
                        blo = aux
                        a.append(blo)
            for a in linea:
                cadena = ','.join(a)
                name.write(cadena)
                print(a)
            name.close

        def Añadiralicuota():
            def posicion (i):
                p = 0
                if i[2] == 'Enero'+'\n':
                    p = 0
                elif i[2]=='Febrero'+'\n':
                    p = 1
                elif i[2]=='Marzo'+'\n':
                    p = 2
                elif i[2]=='Abril'+'\n':
                    p = 3
                elif i[2]=='Mayo'+'\n':
                    p = 4
                elif i[2]=='Junio'+'\n':
                    p = 5
                elif i[2]=='Julio'+'\n':
                    p = 6
                elif i[2]=='Agosto'+'\n':
                    p = 7
                elif i[2]=='Septiembre'+'\n':
                    p = 8
                elif i[2]=='Octubre'+'\n':
                    p = 9
                elif i[2]=='Noviembre'+'\n':
                    p = 10
                elif i[2]=='Diciembre'+'\n':
                    p = 11
                return p
            # Agregar valor de alícuota por mes
            file = open("condominos.txt","r") 
            for nombre in file.readlines():
                aux = nombre.split()
                txt = "".join(aux) + ".txt"
                name = open(txt,"r")
                lista = name.read().split(',')
                ali = open("Alicuota.txt","r")
                al = ali.read().split('\n')
                if (mes.get()=='Enero'):
                    lista[0] = str(float(lista[0]) + float(al[0]))
                    str(lista[0])
                elif(mes.get()=='Febrero'):
                    lista[1] = str(float(lista[1]) + float(al[0]))
                    str(lista[1])
                elif(mes.get()=='Marzo'):
                    lista[2] = str(float(lista[2]) + float(al[0]))
                    str(lista[2])
                elif(mes.get()=='Abril'):
                    lista[3] = str(float(lista[3]) + float(al[0]))
                    str(lista[3])
                elif(mes.get()=='Mayo'):
                    lista[4] = str(float(lista[4]) + float(al[0]))
                    str(lista[4])
                elif(mes.get()=='Junio'):
                    lista[5] = str(float(lista[5]) + float(al[0]))
                    str(lista[5])
                elif(mes.get()=='Julio'):
                    lista[6] = str(float(lista[6]) + float(al[0]))
                    str(lista[6])
                elif(mes.get()=='Agosto'):
                    lista[7] = str(float(lista[7]) + float(al[0]))
                    str(lista[7])
                elif(mes.get()=='Septiembre'):
                    lista[8] = str(float(lista[8]) + float(al[0]))
                    str(lista[8])
                elif(mes.get()=='Octubre'):
                    lista[9] = str(float(lista[9]) + float(al[0]))
                    str(lista[9])
                elif(mes.get()=='Noviembre'):
                    lista[10] = str(float(lista[10]) + float(al[0]))
                    str(lista[10])
                elif(mes.get()=='Diciembre'):
                    lista[11] = str(float(lista[11]) + float(al[0]))
                    str(lista[11])
                
                cadena = al[0]+','+'alicuota'+','+mes.get()+'\n'
                ali.close
                name.close   
                name = open(txt,"a")
                name.write(cadena)
                name.close

                name = open(txt,'r')
                linea = [i.split(',') for i in name]
                name.close
                name = open(txt,"w")
                for a in linea:
                    aux = 'c'
                    blo = 'i'
                    if not(a==linea[0]):
                        if not (a[2]=='i'):
                            pos = posicion(a)
                            linea[0][pos] = str(float(linea[0][pos])+float(a[0]))
                            aux = a[2]
                            a[2] = blo
                            blo = aux
                            a.append(blo)
                for a in linea:
                    cadena = ','.join(a)
                    name.write(cadena)
                    print(a)
                name.close
                messagebox.showinfo("Exito","Se añadió la alícuota a todos los condóminos")
                file.close         

        def minimize():
            us.deiconify()
            userw.destroy()

        us.iconify()
        us.iconify()
        userw = Toplevel()
        monto = StringVar()
        motivo = StringVar()
        userw.title("Modo Usuario")
        userw.geometry("500x400")
        userw.config(bg='cadetblue4')
        file = open("condominos.txt","r")
        etiqueta = Label(userw,text="INGRESE EL ID",font=('fixedsys',20),bg='cadetblue4').place(x=140,y=0)
        tag_ID = Label(userw,text="ID:",bg='cadetblue4',font=('fixedsys',10)).place(x=150,y=40)
        tag_we=Label(userw,text="Nombre:    Deudas:     Descripción: ",bg='cadetblue4',font=('fixedsys',14),fg='yellow').place(x=20,y=70)
        montot = Label(userw,text="  Monto            Descripción",bg='cadetblue4',font=('fixedsys',10)).place(x=20,y=270)
        tag = Entry(userw,width=15,textvariable=monto).place(x=20,y=270)
        tagm = Entry(userw,width=30,textvariable=motivo).place(x=140,y=270)
        entrada_ID= ttk.Combobox(userw,state='readonly')
        entrada_ID.place(x=190,y=40)
        entrada_ID['values'] = file.read()
        Button(userw,text="Añadir multa",width=12,font=('fixedsys',12),command=deudas).place(x=350,y=270)
        file.close
        Button(userw,text="Añadir alícuota",width=15,font=('fixedsys',12),command=Añadiralicuota).place(x=100,y=300)
        mes = ttk.Combobox(userw,state='readonly')
        mes.place(x=250,y=300)
        mes['values'] = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
        Button(userw,text="Atrás",width=7,command=minimize,font=('fixedsys',8)).place(x=30,y=350)
        Button(userw,text="Salir",width=7,command=quit,font=('fixedsys',8)).place(x=350,y=350)
        Button(userw,text="Enter",width=4,font=('fixedsys',10),command=consultar2).place(x=350,y=38)
    
    def Quitmonto(): #Funcion para quitar un monto del condómino
        def minimizar():
            userq.destroy()
            us.deiconify()

        def consultar2():
            def ver():
                b = 100
                file = open(nombre,"r")
                lista = [l.split(',') for l in file]
                for a in lista:
                    if not(a==lista[0]):
                        texto = "    "+a[0]+"       "+a[1]+" en el mes de "+a[3]
                        te = Label(userq,text=texto,bg='cadetblue4',font=('fixedsys',14)).place(x=90,y=b)
                        b = b + 20

            nombre=entrada_ID.get()+".txt"
            file=open(nombre,"r")
            lista = file.read().split(',')
            tag1=Label(userq,text=entrada_ID.get(),bg='cadetblue4',font=('fixedsys',14),fg='white').place(x=20,y=100)
            #tag2=Label(userq,text=sk,bg='cadetblue4',font=('fixedsys',14)).place(x=120,y=120)
            ver()
            file.close
     
        def deudas():
            txt = entrada_ID.get() + ".txt"

            def posicion (i):
                p = 0
                if i[3] == 'Enero'+'\n':
                    p = 0
                elif i[3]=='Febrero'+'\n':
                    p = 1
                elif i[3]=='Marzo'+'\n':
                    p = 2
                elif i[3]=='Abril'+'\n':
                    p = 3
                elif i[3]=='Mayo'+'\n':
                    p = 4
                elif i[3]=='Junio'+'\n':
                    p = 5
                elif i[3]=='Julio'+'\n':
                    p = 6
                elif i[3]=='Agosto'+'\n':
                    p = 7
                elif i[3]=='Septiembre'+'\n':
                    p = 8
                elif i[3]=='Octubre'+'\n':
                    p = 9
                elif i[3]=='Noviembre'+'\n':
                    p = 10
                elif i[3]=='Diciembre'+'\n':
                    p = 11
                return p

            name = open(txt,'r')
            lineas = [linea.split(',') for linea in name]
            name.close

            name = open(txt,'w')
            for i in lineas:
                if not(i==lineas[0]):
                    if monto.get()==i[0] or (mes.get()+'\n')==i[3]:
                        pos = posicion(i)
                        lineas[0][pos] = str(float(lineas[0][pos])-float(i[0]))
                        lineas.remove(i)
            for i in lineas:
                sk = ','.join(i)
                name.write(sk)
            name.close
    
        def Quitaralicuota():
            # Eliminar valor de alícuota por mes
            txt = entrada_ID.get()+".txt"
            name = open(txt,"r")
            lista = name.read().split(',')
            ali = open("Alicuota.txt","r")
            al = ali.read().split('/')
            if (mes.get()=='Enero'):
                lista[0] = str(float(lista[0]) - float(al[3]))
                str(lista[0])
            elif(mes.get()=='Febrero'):
                lista[1] = str(float(lista[1]) - float(al[3]))
                str(lista[1])
            elif(mes.get()=='Marzo'):
                lista[2] = str(float(lista[2]) - float(al[3]))
                str(lista[2])
            elif(mes.get()=='Abril'):
                lista[3] = str(float(lista[3]) - float(al[3]))
                str(lista[3])
            elif(mes.get()=='Mayo'):
                lista[4] = str(float(lista[4]) - float(al[3]))
                str(lista[4])
            elif(mes.get()=='Junio'):
                lista[5] = str(float(lista[5]) - float(al[3]))
                str(lista[5])
            elif(mes.get()=='Julio'):
                lista[6] = str(float(lista[6]) - float(al[3]))
                str(lista[6])
            elif(mes.get()=='Agosto'):
                lista[7] = str(float(lista[7]) - float(al[3]))
                str(lista[7])
            elif(mes.get()=='Septiembre'):
                lista[8] = str(float(lista[8]) - float(al[3]))
                str(lista[8])
            elif(mes.get()=='Octubre'):
                lista[9] = str(float(lista[9]) - float(al[3]))
                str(lista[9])
            elif(mes.get()=='Noviembre'):
                lista[10] = str(float(lista[10]) - float(al[3]))
                str(lista[10])
            elif(mes.get()=='Diciembre'):
                lista[11] = str(float(lista[11]) - float(al[3]))
                str(lista[11])
            lista[12] = str(float(lista[0]) +float(lista[1])+float(lista[2])+float(lista[3]) +float(lista[4])+float(lista[5])+float(lista[6]) +float(lista[7])+float(lista[8])+float(lista[9]) +float(lista[10])+float(lista[11])+ deuda)

            cadena = ','.join(lista)
            ali.close
            name.close   
            name = open(txt,"w")
            name.write(cadena)
            name.close
            messagebox.showinfo("Exito","Se Realizó elpago la alícuota del condómino")      

        def Recibo():
            hora = time.strftime("%H:%M:%S")
            fecha = time.strftime("%d/%m/%y")
            def fichero():
                file = open("Recibo.txt","w")
                file.write("                    Recibo"+'\n')
                file.write(" ")
                file.write("Nombre: "+entrada_ID.get()+'\n')
                file.write("Fecha: "+str(fecha)+'\n')
                file.write("Hora: "+str(hora)+'\n')
                file.write("******************************************"+'\n')
                file.write("Pago                Descripción"+'\n\n')
                file.write(str(monto.get())+'$'+'                  '+str(motivo.get())+" por el mes de "+mes.get())
                file.close
            
            rec = Toplevel()
            rec.geometry("400x250")
            fichero()
            i = 10
            file = open("Recibo.txt","r")
            lista = file.read().split('\n')
            for a in lista:
                tag = Label(rec,text=a,font=('fixedsys',6)).place(x=10,y=i)
                i = i + 20
            file.close


        us.iconify()
        userq = Toplevel()
        monto = StringVar()
        motivo = StringVar()
        userq.title("Realizar Pago")
        userq.geometry("500x400")
        userq.config(bg='cadetblue4')
        file = open("condominos.txt","r")
        etiqueta = Label(userq,text="INGRESE EL ID",font=('fixedsys',20),bg='cadetblue4').place(x=140,y=0)
        tag_ID = Label(userq,text="ID:",bg='cadetblue4',font=('fixedsys',10)).place(x=150,y=40)
        tag_we=Label(userq,text="Nombre:    Deudas:     Descipción: ",bg='cadetblue4',font=('fixedsys',14),fg='yellow').place(x=20,y=70)
        montot = Label(userq,text="  Monto            Descripción",bg='cadetblue4',font=('fixedsys',10)).place(x=20,y=200)
        tag = Entry(userq,width=15,textvariable=monto).place(x=20,y=230)
        tagm = Entry(userq,width=30,textvariable=motivo).place(x=140,y=230)
        entrada_ID= ttk.Combobox(userq,state='readonly')
        entrada_ID.place(x=190,y=40)
        entrada_ID['values'] = file.read()
        Button(userq,text="Quitar multa",width=12,font=('fixedsys',12),command=deudas).place(x=350,y=230)
        file.close
        Button(userq,text="Quitar alícuota",width=15,font=('fixedsys',12),command=Quitaralicuota).place(x=100,y=280)
        mes = ttk.Combobox(userq,state='readonly')
        mes.place(x=250,y=280)
        mes['values'] = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
        Button(userq,text="Atrás",width=7,command=minimizar,font=('fixedsys',8)).place(x=30,y=350)
        Button(userq,text="Salir",width=7,command=quit,font=('fixedsys',8)).place(x=350,y=350)
        Button(userq,text="Imprimir Recibo",font=('fixedsys',8),command=Recibo).place(x=160,y=350)
        Button(userq,text="Enter",width=4,font=('fixedsys',10),command=consultar2).place(x=350,y=38)

    def Pagosc(): #Función para realizar los pagos del conjunto
        def show():
            mes = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
            file = open("Egresos.txt","r")
            lista = [i.split(',') for i in file]
            file.close
            b = 140 
            for a in lista:
                if a==lista[1]:
                    for e in a:
                        tag = Label(pg,text=e+'$',bg='cadetblue4',font=('fixedsys',7)).place(x=50,y=b)
                        b = b + 20
            x = 140
            for m in mes:
                tagm = Label(pg,text=m,bg='cadetblue4',font=('fixedsys',7)).place(x=150,y=x)
                x = x + 20
        def deudas():
            name = open("Egresos.txt","a")
            name.write(str(dinero.get()+','+motivo.get()+','+mes.get()+'\n'))
            name.close
            messagebox.showinfo("Éxito","Se ha agregado el gasto con éxito")

            def posicion (i):
                p = 0
                if i[2] == 'Enero'+'\n':
                    p = 0
                elif i[2]=='Febrero'+'\n':
                    p = 1
                elif i[2]=='Marzo'+'\n':
                    p = 2
                elif i[2]=='Abril'+'\n':
                    p = 3
                elif i[2]=='Mayo'+'\n':
                    p = 4
                elif i[2]=='Junio'+'\n':
                    p = 5
                elif i[2]=='Julio'+'\n':
                    p = 6
                elif i[2]=='Agosto'+'\n':
                    p = 7
                elif i[2]=='Septiembre'+'\n':
                    p = 8
                elif i[2]=='Octubre'+'\n':
                    p = 9
                elif i[2]=='Noviembre'+'\n':
                    p = 10
                elif i[2]=='Diciembre'+'\n':
                    p = 11
                return p

            name = open("Egresos.txt",'r')
            linea = [i.split(',') for i in name]
            name.close
            name = open("Egresos.txt","w")
            for a in linea:
                aux = 'c'
                blo = 'i'
                if not(a==linea[0]) and not(a==linea[1]):
                    if not (a[2]=='i'):
                        pos = posicion(a)
                        linea[1][pos] = str(float(linea[1][pos])-float(a[0]))
                        aux = a[2]
                        a[2] = blo
                        blo = aux
                        a.append(blo)
            for a in linea:
                cadena = ','.join(a)
                name.write(cadena)
                print(a)
            name.close
        
        def minimizarr():
            pg.destroy()
            us.deiconify()
        dinero = StringVar()
        motivo = StringVar()
        us.iconify()
        pg = Toplevel()
        pg.geometry("500x500")
        pg.title("Realizar Pagos del conjunto")
        pg.config(bg='cadetblue4')
        titulo = Label(pg,text="Realizar pagos del conjunto",bg='cadetblue4',font=('fixedsys',16),fg='yellow').place(x=160,y=10)
        mes = ttk.Combobox(pg,state='readonly')
        mes.place(x=240,y=60)
        mes['values'] = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
        mest = Label(pg,text="Mes",bg='cadetblue4',font=('fixedsys',7)).place(x=270,y=40)
        monto = Label(pg,text="Monto",bg='cadetblue4',font=('fixedsys',7)).place(x=50,y=40)
        mt = Entry(pg,width=10,textvariable=dinero).place(x=50,y=60)
        motivot = Label(pg,text="Descripción",bg='cadetblue4',font=('fixedsys',7)).place(x=130,y=40)
        mot = Entry(pg,width=15,textvariable=motivo).place(x=130,y=60) 
        Button(pg,text="Realizar",width=7,font=('fixedsys',7),command=deudas).place(x=240,y=100)
        Button(pg,text="Atrás",width=8,font=('fixedsys',7),command=minimizarr).place(x=40,y=460)
        show()
    
    def mini():
        us.destroy()
        window.deiconify()

    window.iconify()
    us = Toplevel()
    us.title("Modo usuario")
    us.geometry("400x300")
    us.config(bg='cadetblue4')
    tag = Label(us,text="MODO USUARIO",font=('fixedsys',20),bg='cadetblue4').place(x=110,y=10)
    Button(us,width=32,text="Añadir monto al condómino",command=Addmonto,font=('fixedsys',6)).place(x=70,y=100)
    Button(us,width=32,text="Realizar pago del condómino",command=Quitmonto,font=('fixedsys',6)).place(x=70,y=140)
    Button(us,width=32,text="Realizar pago del conjunto",command=Pagosc,font=('fixedsys',6)).place(x=70,y=180)
    Button(us,text="Atrás",width=7,font=('fixedsys',7),command=mini).place(x=40,y=260)


window = Tk()
window.title("Administrados de conjuntos habitacionales")
window.geometry("400x300")
window.config(bg='cadetblue4')
intentos = 0
Enero = 0
Febrero = 0
Marzo = 0
Abril = 0
Mayo = 0
Junio = 0
Julio = 0
Agosto = 0
Septiembre = 0
Octubre = 0
Noviembre = 0
Diciembre = 0
tag = Label(window,text="BIENVENIDO",font=('fixedsys',20),bg='cadetblue4').place(x=120,y=0)
tag2 = Label(window,text="AL ADMINISTRADOR",font=('fixedsys',20),bg='cadetblue4').place(x=70,y=50)
tag3 = Label(window,text="CÓMO DESEA INGRESAR?",font=('fixedsys',15),bg='cadetblue4').place(x=120,y=100)
Button(window,text="Usuario",width=15,command=Modo_user,font=('fixedsys',8)).place(x=140,y=150)
Button(window,text="Administrador",width=15,command=Modo_admin,font=('fixedsys',8)).place(x=140,y=180)
Button(window,text="Salir",width=7,command=quit,font=('fixedsys',8)).place(x=172,y=220)
window.mainloop()
