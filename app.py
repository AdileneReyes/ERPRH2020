from flask import Flask, render_template, request, session, flash
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
@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        server = 'localhost'
        database = 'ERP2020'
        username = request.form['Usuario']
        password = request.form['Contraseña']
        session['usr'] = username
        session['pass'] = password
        cnxn = pyodbc.connect(
            'Driver={ODBC Driver 17 for SQL Server}; SERVER='+server+';DATABASE='+database+';UID='+username+ ';PWD='+password)
        cursor=cnxn.cursor()
        cnxn.close()
    except:
        flash('Datos incorrectos')
    return render_template('Comunes/principal.html')

'''
    udao=UsuarioDAO()
    nombreUsuario=request.form['Usuario']
    contra=request.form['Contraseña']
    u=udao.validar(nombreUsuario,contra)
    if u['id']!=None:
        session['user']=u
        return render_template('Comunes/principal.html', user=session.get('user'))
    else:
        return render_template('Login.html')
'''






if __name__ == '__main__':
    app.run(debug=True)
