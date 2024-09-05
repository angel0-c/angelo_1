from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/portaforio')
def portaforio(): 
    return render_template('portaforio.html')

@app.route('/contacto')
def contacto(): 
    return render_template('contacto.html')

@app.route ('/mensaje', methods=['POST'])
def mensaje():
    if request.method == 'POST': 
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        contacto = int(request.form['contacto'])
        correo = request.form['correo']
        asunto = request.form['asunto']   
    return render_template('mensaje.html', res=nombre, pes=apellido, mes=correo, res2=contacto)   

if __name__ == '__main__':
    app.run()