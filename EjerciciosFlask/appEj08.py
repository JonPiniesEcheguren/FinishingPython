from flask import Flask,Blueprint, request, url_for
from EjerciciosFlask.Ej08_Pseu import principal
app = Flask(__name__)

appEj08= Blueprint('appEj08',__name__,static_folder='static', template_folder='template' )

@appEj08.route("/appEj08")

def home():
    
    return f"""
        <html>
        <body>
            <h1>Determinar Año Bisiesto</h1>
            <form method="post" action="/vej08">
                <label for="numero">Año:</label>
                <input type="number" name="bisiesto" id="bisiesto">
                <br>
                <input type="button" value="Volver" onclick="history.back(-1)" /> 
                <input type="submit" value="Entrar">
            </form>
        </body>
        </html>
    """
@appEj08.route('/vej08', methods=['POST'])

def vej08():
    bisiesto=request.form["bisiesto"]
    resultado= principal(bisiesto)
    return f"""
        <html>
        <body>
            <h1>Determinar Año Bisiesto</h1>
            <p>{resultado}</p>
            <input type="button" value="Volver" onclick="history.back(-1)" /> 
        </body>
        </html>
    """


if __name__ == '__main__':
   app.run(debug=True)