from flask import Flask

app = Flask(__name__)

@app.route('/')
def calculadora():
    mensaje = '''
    <h1> Bienvenido a la calculadora de Python<h1>
    <h2> Para sumar escribe en el navegador http://127.0.0.1:5000/sumar <h2>
    <h2> Para restar escribe en el navegador http://127.0.0.1:5000/restar<h2>
    <h2> Para multiplicacion escribe en el navegador http://127.0.0.1:5000/multiplicacion<h2>
    <h2> Para division escribe en el navegador http://127.0.0.1:5000/division<h2>
    <h2> Para saber si un numero es menor escribe en el navegador http://127.0.0.1:5000/menor<h2>
    <h2> Para saber si un numero es mayor escribe en el navegador http://127.0.0.1:5000/mayor<h2>

    <footer>
    LEONARDO VARGAS LOPEZ-
    23308060610434-
    5-D-
    PROGRAMACION
    </footer>
    '''
    return mensaje

@app.route('/sumar/<v1>/<v2>')
def sumar(v1, v2):
    num1 = int(v1)
    num2 = int(v2)
    suma = num1 + num2
    return (f"La suma de {v1} y {v2} es {suma}")

@app.route('/restar/<v1>/<v2>')
def restar(v1, v2):
    num1 = int(v1)
    num2 = int(v2)
    resta = num1 - num2
    return (f"La resta de {v1} y {v2} es {resta}")

@app.route('/multiplicacion/<v1>/<v2>')
def multiplicacion(v1, v2):
    num1 = int(v1)
    num2 = int(v2)
    multiplicacion = num1 * num2
    return (f"La multiplicacion de {v1} y {v2} es {multiplicacion}")

@app.route('/division/<v1>/<v2>')
def division(v1, v2):
    num1 = int(v1)
    num2 = int(v2)
    dividir = num1 / num2
    return (f"La division de {v1} y {v2} es {dividir}")

@app.route('/mayor/<v1>/<v2>')
def mayor(v1, v2):
    num1 = int(v1)
    num2 = int(v2)
    if num1 > num2:
        mayor_numero = num1
        return (f"El mayor número entre {v1} y {v2} es {mayor_numero}")
    elif num2 > num1:
        mayor_numero = num2
        return (f"El mayor número entre {v1} y {v2} es {mayor_numero}")
    else:
        return (f"Los números {v1} y {v2} son iguales")
    
@app.route('/menor/<v1>/<v2>')
def menor(v1, v2):
    num1 = int(v1)
    num2 = int(v2)
    if num1 < num2:
        menor_numero = num1
        return (f"El menor número entre {v1} y {v2} es {menor_numero}")
    elif num2 < num1:
        menor_numero = num2
        return (f"El menor número entre {v1} y {v2} es {menor_numero}")
    else:
        return (f"Los números {v1} y {v2} son iguales")
    

if __name__ == '__main__':
    app.run(debug=True)
