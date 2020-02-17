from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import pyodbc
from Datos.usuarioDAO import UsuarioDAO


app = Flask(__name__)
app.secret_key=b'yangars'


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-8SKO2G9\SQLEXPRESS;'
                      'Database=ERP2020;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()




#Nos direcciona a la pagina para logearse
@app.route('/')
def index():
    return render_template('Login.html')



#Direcciona a la pagina principal del sistema
@app.route('/login', methods=['POST'])
def login():
    udao=UsuarioDAO()
    nombreUsuario=request.form['Usuario']
    contra=request.form['Contraseña']
    u=udao.validar(nombreUsuario,contra)
    if u['id']!=None:
        session['user']=u
        return render_template('Comunes/principal.html', user=session.get('user'))
    else:
        return render_template('Login.html')






if __name__ == '__main__':
    app.run(debug=True)
