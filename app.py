# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash
from passlib.hash import pbkdf2_sha256
from db import insert_employee, get_employee_by_email

app = Flask(__name__)
app.secret_key = 'clave_secreta'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        primer_nombre = request.form['primer_nombre']
        apellido_paterno = request.form['apellido_paterno']
        apellido_materno = request.form['apellido_materno']
        email = request.form['email']
        telefono = request.form['telefono']
        id_puesto = request.form['id_puesto']
        contrasena = request.form['contrasena']
        contrasena_hash = pbkdf2_sha256.hash(contrasena)
        
        insert_employee(primer_nombre, apellido_paterno, apellido_materno, email, telefono, id_puesto, contrasena_hash)
        flash('Registro exitoso. Inicia sesión.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        contrasena = request.form['contrasena']
        empleado = get_employee_by_email(email)
        
        if empleado and pbkdf2_sha256.verify(contrasena, empleado[7]):
            session['user_id'] = empleado[0]
            flash('Inicio de sesión exitoso')
            return redirect(url_for('home'))
        else:
            flash('Correo o contraseña incorrectos')
    
    return render_template('login.html')

@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Sesión cerrada')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
