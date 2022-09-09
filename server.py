from crypt import methods
from flask import Flask, redirect, render_template, request

from usuario import Usuario

app = Flask(__name__)

@app.route('/users')
def index():
    usuarios = Usuario.get_all()
    print(usuarios)
    return render_template('users.html', usuarios=usuarios)

@app.route('/users/new')
def new():
    return render_template('new.html')

@app.route('/users/add', methods=["POST"])
def add():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'], 
        'email': request.form['email']
    }
    Usuario.save(data)
    return redirect('/users/new')

if __name__ == '__main__':
    app.run(debug=True)