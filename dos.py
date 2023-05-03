import mysql.connector  #pip install mysql-connector-python
 
class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='alumnos', 
                                            user = 'root',
                                            port="3306",
                                            password ='')



    def inserta_producto(self,nombre, edad, email, naci):
        cur = self.conexion.cursor()
        sql='''INSERT INTO productos (nombre, edad, email, naci) 
        VALUES('{}', '{}','{}', '{}')'''.format(nombre, edad, email, naci)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()


    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM escuela " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_producto(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM escuela WHERE NOMBRE = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 

    def elimina_productos(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM escuela WHERE NOMBRE = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()