from tkinter import *
from tkinter import ttk,messagebox, Tk, PhotoImage

import tkinter as tk
import mysql.connector
import subprocess

# Conectar a la base de datos
def venta():
 def iniciar_sesion():
    global var
    usuario = nombre_usuario.get()
    contrasena = contrasena_usuario.get()
    if usuario == "administrador" and contrasena == "1234":
     resultado.config(text="Inicio de sesión exitoso")
     var="si"
     root.destroy()
    elif usuario == "proveedor" and contrasena == "1982":
     resultado.config(text="inicio sesion exitasamente")
     var="no"  
     root.destroy()
    else:
        resultado.config(text="Nombre de usuario o contraseña incorrectos")  
 global var 
   
 root=tk.Tk()
 root.geometry("300x200")
 root.wm_title("titulo")
 resultadox = tk.Label(text="password ")
 resultadox.place(x=100,y=60)
 nombre_usuario = tk.Entry()
 nombre_usuario.insert(0, "administrador")
 nombre_usuario.place(x=100,y=40)
 resultadol=tk.Label(text="user")
 resultadol.place(x=100,y=20)
 contrasena_usuario = tk.Entry(show="*")
 contrasena_usuario.insert(0, "1234")
 contrasena_usuario.place(x=100,y=80)
         
 iniciar_sion = tk.Button(text="CLICK AQUI", command=iniciar_sesion)
 iniciar_sion.place(x=100,y=100)
 resultado=tk.Label()
 resultado.place(x=100,y=120)
 root.mainloop()     

ventana=tk.Tk()
ventana.geometry("600x500+10+10")
ventana.title(" FONDOS DE PANTALLA ")

imagen=PhotoImage(file="lol.png")
iblimagen=Label(ventana,image=imagen).place(x=0,y=0)
iniciar_sesion=tk.Button(text=" CLICK AQUI ",command=ventana.destroy)
iniciar_sesion.place(x=400,y=410)

ventana.mainloop()





try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="escuela"
    )
except mysql.connector.Error as e:
    messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")
    exit()


# Crear la tabla de alumnos si no existe
mi_cursor = db.cursor()
def mostrar():
    cursor = db.cursor()
    sentencia = "SELECT * FROM alumnos" 
    cursor.execute(sentencia)
    registro = cursor.fetchall()
    return registro
def mostrarP():
    tabla_alumnos.delete(*tabla_alumnos.get_children())
    registro = mostrar()
    i = -1
    for dato in registro:
        i= i+1                       
        tabla_alumnos.insert('',i, text = registro[i][1:1], values=registro[i][0:6]) # type: ignoreTrue





# Función para leer todos los alumnos de la base de datos
def leer_alumnosDB():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM alumnos")
    return cursor.fetchall()

# Función para agregar un nuevo alumno a la base de datos
def agregar_alumnoDB(id,nombre,edad,email,naci):
    cursor = db.cursor()
    a='''INSERT INTO alumnos (id,nombre,edad,email,naci) VALUES ('{}','{}','{}','{}','{}')'''.format(id,nombre, edad, email,naci)
    cursor.execute(a)
    db.commit()
    cursor.close()


# Función para actualizar un alumno existente en la base de datos
def actualizar_alumnoDB(id, nombre, edad, email,naci):
    id=entrada_id.get()
    nombre=entrada_nombre.get()
    edad=entrada_edad.get()
    email=entrada_email.get()
    naci=entrada_naci.get()
    cursor = db.cursor()
    print("UPDATE alumnos SET id = %s, nombre = %s, edad = %s, email = %s, naci = %s WHERE id = %s", (id, nombre, edad,naci, email, id))
    cursor.execute("UPDATE alumnos SET id = %s, nombre = %s, edad = %s, email = %s, naci = %s WHERE id = %s", (id, nombre, edad, email, naci, id))
    db.commit()

# Función para eliminar un alumno existente de la base de datos
def eliminar_alumnoDB(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM alumnos WHERE id = %s", (id,))
    db.commit()

# Función para mostrar una lista de todos los alumnos
def mostrar_alumnos():
    # Limpiar la tabla
    for widget in tabla_alumnos.winfo_children():
        widget.destroy()

    # Obtener todos los alumnos
    alumnos = leer_alumnosDB()

    # Mostrar los alumnos en la tabla
    for i, alumno in enumerate(alumnos):
        id = alumno[0]
        nombre = alumno[1]
        edad = alumno[2]
        email = alumno[3]
        naci = alumno[4]

        Label(tabla_alumnos, text=id).grid(row=i, column=0)
        Label(tabla_alumnos, text=nombre).grid(row=i, column=1)
        Label(tabla_alumnos, text=edad).grid(row=i, column=2)
        Label(tabla_alumnos, text=email).grid(row=i, column=3)    
        Label(tabla_alumnos, text=naci).grid(row=i, column=4)  
        
        mostrar_alumnos
            

# Función para agregar un nuevo alumno
def agregar_alumno():
    # Obtener los datos del nuevo alumno
    id=entrada_id.get()
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    email = entrada_email.get()
    naci = entrada_naci.get()
    # Validar que los campos no estén vacíos
    if not id or not nombre or not edad or not email or not naci:
        messagebox.showerror("Error al agregar el alumno", "Por favor ingrese todos los datos del alumno")
        return

    # Agregar el nuevo alumno
    agregar_alumnoDB(id,nombre,edad,email,naci)
    datos=(nombre, edad, email,naci)
    tabla_alumnos.insert('',0,text=nombre,values=datos)
        
    # Limpiar los campos de entrada
    entrada_id.delete(0,END)
    entrada_nombre.delete(0, END)
    entrada_edad.delete(0, END)
    entrada_email.delete(0, END)
    entrada_naci.delete(0,END)
    
    mostrar_alumnos



# Función para actualizar un alumno existente
def actualizar_alumno():
    # Obtener los datos del alumno a actualizar
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    email = entrada_email.get()
    naci=entrada_naci.get()


    # Validar que los campos no estén vacíos
    if not nombre or not edad or not email or not naci:
        messagebox.showerror("Error al actualizar el alumno", "Por favor ingrese todos los datos del alumno")
        return

    # Actualizar el alumno
    actualizar_alumnoDB(nombre, edad, email,naci)

    # Limpiar los campos de entrada
    entrada_id.delete(0, END)
    entrada_nombre.delete(0, END)
    entrada_edad.delete(0, END)
    entrada_email.delete(0, END)
    entrada_naci.delete(0,END)
    
    mostrar_alumnos



# Función para eliminar un alumno existente
def eliminar_alumno():
    # Obtener el ID del alumno a eliminar
    id = entrada_id.get()

    # Validar que se haya ingresado un ID
    if not id:
        messagebox.showerror("Error al eliminar el alumno", "Por favor ingrese el ID del alumno a eliminar")
        return

    # Preguntar al usuario si está seguro de eliminar el alumno
    confirmar = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de eliminar este alumno?")

    if confirmar:
        # Eliminar el alumno
        eliminar_alumnoDB(id)

        # Limpiar los campos de entrada
        entrada_id.delete(0, END)
        entrada_nombre.delete(0, END)
        entrada_edad.delete(0, END)
        entrada_email.delete(0, END)

        # Mostrar la lista actualizada de alumnos
        mostrar_alumnos()

  




# Crear la ventana principal
ventana = tk.Tk()
ancho_ventana = 480
alto_ventana = 480
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.configure(bg="#BA55D3")

ventana.title("Ejemplo CRUD con Python y MySQL")





# Crear los campos de entrada para los datos del alumno
Label(ventana, text="Id:").grid(row=0, column=0, padx=5, pady=5)
entrada_id = Entry(ventana,bg="aqua")
entrada_id.grid(row=0, column=1, padx=5, pady=5)

Label(ventana, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
entrada_nombre = Entry(ventana,bg="aqua")
entrada_nombre.grid(row=1, column=1, padx=5, pady=5)

Label(ventana, text="Edad:").grid(row=2, column=0, padx=5, pady=5)
entrada_edad = Entry(ventana,bg="aqua")
entrada_edad.grid(row=2, column=1, padx=5, pady=5)

Label(ventana, text="Email:").grid(row=3, column=0, padx=5, pady=5)
entrada_email = Entry(ventana,bg="aqua")
entrada_email.grid(row=3, column=1, padx=5, pady=5)

Label(ventana, text="Naci:").grid(row=4, column=0, padx=5, pady=5)
entrada_naci = Entry(ventana,bg="aqua")
entrada_naci.grid(row=4, column=1, padx=5, pady=5)

# Crear los botones para agregar, actualizar y eliminar alumnos
Button(ventana, text="Agregar alumno", command=agregar_alumno,bg="red").grid(row=0, column=2, padx=5, pady=5)
Button(ventana, text="Actualizar alumno", command=actualizar_alumno,bg="blue").grid(row=1, column=2, padx=5, pady=5)
Button(ventana, text="mostrar tabla", command=mostrarP,bg="blue").grid(row=3, column=2, padx=5, pady=5)
def regresar():
    ventana.destroy()
    subprocess.call(["python", "3.py"]) 
Button(ventana, text="Regresar", command=regresar, font="Times", bg="#585858", fg="white").grid(row=2, column=2, padx=5, pady=5)

# Crear la tabla para mostrar los alumnos
tabla_alumnos=ttk.Treeview(ventana)
tabla_alumnos.grid(row=5, column=1, columnspan=5, padx=5, pady=5)
tabla_alumnos["columns"]=("Id","Nombre","Edad","Email","Naci")
tabla_alumnos.column("#0",width=0,stretch=tk.NO)
tabla_alumnos.column("Id",width=50,anchor=CENTER)
tabla_alumnos.column("Nombre",width=50,anchor=CENTER)
tabla_alumnos.column("Edad",width=50,anchor=CENTER)       
tabla_alumnos.column("Email",width=55,anchor=CENTER)        
tabla_alumnos.column("Naci",width=55,anchor=CENTER)


tabla_alumnos.heading("#0",text="")
tabla_alumnos.heading("Id",text="Id",anchor=CENTER)
tabla_alumnos.heading("Nombre",text="Nombre",anchor=CENTER)
tabla_alumnos.heading("Edad",text="Edad",anchor=CENTER)
tabla_alumnos.heading("Email",text="Email",anchor=CENTER)
tabla_alumnos.heading("Naci",text="Naci",anchor=CENTER)
ban=True
# agregar datos

estilo = ttk.Style(ventana)
estilo.theme_use('alt') 
estilo.configure(".",font= ('Helvetica', 10, 'bold'), foreground='red2')        
estilo.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='green',  background='white')
estilo.map('Treeview',background=[('selected', 'pink2')], foreground=[('selected','blue')] )
        


mostrar_alumnos

# Iniciar el loop de la ventana
ventana.mainloop()

