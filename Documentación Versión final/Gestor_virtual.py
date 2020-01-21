from tkinter import *
from tkinter import messagebox
import os
from tkinter import ttk

def validar():
    #Ingresos
    def Consultar():
        con = Toplevel()
        con.geometry("500x400+525+250")
        file = open("Ingresos.txt","r")
        title = Label(con,text="CONSULTAR DEUDORES",bg='beige',font=('Comic',14)).place(x=160,y=0)
        tag = Label(con,text="Los condóminos deudores de la alicuota son:\n",fg="black").place(x=100,y=100)
        tag1 = Label(con,text=file.read()).place(x=200,y=150)
        file.close
        Button(con,text="Atrás",command=con.destroy,font=('Comic',10),width=7).place(x=90,y=350)

    def Alicuota():
        al = Toplevel()
        al.geometry("500x400+525+250")
        al.title("ALICUOTA")
        al.config(bg='beige')
        title = Label(al,text="INFORMA ALICUOTA",bg='beige',font=('Comic',14)).place(x=160,y=0)
        mensaje = "El valor mensual de la alícuota es de: 65 $ USD"
        agua = "Cuota para el agua: 30 $ USD"
        luz= "Cuota para la luz: 15 $ USD"
        guardia = "Cuota para la guardianía: 20 $ USD"
        tag = Label(al,text=mensaje,bg='beige').place(x=160,y=150)
        tag1 = Label(al,text=agua,bg='beige').place(x=160,y=180)
        tag2 = Label(al,text=luz,bg='beige').place(x=160,y=200)
        tag3 = Label(al,text=guardia,bg='beige').place(x=160,y=220)
        Button(al,text="Atrás",command=al.destroy,font=('Comic',10),width=7).place(x=90,y=350)

    def Quit():
        def Quitfromfile():
            file = open("Ingresos.txt","r")
            lista = []
            dato = deudores.get() + "\n"
            for linea in file.readlines():
                lista.append(linea)
            for e in lista:
                if dato==e:
                    lista.remove(e)
            file.close
            file = open("Ingresos.txt","w")
            for e in lista:
                file.write(e+"\n")
            file.close
            mensaje = "El condómino con el ID "+ deudores.get() +"  ha sido removido de la lista de deudores"
            tag = Label(quit,text=mensaje).place(x=90,y=190)
            
        quit = Toplevel()
        quit.geometry("500x400+525+250")
        tag = Label(quit,text="ELIMINAR DEUDOR",fg="black",bg='beige',font=('Comic',14)).place(x=160,y=0)
        tag1 = Label(quit,text="Seleccione: ",fg="black").place(x=175,y=100)
        file = open("Ingresos.txt","r")
        deudores = ttk.Combobox(quit)
        deudores.place(x=200,y=100)
        deudores['values'] = file.read()
        Button(quit,text="Eliminar",fg="Black",command=Quitfromfile).place(x=200,y=150)
        file.close()
        Button(quit,text="Atrás",command=quit.destroy,font=('Comic',10),width=7).place(x=90,y=350)

    def Add():
        def Addtofile():
            file = open("Ingresos.txt","a")
            confirm = Label(add,text="La lista ha sido actualizada",fg="black").place(x=150,y=200)        
            file.write(casas.get()+"\n")
            file.close
        add = Toplevel()
        add.geometry("500x400+525+250")
        tag = Label(add,text="AÑADIR DEUDOR",fg="black",bg='beige',font=('Comic',14)).place(x=200,y=0)
        tag1 = Label(add,text="Seleccione: ",fg="black",bg='beige').place(x=120,y=100)
        casas = ttk.Combobox(add)
        casas.place(x=200,y=100)
        casas ['values']= ['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20']
        Button(add,text="Añadir",fg="black",command=Addtofile).place(x=200,y=150)
        Button(add,text="Atrás",command=add.destroy,font=('Comic',10),width=7).place(x=90,y=350)

    def Ingresos():
        def minimizar():
            ingresos.destroy()
            menu.deiconify()
        menu.iconify()
        ingresos = Tk()
        ingresos.title("INGRESOS")
        ingresos.geometry("500x400+525+250")
        ingresos.config(bg='beige')
        etiqueta_bienvenida = Label(ingresos,text="MÓDULO DE INGRESOS",font=('Comic',14),bg='beige').place(x=160,y=0)
        Button(ingresos,text="Añadir Deudor",font=('Comic',10),width=15,fg="black",command=Add).place(x=200,y=100)
        Button(ingresos,text="Eliminar Deudor",font=('Comic',10),width=15,fg="black",command=Quit).place(x=200,y=150)
        Button(ingresos,text="Consultar deudores",font=('Comic',10),width=15,fg="black",command=Consultar).place(x=200,y=200)
        Button(ingresos,text="Consultar alícuota",font=('Comic',10),width=15,fg="black",command=Alicuota).place(x=200,y=250)
        Button(ingresos,text="Atrás",command=minimizar,font=('Comic',10),width=5).place(x=230,y=300)
        ingresos.mainloop()

    #Egresos
    def Egresos():
        def minimizar():
            egresos.destroy()
            menu.deiconify()
        def Agua():
            egresos.deiconify()
            water = Tk()
            water.title("SERVICIO DEL AGUA POTABLE")
            water.geometry("500x400+525+250")
            water.config(bg='beige')
            lista= []
            cond = ['C1\n','C2\n','C3\n','C4\n','C5\n','C6\n','C7\n','C8\n','C9\n','C10\n','C11\n','C12\n','C13\n','C14\n','C15\n','C16\n','C17\n','C18\n','C19\n','C20\n']
            file = open("Ingresos.txt","r")
            for linea in file.readlines():
                lista.append(linea)
                if linea in cond:
                    cond.remove(linea)
            file.close
            agua = str(len(cond)*30)
            title = Label(water,text="SERVICIO AGUA POTABLE",bg='beige',font=('Comic',14)).place(x=160,y=0)
            mensaje = "El monto total para el servicio del agua es: "+agua+" $ USD"
            tag = Label(water,text=mensaje,bg='beige').place(x=100,y=80)
            Button(water,text="Atrás",command=water.destroy).place(x=100,y=210)

        def Luz():
            egresos.deiconify()
            light = Tk()
            light.title("SERVICIO DEL AGUA POTABLE")
            light.geometry("500x400+525+250")
            light.config(bg='beige')
            lista= []
            cond = ['C1\n','C2\n','C3\n','C4\n','C5\n','C6\n','C7\n','C8\n','C9\n','C10\n','C11\n','C12\n','C13\n','C14\n','C15\n','C16\n','C17\n','C18\n','C19\n','C20\n']
            file = open("Ingresos.txt","r")
            for linea in file.readlines():
                lista.append(linea)
                if linea in cond:
                    cond.remove(linea)
            file.close
            luz = str(len(cond)*15)
            title = Label(light,text="SERVICIO LUZ",bg='beige',font=('Comic',14)).place(x=160,y=0)
            mensaje = "El monto total para el servicio de la luz es: "+luz+" $ USD"
            tag = Label(light,text=mensaje,bg='beige').place(x=100,y=80)
            Button(light,text="Atrás",command=light.destroy).place(x=100,y=210)

        def Guardia():
            egresos.deiconify()
            guard = Tk()
            guard.title("SERVICIO DEL AGUA POTABLE")
            guard.geometry("500x400+525+250")
            guard.config(bg='beige')
            lista= []
            cond = ['C1\n','C2\n','C3\n','C4\n','C5\n','C6\n','C7\n','C8\n','C9\n','C10\n','C11\n','C12\n','C13\n','C14\n','C15\n','C16\n','C17\n','C18\n','C19\n','C20\n']
            file = open("Ingresos.txt","r")
            for linea in file.readlines():
                lista.append(linea)
                if linea in cond:
                    cond.remove(linea)
            file.close
            luz = str(len(cond)*20)
            title = Label(guard,text="SERVICIO GUARDIANÍA",bg='beige',font=('Comic',14)).place(x=160,y=0)
            mensaje = "El monto total para el servicio de la guardianía es: "+luz+" $ USD"
            tag = Label(guard,text=mensaje,bg='beige').place(x=100,y=80)
            Button(guard,text="Atrás",command=guard.destroy).place(x=100,y=210)

        menu.iconify()
        egresos = Tk()
        egresos.title("Egresos")
        egresos.geometry("500x400+525+250")
        egresos.config(bg='beige')
        etiqueta1 = Label(egresos,text="MÓDULO DE EGRESOS",font=('Comic',14),bg='beige').place(x=170,y=0)
        Button(egresos,text="Servicio de agua potable",width=20,fg="black",command=Agua).place(x=200,y=100)
        Button(egresos,text="Servicio de la luz",width=20,fg="black",command=Luz).place(x=200,y=150)
        Button(egresos,text="Servicio de la guardianía",width=20,fg="black",command=Guardia).place(x=200,y=200)
        Button(egresos,text="Atrás",command=minimizar,width=20).place(x=200,y=250)

    if verifica_usuario.get()=='Admin' and verifica_clave.get()== '246810' :
        messagebox.showinfo("Exito","Accedio con exito")
        window.destroy()
        menu=Tk()
        menu.title("Administrador de inquilinos")
        menu.geometry('500x400+525+250')
        menu.config(bg='beige')
        Etiqueta_instrucciones=Label(menu,text="Seleccione lo que desea hacer:",font=('Comic',14),bg='beige').place(x=80,y=60)
        Button(menu,text="Ingresos",command=Ingresos,font=('Comic',12),width=10).place(x=100,y=175)
        Button(menu,text="Egresos",command=Egresos,font=('Comic',12),width=10).place(x=300,y=175)
        Button(menu,text="Salir",command=quit,font=('Comic',12),width=7).place(x=215,y=225)
        menu.mainloop()
    else:
        messagebox.showwarning("Error","Usuario y/o clave incorrecta")

window= Tk()
verifica_usuario = StringVar()
verifica_clave = StringVar()
window.title("Administador de inquilinos")
window.geometry('400x300+525+250')
window.config(background='beige')
titulo=Label(window,text='BIENVENIDO',font=('Comic',20),bg='beige').place(x=110,y=0)
titulo=Label(window,text='Inicie sesion',font=('Comic',14),bg='beige').place(x=140,y=50)
etiqueta_login_nombre = Label(window,text="Usuario: ",font=('Comic',10),bg=('beige')).place(x=50,y=100)
entrada_login_nombre = Entry(window,width=24,textvariable=verifica_usuario).place(x=140,y=100)
etiqueta_login_clave = Label(window,text="Contraseña: ",font=('Comic',10),bg='beige').place(x=50,y=125)
entrada_login_clave  = Entry(window,width=24,textvariable=verifica_clave,show="*").place(x=140,y=125)
Button(window,text="Login",command=validar,font=('Comic',12),width=5).place(x=170,y=175)
Button(window,text="Exit",font=('Comic',12),width=5,command=quit).place(x=170,y=210)
window.mainloop()
