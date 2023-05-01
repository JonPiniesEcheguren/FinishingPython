from flask import Flask,Blueprint, request, url_for
from EjerciciosFlask.Ej11_Pseu import principal
app = Flask(__name__)

appEj11= Blueprint('appEj11',__name__,static_folder='static', template_folder='template' )

@appEj11.route("/appEj11")

def home():
    
    return f"""
        <html>
        <body>
            <h1>Factorial de un numero</h1>
            <form method="post" action="/vej11">
                <label for="numero">Numero:</label>
                <input type="number" name="factorial" id="factorial">
                <br>
                <input type="button" value="Volver" onclick="history.back(-1)" /> 
                <input type="submit" value="Entrar">
            </form>
        </body>
        </html>
    """
@appEj11.route('/vej11', methods=['POST'])

def vej11():
    factorial=request.form["factorial"]
    resultado= principal(factorial)
    return f"""
        <html>
        <body>
            <h1>Factorial de un numero</h1>
            <p>El factorial del numero introducido es : {resultado}</p>
            <input type="button" value="Volver" onclick="history.back(-1)" /> 
        </body>
        </html>
    """


if __name__ == '__main__':
   app.run(debug=True)