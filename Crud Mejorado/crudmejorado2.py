import tkinter as tk
import mysql.connector
from tkinter import ttk,Label
import subprocess
from tkinter import messagebox

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="escuela"
)

mi_cursor = bd.cursor()
mi_cursor.execute("SELECT id, nombre, edad, email, naci FROM alumnos")
resultado = mi_cursor.fetchall()

# crear ventana de Tkinter
ventana = tk.Tk()
ancho_ventana = 620
alto_ventana = 480
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.title("Registros de alumnos")
primero=tk.Label(ventana, text="- Registro de de alumnos -", bg='#3CB371', fg="white", font='Times 20').pack(pady=30)
# crear Table
tabla_alumno = ttk.Treeview(ventana)
tabla_alumno['columns'] = ('id','nombre','edad', 'email', 'naci')

# ajustar las columnas
tabla_alumno.column('#0', width=0, stretch=tk.NO)
tabla_alumno.column('id', anchor=tk.CENTER, width=50)
tabla_alumno.column('nombre', anchor=tk.CENTER, width=175)
tabla_alumno.column('edad', anchor=tk.CENTER, width=75)
tabla_alumno.column('email', anchor=tk.CENTER, width=220)
tabla_alumno.column('naci', anchor=tk.CENTER, width=50)

# heading
tabla_alumno.heading('#0', text='', anchor=tk.CENTER)
tabla_alumno.heading('id', text='Id', anchor=tk.CENTER)
tabla_alumno.heading('nombre', text='Nombre', anchor=tk.CENTER)
tabla_alumno.heading('edad', text='Edad', anchor=tk.CENTER)
tabla_alumno.heading('email', text='Email', anchor=tk.CENTER)
tabla_alumno.heading('naci', text='Nacimiento', anchor=tk.CENTER)

ban=True
# agregar datos
for valor in resultado:
  if (ban):
    tabla_alumno.insert(parent='', index='end', id=valor[0], tag=['t1'], values=(valor[0], valor[1], valor[2], valor[3], valor[4]))
    ban=False
  else:
    tabla_alumno.insert(parent='', index='end', id=valor[0], tag=['t2'], values=(valor[0], valor[1], valor[2], valor[3], valor[4]))
    ban=True

tabla_alumno.tag_configure('t1', foreground= 'white', background = '#383838', font="Times 12")
tabla_alumno.tag_configure('t2', foreground='#FFCC00', background = '#003366', font="Times 12")

# mostrar tabla en ventana
tabla_alumno.pack()
def regresar ():
    ventana.destroy()
    subprocess.call(["python", "crudmejorado1.py"]) 
button_guardar = tk.Button(ventana, text="Regresar", command=regresar, font="Times", bg="#3CB371", fg="white")
button_guardar.pack(pady=30)
def elimina(id):
    cur = bd.cursor()
    sentencia='''DELETE FROM alumnos WHERE id = {}'''.format(id)
    cur.execute(sentencia)
    bd.commit()    
    cur.close()
def eliminar_alumno():
       id=entrada_id.get()
       if id=="":
           messagebox.showerror("ERROR","INGRESE UN DATO EN LA ID:")
           return  
       elimina(id)
ventana1=ttk.Label(ventana,text=" Colocar id para eliminar    ")
ventana1.place(x=10,y=10)


button_eliminar=tk.Button(ventana,text=" ELIMINAR DATO ",command=eliminar_alumno,font="Times", bg="#3CB371", fg="white")
button_eliminar.pack(pady=5)
entrada_id=ttk.Entry()
entrada_id.place(x=10,y=30)

ventana['bg'] = '#800000'
ventana.resizable(width=0, height=0)
ventana.mainloop()