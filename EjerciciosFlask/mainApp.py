from flask import Flask, request, url_for

from EjerciciosFlask.appEj06 import appEj06
from EjerciciosFlask.appEj07 import appEj07 
from EjerciciosFlask.appEj08 import appEj08 
from EjerciciosFlask.appEj11 import appEj11 
from EjerciciosFlask.appEj12 import appEj12 
from EjerciciosFlask.appEj13 import appEj13 


app = Flask(__name__)
app.register_blueprint(appEj06)
app.register_blueprint(appEj07)
app.register_blueprint(appEj08)
app.register_blueprint(appEj11)
app.register_blueprint(appEj12)
app.register_blueprint(appEj13)


@app.route("/")
@app.route("/home")


def home():
    
    return f"""
        <html>
        <body>
            <h1>Menu Aplicaciones HTML</h1>
            <form method="get" action="/appEj06">
                <input  type="submit" value="Ejercicio 6 - Grados Celsius a Farenheit">
            </form>
            <form method="get" action="/appEj07">
                <input  type="submit" value="Ejercicio 7 - Determinar si es Par o Impar">
            </form>
            <form method="get" action="/appEj08">
                <input  type="submit" value="Ejercicio 8 - Determinar Año Bisiesto">
            </form>
            <form method="get" action="/appEj11">
                <input  type="submit" value="Ejercicio 11 - Factorial de un numero">
            </form>
            <form method="get" action="/appEj12">
                <input  type="submit" value="Ejercicio 12 - Numero Primo">
            </form>
            <form method="get" action="/appEj13">
                <input  type="submit" value="Ejercicio 13 - Volumen y Area de un cubo">
            </form>
        </body>
        </html>
    """
#<form method="get" action="/shutdown">
#                <input  type="submit" value="Salir">
#            </form>
#def shutdown_server():
#    func = request.environ.get('werkzeug.server.shutdown')
#    if func is None:
#        raise RuntimeError('Not running with the Werkzeug Server')
#    func()
    
#@app.route('/shutdown')
#def shutdown():
#    shutdown_server()
#    return 'Server shutting down...'

def principal():
    app.run()

if __name__ == '__main__':
   principal()