import pyodbc
class Conexion:
    db=None

    def __init__(self):
<<<<<<< HEAD:ERPRH2020-master/Datos/Conexion.py
        self.db=pyodbc.connect(Driver="{SQL Server};", Server="DESKTOP-8SKO2G9\SQLEXPRESS;", db='ERP2020;', Trusted_Connection='yes;')
=======
        self.db=pyodbc.connect(Driver="{SQL Server};", Server="localhost;", db='ERP2020;', Trusted_Connection='yes;')
>>>>>>> 89f7ce5ef98df49b26679279fc1fbada71b63c0c:Datos/Conexion.py

    def getDB(self):
        return self.db

    def cerrar(self):
        self.db.close()
